#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
منصة الأستاذ أحمد حلي التعليمية
Main application entry point
"""

import os
import logging
from app import app, db
from flask_login import LoginManager

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'يرجى تسجيل الدخول للوصول إلى هذه الصفحة.'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))

# Import routes after app initialization
from routes import main_bp, admin_bp, student_bp
from test_routes import test_bp
from sms_routes import sms_bp
from payment_routes import payment_bp

# Register blueprints
app.register_blueprint(main_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(student_bp, url_prefix='/student')
app.register_blueprint(test_bp, url_prefix='/test')
app.register_blueprint(sms_bp, url_prefix='/sms')
app.register_blueprint(payment_bp, url_prefix='/payment')

if __name__ == '__main__':
    with app.app_context():
        # Create database tables
        db.create_all()
        
        # Create default admin user if not exists
        from models import User
        admin_user = User.query.filter_by(username='admin').first()
        if not admin_user:
            admin_user = User(
                username='admin',
                full_name='مدير النظام',
                role='admin',
                points=10000
            )
            admin_user.set_password('password')
            db.session.add(admin_user)
            
        # Create default student user if not exists
        student_user = User.query.filter_by(username='student').first()
        if not student_user:
            student_user = User(
                username='student',
                full_name='طالب تجريبي',
                role='student',
                points=100
            )
            student_user.set_password('password')
            db.session.add(student_user)
            
        try:
            db.session.commit()
            print("✓ تم إنشاء المستخدمين الافتراضيين")
            print("👤 المدير: admin / password")
            print("🎓 الطالب: student / password")
        except Exception as e:
            db.session.rollback()
            print(f"خطأ في إنشاء المستخدمين: {e}")
    
    app.run(host='0.0.0.0', port=5000, debug=True)