import os
import sys
import logging
import random
import string
from datetime import datetime, timedelta
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

def generate_random_code(length=8):
    """توليد رمز عشوائي"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def create_sample_videos():
    """إنشاء فيديوهات نموذجية"""
    try:
        # إنشاء ثلاثة فيديوهات
        videos = [
            {
                "title": "مقدمة في الجبر",
                "url": "https://www.youtube.com/watch?v=DCK_IohKSik",
                "description": "شرح أساسيات الجبر والمعادلات",
                "uploaded_by": 1,  # المشرف
                "requires_code": True,
                "points_cost": 50
            },
            {
                "title": "حساب المثلثات",
                "url": "https://www.youtube.com/watch?v=ekEXn1ZoxHE",
                "description": "شرح نظريات حساب المثلثات الأساسية",
                "uploaded_by": 1,  # المشرف
                "requires_code": False,
                "points_cost": 0
            },
            {
                "title": "الإحصاء والاحتمالات",
                "url": "https://www.youtube.com/watch?v=gU9-ktOwWz4",
                "description": "مقدمة في الإحصاء والاحتمالات",
                "uploaded_by": 1,  # المشرف
                "requires_code": True,
                "points_cost": 100
            }
        ]
        
        for video in videos:
            # إضافة تاريخ الإنشاء
            video["created_at"] = datetime.now()
            
            # إنشاء الفيديو
            postgres_session.execute(text("""
                INSERT INTO videos (title, url, description, uploaded_by, created_at, requires_code, points_cost)
                VALUES (:title, :url, :description, :uploaded_by, :created_at, :requires_code, :points_cost)
                RETURNING id
            """), video)
            
        postgres_session.commit()
        logging.info("تم إنشاء الفيديوهات النموذجية بنجاح")
        
        # استرجاع معرفات الفيديوهات
        video_ids = postgres_session.execute(text("SELECT id FROM videos")).fetchall()
        video_ids = [v[0] for v in video_ids]
        
        # إنشاء رموز الوصول للفيديوهات التي تتطلب رمز
        for video_id in video_ids:
            video_info = postgres_session.execute(text(
                "SELECT requires_code FROM videos WHERE id = :id"
            ), {"id": video_id}).fetchone()
            
            if video_info and video_info[0]:  # إذا كان الفيديو يتطلب رمز
                # إنشاء 5 رموز لكل فيديو
                for _ in range(5):
                    code = generate_random_code()
                    postgres_session.execute(text("""
                        INSERT INTO lecture_codes (video_id, code, created_at, is_active)
                        VALUES (:video_id, :code, :created_at, :is_active)
                    """), {
                        "video_id": video_id,
                        "code": code,
                        "created_at": datetime.now(),
                        "is_active": True
                    })
                
        postgres_session.commit()
        logging.info("تم إنشاء رموز الوصول للفيديوهات بنجاح")
        
        return True
    except Exception as e:
        postgres_session.rollback()
        logging.error(f"خطأ عند إنشاء الفيديوهات النموذجية: {str(e)}")
        return False

def create_sample_test():
    """إنشاء اختبار نموذجي"""
    try:
        # إنشاء اختبار
        test = {
            "title": "اختبار الجبر والهندسة",
            "description": "اختبار شامل في الجبر والهندسة والمثلثات",
            "created_by": 1,  # المشرف
            "created_at": datetime.now(),
            "is_active": True,
            "time_limit_minutes": 45,
            "passing_score": 60,
            "max_attempts": 2,
            "access_type": "points",
            "points_required": 50
        }
        
        result = postgres_session.execute(text("""
            INSERT INTO tests (title, description, created_by, created_at, is_active, 
                              time_limit_minutes, passing_score, max_attempts, access_type, points_required)
            VALUES (:title, :description, :created_by, :created_at, :is_active, 
                   :time_limit_minutes, :passing_score, :max_attempts, :access_type, :points_required)
            RETURNING id
        """), test)
        
        test_id = result.fetchone()[0]
        postgres_session.commit()
        logging.info(f"تم إنشاء الاختبار النموذجي برقم {test_id}")
        
        # إنشاء أسئلة الاختبار
        questions = [
            {
                "test_id": test_id,
                "question_text": "ما هو حل المعادلة x² + 5x + 6 = 0؟",
                "question_type": "multiple_choice",
                "points": 10,
                "question_order": 1
            },
            {
                "test_id": test_id,
                "question_text": "ماذا يساوي جيب الزاوية 30 درجة؟",
                "question_type": "multiple_choice",
                "points": 10,
                "question_order": 2
            },
            {
                "test_id": test_id,
                "question_text": "ما هي مساحة دائرة نصف قطرها 5 سم؟",
                "question_type": "multiple_choice",
                "points": 10,
                "question_order": 3
            },
            {
                "test_id": test_id,
                "question_text": "ماذا يساوي 3² × 4³؟",
                "question_type": "multiple_choice",
                "points": 10,
                "question_order": 4
            },
            {
                "test_id": test_id,
                "question_text": "اشرح الفرق بين المتواليات الحسابية والهندسية مع ذكر أمثلة.",
                "question_type": "text",
                "points": 20,
                "question_order": 5
            }
        ]
        
        for question in questions:
            result = postgres_session.execute(text("""
                INSERT INTO test_questions (test_id, question_text, question_type, points, question_order)
                VALUES (:test_id, :question_text, :question_type, :points, :question_order)
                RETURNING id
            """), question)
            
            question_id = result.fetchone()[0]
            
            # إضافة خيارات للأسئلة متعددة الخيارات
            if question["question_type"] == "multiple_choice":
                choices = []
                if question["question_order"] == 1:
                    choices = [
                        {"text": "x = -2, x = -3", "is_correct": True},
                        {"text": "x = 2, x = 3", "is_correct": False},
                        {"text": "x = -2, x = 3", "is_correct": False},
                        {"text": "x = 2, x = -3", "is_correct": False}
                    ]
                elif question["question_order"] == 2:
                    choices = [
                        {"text": "0.5", "is_correct": True},
                        {"text": "0.707", "is_correct": False},
                        {"text": "0.866", "is_correct": False},
                        {"text": "1", "is_correct": False}
                    ]
                elif question["question_order"] == 3:
                    choices = [
                        {"text": "25π سم²", "is_correct": True},
                        {"text": "10π سم²", "is_correct": False},
                        {"text": "50π سم²", "is_correct": False},
                        {"text": "5π سم²", "is_correct": False}
                    ]
                elif question["question_order"] == 4:
                    choices = [
                        {"text": "576", "is_correct": True},
                        {"text": "144", "is_correct": False},
                        {"text": "256", "is_correct": False},
                        {"text": "81", "is_correct": False}
                    ]
                
                for i, choice in enumerate(choices, 1):
                    postgres_session.execute(text("""
                        INSERT INTO question_choices (question_id, choice_text, is_correct, choice_order)
                        VALUES (:question_id, :choice_text, :is_correct, :choice_order)
                    """), {
                        "question_id": question_id,
                        "choice_text": choice["text"],
                        "is_correct": choice["is_correct"],
                        "choice_order": i
                    })
        
        postgres_session.commit()
        logging.info("تم إنشاء أسئلة وخيارات الاختبار النموذجي بنجاح")
        
        return True
    except Exception as e:
        postgres_session.rollback()
        logging.error(f"خطأ عند إنشاء الاختبار النموذجي: {str(e)}")
        return False

if __name__ == "__main__":
    logging.info("بدء إنشاء المحتوى النموذجي")
    
    videos_created = create_sample_videos()
    tests_created = create_sample_test()
    
    if videos_created and tests_created:
        logging.info("تم إنشاء المحتوى النموذجي بنجاح")
    else:
        logging.error("حدث خطأ أثناء إنشاء المحتوى النموذجي")
    
    # إغلاق الجلسة
    postgres_session.remove()