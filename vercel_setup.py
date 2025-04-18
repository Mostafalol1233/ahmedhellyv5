#!/usr/bin/env python
"""
سكريبت إعداد لنشر التطبيق على Vercel.
يقوم هذا السكريبت بإنشاء المجلدات والملفات اللازمة لنشر التطبيق على Vercel.
"""

import os
import sys
import json
import logging
from pathlib import Path

# إعداد التسجيل
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# المسار الحالي للتطبيق
BASE_DIR = Path(__file__).resolve().parent

def setup_vercel_environment():
    """إعداد بيئة Vercel"""
    try:
        # إنشاء ملف .env للتطوير المحلي
        env_file = BASE_DIR / '.env'
        if not env_file.exists():
            with open(env_file, 'w', encoding='utf-8') as f:
                f.write("""# بيئة التطوير المحلية
DATABASE_URL=sqlite:///instance/app.db
SESSION_SECRET=your-local-secret-key-change-this-in-production
FLASK_ENV=development
""")
            logger.info("تم إنشاء ملف .env")
        
        # التحقق من وجود ملف vercel.json
        vercel_json = BASE_DIR / 'vercel.json'
        if not vercel_json.exists():
            # إنشاء ملف vercel.json إذا لم يكن موجودًا
            vercel_config = {
                "version": 2,
                "builds": [
                    {
                        "src": "main.py",
                        "use": "@vercel/python",
                        "config": {
                            "runtime": "python3.9",
                            "maxLambdaSize": "15mb"
                        }
                    }
                ],
                "routes": [
                    {
                        "src": "/(.*)",
                        "dest": "main.py"
                    }
                ],
                "env": {
                    "PYTHONUNBUFFERED": "1"
                }
            }
            
            with open(vercel_json, 'w', encoding='utf-8') as f:
                json.dump(vercel_config, f, indent=2)
            logger.info("تم إنشاء ملف vercel.json")
        
        # التأكد من وجود مجلد للملفات الثابتة
        static_dir = BASE_DIR / 'static'
        if not static_dir.exists():
            os.makedirs(static_dir)
            logger.info("تم إنشاء مجلد static")
        
        # إنشاء ملف اختبار لضمان نشر المجلد
        static_test_file = static_dir / '.vercel_static_files'
        if not static_test_file.exists():
            with open(static_test_file, 'w', encoding='utf-8') as f:
                f.write("# هذا الملف موجود لضمان نشر مجلد static على Vercel")
        
        logger.info("تم إكمال إعداد البيئة بنجاح!")
        return True
        
    except Exception as e:
        logger.error(f"حدث خطأ أثناء إعداد البيئة: {str(e)}")
        return False

def verify_requirements():
    """التحقق من وجود المكتبات المطلوبة للنشر"""
    try:
        # قائمة المكتبات الأساسية المطلوبة
        required_packages = [
            'flask', 'flask-sqlalchemy', 'flask-login', 'flask-wtf', 
            'gunicorn', 'psycopg2-binary', 'requests'
        ]
        
        # إختبار استيراد كل مكتبة
        missing_packages = []
        for package in required_packages:
            package_name = package.replace('-', '_')
            try:
                __import__(package_name)
            except ImportError:
                missing_packages.append(package)
        
        if missing_packages:
            logger.warning(f"المكتبات التالية مفقودة ويجب تثبيتها: {', '.join(missing_packages)}")
            return False
        
        logger.info("جميع المكتبات المطلوبة متوفرة!")
        return True
            
    except Exception as e:
        logger.error(f"حدث خطأ أثناء التحقق من المكتبات: {str(e)}")
        return False

def main():
    """الوظيفة الرئيسية للسكريبت"""
    logger.info("بدء إعداد Vercel...")
    
    if setup_vercel_environment():
        logger.info("تم إعداد بيئة Vercel بنجاح.")
    else:
        logger.error("فشل في إعداد بيئة Vercel.")
    
    if verify_requirements():
        logger.info("تم التحقق من المكتبات المطلوبة بنجاح.")
    else:
        logger.warning("هناك مكتبات مفقودة. يرجى تثبيتها قبل النشر.")
    
    logger.info("""
==============================================
            إعداد Vercel مكتمل!
==============================================

للنشر على Vercel:

1. قم بتسجيل الدخول إلى حسابك على Vercel
2. انقر على "New Project"
3. استورد المشروع من GitHub
4. قم بتكوين المشروع:
   - Framework Preset: Other
   - Root Directory: ./
   - Build Command: اترك فارغًا
   - Output Directory: اترك فارغًا
5. انقر على "Deploy"
6. بعد النشر، يجب إعداد متغيرات البيئة:
   - DATABASE_URL: رابط قاعدة البيانات PostgreSQL
   - SESSION_SECRET: مفتاح سري للجلسات

يمكنك استخدام سكريبت db_migrate.py لإنشاء جداول قاعدة البيانات بعد النشر.
==============================================
""")

if __name__ == "__main__":
    main()