from flask import render_template
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from app import app, db, logging
import os

# Initialize CSRF protection
csrf = CSRFProtect(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'main.login'

# Error handlers
@app.errorhandler(403)
def forbidden(e):
    logging.error(f"403 Forbidden error: {str(e)}")
    return render_template('403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
    logging.error(f"404 Page not found error: {str(e)}")
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    import traceback
    error_details = traceback.format_exc()
    logging.error(f"500 Internal server error: {str(e)}\nTraceback:\n{error_details}")
    return render_template('500.html'), 500

# Database is already initialized in app.py


# Import and register blueprints
with app.app_context():
    import models
    from routes import main_bp, admin_bp, student_bp
    from test_routes import admin_tests, student_tests
    import payment_routes
    import sms_routes

    # Create tables
    db.create_all()

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(student_bp, url_prefix='/student')
    app.register_blueprint(admin_tests, url_prefix='/admin/tests')
    app.register_blueprint(student_tests, url_prefix='/student/tests')
    app.register_blueprint(payment_routes.payment_bp, url_prefix='/payment')
    app.register_blueprint(sms_routes.sms_bp, url_prefix='/sms')

    # User loader
    @login_manager.user_loader
    def load_user(user_id):
        return models.User.query.get(int(user_id))

    # التحقق من المستخدمين النشطين
    def check_users():
        admin_exists = models.User.query.filter_by(role='admin').first() is not None
        student_exists = models.User.query.filter_by(role='student').first() is not None

        if not admin_exists:
            logging.warning("تنبيه: لا يوجد مستخدم بصلاحية المشرف! استخدم create_users.py لإنشاء مستخدمين.")

        if not student_exists:
            logging.warning("تنبيه: لا يوجد مستخدم بصلاحية الطالب! استخدم create_users.py لإنشاء مستخدمين.")

        active_users = models.User.query.all()
        print("المستخدمون النشطون:")
        print("==================")
        for user in active_users:
            print(f"- {user.full_name or user.username} ({user.username})")
        print("==================")

    # تنفيذ التحقق
    check_users()

def check_if_first_run():
    """Check if this is the first run by checking if an indicator file exists"""
    indicator_file = os.path.join(os.getcwd(), 'first_run_complete.txt')
    if not os.path.exists(indicator_file):
        try:
            from create_test import create_sample_test
            with app.app_context():
                test = create_sample_test()
                logging.info(f"Created sample test: {test.title}")

            with open(indicator_file, 'w') as f:
                f.write('First run completed at: ' + 
                        __import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            logging.info("First run setup completed")
        except Exception as e:
            logging.error(f"Error during first run setup: {str(e)}")

if __name__ == "__main__":
    check_if_first_run()

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        threaded=True
    )