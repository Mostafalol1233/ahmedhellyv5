import os
import sys
import logging
from datetime import datetime
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session

# تعيين تسجيل الأحداث
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# محركات قواعد البيانات
sqlite_path = os.path.join(os.getcwd(), 'instance', 'app.db')
sqlite_uri = f"sqlite:///{sqlite_path}"
postgres_uri = os.environ.get('DATABASE_URL')

if not postgres_uri:
    logging.error("متغير DATABASE_URL غير موجود في البيئة")
    sys.exit(1)

logging.info(f"قاعدة بيانات SQLite: {sqlite_uri}")
logging.info(f"قاعدة بيانات PostgreSQL: {postgres_uri}")

# إنشاء محركات وجلسات لكلتا قاعدتي البيانات
try:
    sqlite_engine = create_engine(sqlite_uri)
    sqlite_session = scoped_session(sessionmaker(bind=sqlite_engine))
    
    postgres_engine = create_engine(postgres_uri)
    postgres_session = scoped_session(sessionmaker(bind=postgres_engine))
    
    logging.info("تم الاتصال بكلتا قاعدتي البيانات بنجاح")
except Exception as e:
    logging.error(f"خطأ عند الاتصال بقواعد البيانات: {str(e)}")
    sys.exit(1)

# تحديد الجداول التي سيتم ترحيلها
tables = [
    'users',
    'point_transfers',
    'videos',
    'comments',
    'posts',
    'lecture_codes',
    'video_views',
    'video_likes',
    'student_notes',
    'ai_chat_messages',
    'direct_messages',
    'tests',
    'test_questions',
    'question_choices',
    'test_attempts',
    'test_answers',
    'test_retry_requests'
]

