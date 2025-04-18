
import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# تكوين التسجيل
logging.basicConfig(level=logging.INFO)

# Create base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass

# Initialize Flask app
app = Flask(__name__)

# Initialize SQLAlchemy
db = SQLAlchemy(model_class=Base)

# تكوين السر
app.secret_key = os.environ.get("SESSION_SECRET", "ahmed-helly-educational-platform-secret-key")

# تكوين قاعدة البيانات
# استخدام رابط محدد بشكل مباشر لقاعدة بيانات PostgreSQL
DATABASE_URL = "postgresql://neondb_owner:npg_ClcIa2kJ6KUY@ep-lively-mountain-a42ezf7w-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require"

if DATABASE_URL:
    logging.info("استخدام قاعدة بيانات PostgreSQL")
    # استخدام قاعدة بيانات PostgreSQL بالرابط المحدد
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
else:
    # استخدام قاعدة بيانات SQLite كنسخة احتياطية
    instance_db_path = os.path.join(os.getcwd(), 'instance', 'app.db')
    root_db_path = os.path.join(os.getcwd(), 'app.db')

    if os.path.exists(instance_db_path) and os.path.getsize(instance_db_path) > 0:
        db_path = instance_db_path
        logging.info(f"استخدام قاعدة البيانات من مجلد instance: {instance_db_path}")
    else:
        db_path = root_db_path
        logging.info(f"استخدام قاعدة البيانات من المجلد الرئيسي: {root_db_path}")

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

# Initialize the database
db.init_app(app)
