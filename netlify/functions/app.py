import base64
import os
import sys
from pathlib import Path

# إضافة المجلد الرئيسي للمشروع إلى مسار البحث عن المكتبات
root_path = Path(__file__).parents[2]
sys.path.insert(0, str(root_path))

from main import app

def handler(event, context):
    """
    وظيفة Lambda لمعالجة طلبات Netlify
    """
    # استخراج معلومات الطلب
    path = event.get('path', '/')
    http_method = event.get('httpMethod', 'GET')
    headers = event.get('headers', {})
    query_string = event.get('queryStringParameters', {}) or {}
    body = event.get('body', '')
    
    # تحويل معلومات الطلب إلى بيئة WSGI
    # معالجة query_string بشكل آمن
    query_string_str = ''
    if query_string:
        query_string_str = '&'.join([f"{k}={v}" for k, v in query_string.items()])
    
    # معالجة body بشكل آمن
    body_length = 0
    if body:
        if isinstance(body, str):
            body_length = len(body)
        elif isinstance(body, bytes):
            body_length = len(body)
    
    environ = {
        'REQUEST_METHOD': http_method,
        'PATH_INFO': path,
        'QUERY_STRING': query_string_str,
        'CONTENT_LENGTH': str(body_length),
        'HTTP': 'on',
        'SERVER_NAME': 'netlify',
        'SERVER_PORT': '443',
        'SERVER_PROTOCOL': 'HTTP/1.1',
        'wsgi.version': (1, 0),
        'wsgi.input': body if body else '',
        'wsgi.errors': sys.stderr,
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
        'wsgi.url_scheme': 'https',
    }
    
    # إضافة الهيدرز للبيئة
    for key, value in headers.items():
        key = key.upper().replace('-', '_')
        if key not in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
            key = 'HTTP_' + key
        environ[key] = value
    
    # متغيرات لتخزين الاستجابة
    response_status = None
    response_headers = []
    response_body = []
    
    # وظيفة لمعالجة الاستجابة من Flask
    def start_response(status, headers):
        nonlocal response_status, response_headers
        response_status = status
        response_headers = headers
    
    # تشغيل تطبيق Flask مع البيئة WSGI المعدة
    result = app(environ, start_response)
    
    # جمع محتوى الاستجابة
    for data in result:
        if data:
            response_body.append(data)
    
    # إعداد الاستجابة النهائية
    if not response_status:
        status_code = 500
        headers_dict = {'Content-Type': 'text/plain'}
        body_content = b'Internal Server Error'
    else:
        # استخراج رمز الحالة من نص الاستجابة
        status_code = int(response_status.split(' ')[0])
        headers_dict = {key: value for key, value in response_headers}
        body_content = b''.join(response_body if response_body else [])
    
    # إذا كان المحتوى ثنائي، فإننا نقوم بتشفيره بالـ base64
    is_base64_encoded = not isinstance(body_content, str)
    if is_base64_encoded:
        body_content = base64.b64encode(body_content).decode('utf-8')
    
    # إرجاع الاستجابة في الشكل المطلوب من Netlify
    return {
        'statusCode': status_code,
        'headers': headers_dict,
        'body': body_content,
        'isBase64Encoded': is_base64_encoded
    }