# القراءة والترحيل
def migrate_table(table_name):
    try:
        # الحصول على البيانات من SQLite
        sqlite_data = sqlite_session.execute(text(f"SELECT * FROM {table_name}")).fetchall()
        if not sqlite_data:
            logging.warning(f"الجدول {table_name} فارغ")
            return 0
        
        # الحصول على أسماء الأعمدة من SQLite
        columns = sqlite_session.execute(text(f"PRAGMA table_info({table_name})")).fetchall()
        column_names = [col[1] for col in columns]
        
        # الحصول على معلومات الأعمدة من PostgreSQL
        try:
            postgres_columns_info = postgres_session.execute(text(f"""
                SELECT column_name, data_type
                FROM information_schema.columns
                WHERE table_name = '{table_name}'
            """)).fetchall()
            postgres_column_types = {col[0]: col[1] for col in postgres_columns_info}
            
            # الحصول على أسماء الأعمدة الفعلية في PostgreSQL (للتعامل مع كلمات مفتاحية مثل order)
            postgres_column_names = [col[0] for col in postgres_columns_info]
        except Exception as e:
            logging.warning(f"خطأ عند الحصول على معلومات الأعمدة: {str(e)}")
            postgres_column_types = {}
            postgres_column_names = []
        
        # حذف البيانات الموجودة في PostgreSQL
        try:
            postgres_session.execute(text(f"DELETE FROM {table_name}"))
        except Exception as e:
            logging.warning(f"خطأ عند حذف البيانات الموجودة: {str(e)}")
            postgres_session.rollback()
        
        # تعديل أسماء الأعمدة المحجوزة
        postgres_column_mapping = {}
        for col in column_names:
            if col == 'order':
                # إذا كان PostgreSQL يستخدم اسم عمود مختلف لـ 'order'
                if 'item_order' in postgres_column_names:
                    postgres_column_mapping[col] = 'item_order'
                elif 'question_order' in postgres_column_names:
                    postgres_column_mapping[col] = 'question_order'
                elif 'choice_order' in postgres_column_names:
                    postgres_column_mapping[col] = 'choice_order'
                else:
                    # إذا لم نجد اسم بديل، سنتخطى هذا العمود
                    postgres_column_mapping[col] = None
            else:
                postgres_column_mapping[col] = col
        
        # إدراج البيانات في PostgreSQL
        count = 0
        for row in sqlite_data:
            # تحويل الصفوف إلى قاموس
            row_dict = dict(zip(column_names, row))
            
            # إنشاء قاموس للإدراج مع الأعمدة الصحيحة
            insert_dict = {}
            for col, val in row_dict.items():
                # إذا كان العمود محجوزًا (مثل order)، استخدم الاسم البديل
                if postgres_column_mapping.get(col) is None:
                    continue  # تخطي العمود إذا لم يكن له مقابل
                
                mapped_col = postgres_column_mapping.get(col, col)
                
                # تحويل القيم بناءً على نوع البيانات
                if mapped_col in postgres_column_types:
                    # تحويل القيم المنطقية (Boolean)
                    if postgres_column_types[mapped_col] == 'boolean' and isinstance(val, int):
                        insert_dict[mapped_col] = bool(val)
                    # التعامل مع تحويل القيم الرقمية الكبيرة
                    elif postgres_column_types[mapped_col] in ('integer', 'bigint', 'smallint') and isinstance(val, int):
                        if postgres_column_types[mapped_col] == 'smallint' and val > 32767:
                            insert_dict[mapped_col] = 32767
                        elif postgres_column_types[mapped_col] == 'integer' and val > 2147483647:
                            insert_dict[mapped_col] = 2147483647
                        else:
                            insert_dict[mapped_col] = val
                    else:
                        insert_dict[mapped_col] = val
                else:
                    insert_dict[mapped_col] = val
            
            # حذف الأعمدة التي لا توجد في PostgreSQL
            for col in list(insert_dict.keys()):
                if col not in postgres_column_names:
                    del insert_dict[col]
            
            if not insert_dict:
                logging.warning(f"تخطي صف فارغ في جدول {table_name}")
                continue
            
            # بناء SQL للإدراج
            columns_str = ', '.join(insert_dict.keys())
            placeholders = ', '.join([f':{col}' for col in insert_dict.keys()])
            
            if not columns_str or not placeholders:
                logging.warning(f"تخطي صف بدون أعمدة صالحة في جدول {table_name}")
                continue
            
            insert_sql = text(f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})")
            
            try:
                # تنفيذ عملية الإدراج
                postgres_session.execute(insert_sql, insert_dict)
                count += 1
            except Exception as row_error:
                logging.warning(f"خطأ عند إدراج صف في جدول {table_name}: {str(row_error)}")
                # الاستمرار مع الصف التالي
                continue
        
        # تأكيد الإدراج
        try:
            postgres_session.commit()
            logging.info(f"تم ترحيل {count} صفوف من جدول {table_name} بنجاح")
        except Exception as commit_error:
            postgres_session.rollback()
            logging.error(f"خطأ عند تأكيد الإدراج في جدول {table_name}: {str(commit_error)}")
            
        return count
    except Exception as e:
        postgres_session.rollback()
        logging.error(f"خطأ عند ترحيل جدول {table_name}: {str(e)}")
        return 0

def reset_sequences():
    """إعادة تعيين تسلسلات المعرفات التلقائية في PostgreSQL"""
    try:
        logging.info("إعادة تعيين تسلسلات المعرفات التلقائية...")
        # الحصول على جميع التسلسلات
        sequences = postgres_session.execute(text("""
            SELECT sequence_name FROM information_schema.sequences 
            WHERE sequence_schema = 'public'
        """)).fetchall()
        
        for seq in sequences:
            seq_name = seq[0]
            table_name = seq_name.replace('_id_seq', '')
            
            # الحصول على أقصى قيمة معرف من الجدول
            result = postgres_session.execute(text(f"""
                SELECT MAX(id) FROM {table_name}
            """)).fetchone()
            
            if result and result[0] is not None:
                max_id = result[0]
                # تعيين التسلسل إلى القيمة التالية بعد أقصى قيمة
                postgres_session.execute(text(f"""
                    SELECT setval('{seq_name}', {max_id} + 1, false)
                """))
                logging.info(f"تم تعيين تسلسل {seq_name} إلى {max_id + 1}")
            else:
                logging.info(f"الجدول {table_name} فارغ، تسلسل {seq_name} بقي كما هو")
        
        postgres_session.commit()
        return True
    except Exception as e:
        postgres_session.rollback()
        logging.error(f"خطأ عند إعادة تعيين التسلسلات: {str(e)}")
        return False

