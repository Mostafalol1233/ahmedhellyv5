
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
