import os
import sys
import logging
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session

# تكوين التسجيل
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# الحصول على رابط قاعدة بيانات PostgreSQL
postgres_uri = os.environ.get('DATABASE_URL')

if not postgres_uri:
    logging.error("متغير DATABASE_URL غير موجود في البيئة")
    sys.exit(1)

# إنشاء جلسة PostgreSQL
try:
    postgres_engine = create_engine(postgres_uri)
    postgres_session = scoped_session(sessionmaker(bind=postgres_engine))
    logging.info("تم الاتصال بقاعدة بيانات PostgreSQL بنجاح")
except Exception as e:
    logging.error(f"خطأ عند الاتصال بقاعدة بيانات PostgreSQL: {str(e)}")
    sys.exit(1)

# قائمة الجداول بترتيب عكسي لتلافي مشاكل المفاتيح الخارجية
tables = [
    'test_answers',
    'test_retry_requests',
    'test_attempts',
    'question_choices',
    'test_questions',
    'tests',
    'direct_messages',
    'ai_chat_messages',
    'student_notes',
    'video_likes',
    'video_views',
    'comments',
    'posts',
    'lecture_codes',
    'videos',
    'point_transfers',
    'points_logs',
    'users'
]

def clear_tables():
    """حذف جميع البيانات من جداول PostgreSQL"""
    try:
        # تعطيل قيود المفاتيح الخارجية مؤقتًا إذا كان الأمر ممكنًا
        try:
            postgres_session.execute(text("SET session_replication_role = 'replica';"))
            logging.info("تم تعطيل قيود المفاتيح الخارجية مؤقتًا")
        except Exception as e:
            logging.warning(f"لا يمكن تعطيل قيود المفاتيح الخارجية: {str(e)}")
        
        for table in tables:
            try:
                result = postgres_session.execute(text(f"DELETE FROM {table}"))
                postgres_session.commit()
                logging.info(f"تم حذف البيانات من جدول {table}")
            except Exception as e:
                postgres_session.rollback()
                logging.error(f"خطأ عند حذف البيانات من جدول {table}: {str(e)}")
        
        # إعادة تفعيل قيود المفاتيح الخارجية
        try:
            postgres_session.execute(text("SET session_replication_role = 'origin';"))
            logging.info("تم إعادة تفعيل قيود المفاتيح الخارجية")
        except Exception as e:
            logging.warning(f"لا يمكن إعادة تفعيل قيود المفاتيح الخارجية: {str(e)}")
            
        return True
    except Exception as e:
        logging.error(f"خطأ أثناء حذف البيانات: {str(e)}")
        return False

def reset_sequences():
    """إعادة تعيين تسلسلات المعرفات التلقائية"""
    try:
        # الحصول على جميع التسلسلات
        sequences = postgres_session.execute(text("""
            SELECT sequence_name FROM information_schema.sequences 
            WHERE sequence_schema = 'public'
        """)).fetchall()
        
        for seq in sequences:
            seq_name = seq[0]
            # إعادة تعيين التسلسل إلى 1
            postgres_session.execute(text(f"""
                ALTER SEQUENCE {seq_name} RESTART WITH 1
            """))
            logging.info(f"تم إعادة تعيين تسلسل {seq_name} للبدء من 1")
            
        postgres_session.commit()
        return True
    except Exception as e:
        postgres_session.rollback()
        logging.error(f"خطأ عند إعادة تعيين التسلسلات: {str(e)}")
        return False

if __name__ == "__main__":
    logging.info("بدء عملية تنظيف قاعدة البيانات")
    
    cleared = clear_tables()
    if cleared:
        reset = reset_sequences()
        if reset:
            logging.info("تم تنظيف قاعدة البيانات بنجاح وإعادة تعيين التسلسلات")
        else:
            logging.warning("تم تنظيف قاعدة البيانات ولكن فشلت عملية إعادة تعيين التسلسلات")
    else:
        logging.error("فشلت عملية تنظيف قاعدة البيانات")
    
    # إغلاق الجلسة
    postgres_session.remove()