# ترتيب الجداول المعتمد على قيود المفاتيح الخارجية
dependency_order = [
    'users',
    'videos',
    'lecture_codes',
    'tests',
    'test_questions',
    'question_choices',
    'test_attempts',
    'test_answers',
    'test_retry_requests',
    'point_transfers',
    'points_logs',
    'posts',
    'comments',
    'video_views',
    'video_likes',
    'student_notes',
    'ai_chat_messages',
    'direct_messages',
]

# تعطيل قيود المفاتيح الخارجية مؤقتًا
def disable_foreign_key_constraints():
    try:
        postgres_session.execute(text("SET session_replication_role = 'replica';"))
        logging.info("تم تعطيل قيود المفاتيح الخارجية مؤقتًا")
        return True
    except Exception as e:
        logging.error(f"خطأ عند تعطيل قيود المفاتيح الخارجية: {str(e)}")
        return False

# إعادة تفعيل قيود المفاتيح الخارجية
def enable_foreign_key_constraints():
    try:
        postgres_session.execute(text("SET session_replication_role = 'origin';"))
        logging.info("تم إعادة تفعيل قيود المفاتيح الخارجية")
        return True
    except Exception as e:
        logging.error(f"خطأ عند إعادة تفعيل قيود المفاتيح الخارجية: {str(e)}")
        return False

# بدء عملية الترحيل
def start_migration():
    total_start_time = datetime.now()
    total_rows = 0
    success_tables = 0
    
    logging.info("=== بدء ترحيل البيانات ===")
    
    # نحن لا نستطيع تعطيل قيود المفاتيح الخارجية، لذلك سنستخدم ترتيب الجداول الصحيح
    
    # حاول السماح بالمتابعة رغم الأخطاء
    try:
        # أولاً، احصل على بيانات المستخدمين
        if 'users' in tables:
            start_time = datetime.now()
            logging.info("ترحيل جدول users...")
            rows = migrate_table('users')
            if rows > 0:
                success_tables += 1
                total_rows += rows
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            logging.info(f"استغرق ترحيل users {duration:.2f} ثواني")
            
        # ثم قم بترحيل بقية الجداول حسب الترتيب المعتمد
        for table in dependency_order:
            if table != 'users' and table in tables:  # تخطي جدول users لأننا قمنا بترحيله بالفعل
                start_time = datetime.now()
                logging.info(f"ترحيل جدول {table}...")
                rows = migrate_table(table)
                
                if rows > 0:
                    success_tables += 1
                    total_rows += rows
                    
                end_time = datetime.now()
                duration = (end_time - start_time).total_seconds()
                logging.info(f"استغرق ترحيل {table} {duration:.2f} ثواني")
    except Exception as e:
        logging.error(f"خطأ أثناء عملية الترحيل: {str(e)}")
    
    # إعادة تعيين التسلسلات
    reset_sequences()
    
    total_end_time = datetime.now()
    total_duration = (total_end_time - total_start_time).total_seconds()
    
    logging.info("=== تقرير ترحيل البيانات ===")
    logging.info(f"عدد الجداول التي تم ترحيلها: {success_tables}/{len(tables)}")
    logging.info(f"إجمالي الصفوف التي تم ترحيلها: {total_rows}")
    logging.info(f"إجمالي الوقت المستغرق: {total_duration:.2f} ثواني")

if __name__ == "__main__":
    start_migration()
    
    # إغلاق الجلسات والمحركات
    sqlite_session.remove()
    postgres_session.remove()
    
    logging.info("تم إكمال عملية الترحيل")