from mangum import Mangum
import os
import sys

# إضافة المجلد الرئيسي إلى مسار البحث
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app import app as flask_app

# ضبط الإعدادات للتأكد من أن التطبيق سيعمل مع Netlify Functions
flask_app.config['SESSION_COOKIE_SECURE'] = True
flask_app.config['SESSION_COOKIE_SAMESITE'] = 'None'

# إنشاء وظيفة لامدا باستخدام Mangum
handler = Mangum(flask_app)