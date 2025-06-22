import sys
import os
import json

# Add the project root to Python path
project_root = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.insert(0, project_root)

# Import the Flask app once at module level
try:
    from main import app
except ImportError as e:
    print(f"Import error: {e}")
    app = None

def handler(event, context):
    """Netlify function handler for Flask app"""
    
    if app is None:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': 'Flask app failed to initialize'})
        }
    
    # Get request details from Netlify event
    path = event.get('path', '/')
    method = event.get('httpMethod', 'GET')
    headers = event.get('headers', {})
    query_params = event.get('queryStringParameters') or {}
    body = event.get('body', '')
    is_base64 = event.get('isBase64Encoded', False)
    
    # Handle base64 encoded body
    if is_base64 and body:
        import base64
        body = base64.b64decode(body).decode('utf-8')
    
    # Build query string
    query_string = ''
    if query_params:
        query_string = '&'.join([f'{k}={v}' for k, v in query_params.items()])
    
    try:
        # Create a proper WSGI environ for Flask
        environ = {
            'REQUEST_METHOD': method,
            'PATH_INFO': path,
            'QUERY_STRING': query_string,
            'CONTENT_TYPE': headers.get('content-type', ''),
            'CONTENT_LENGTH': str(len(body)) if body else '0',
            'SERVER_NAME': headers.get('host', 'localhost').split(':')[0],
            'SERVER_PORT': '80',
            'wsgi.version': (1, 0),
            'wsgi.url_scheme': 'https',
            'wsgi.input': None,
            'wsgi.errors': sys.stderr,
            'wsgi.multithread': False,
            'wsgi.multiprocess': True,
            'wsgi.run_once': False,
        }
        
        # Add headers to environ
        for key, value in headers.items():
            key = key.upper().replace('-', '_')
            if key not in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
                environ[f'HTTP_{key}'] = value
        
        # Use Flask test client for proper request handling
        if app is not None:
            with app.test_client() as client:
                client.environ_base.update(environ)
            
                # Make request based on method
                if method == 'GET':
                    flask_response = client.get(path, query_string=query_string)
                elif method == 'POST':
                    content_type = headers.get('content-type', 'application/x-www-form-urlencoded')
                    if 'application/json' in content_type:
                        flask_response = client.post(path, json=json.loads(body) if body else {}, query_string=query_string)
                    else:
                        flask_response = client.post(path, data=body, query_string=query_string, content_type=content_type)
                elif method == 'PUT':
                    flask_response = client.put(path, data=body, query_string=query_string)
                elif method == 'DELETE':
                    flask_response = client.delete(path, query_string=query_string)
                else:
                    flask_response = client.get(path, query_string=query_string)
            
                # Extract response data
                response_body = flask_response.get_data(as_text=True)
                response_headers = dict(flask_response.headers)
                response_status = flask_response.status_code
                
                # Clean up headers for Netlify
                clean_headers = {}
                for key, value in response_headers.items():
                    if key.lower() not in ['content-length', 'transfer-encoding']:
                        clean_headers[key] = str(value)
                
                # Ensure proper content type
                if 'Content-Type' not in clean_headers:
                    if path.endswith('.css'):
                        clean_headers['Content-Type'] = 'text/css'
                    elif path.endswith('.js'):
                        clean_headers['Content-Type'] = 'application/javascript'
                    elif path.endswith('.json'):
                        clean_headers['Content-Type'] = 'application/json'
                    else:
                        clean_headers['Content-Type'] = 'text/html; charset=utf-8'
                
                return {
                    'statusCode': response_status,
                    'headers': clean_headers,
                    'body': response_body
                }
            
    except Exception as e:
        import traceback
        error_trace = traceback.format_exc()
        
        # Log error for debugging
        print(f"Error in Netlify function: {str(e)}")
        print(f"Traceback: {error_trace}")
        
        # Return error response
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'text/html; charset=utf-8'},
            'body': f'''
            <!DOCTYPE html>
            <html lang="ar" dir="rtl">
            <head>
                <meta charset="UTF-8">
                <title>منصة الأستاذ أحمد حلي - خطأ مؤقت</title>
                <style>
                    body {{ 
                        font-family: Arial, sans-serif; 
                        text-align: center; 
                        padding: 50px;
                        background: #f4f4f4;
                    }}
                    .error {{ 
                        background: white; 
                        padding: 30px; 
                        border-radius: 10px; 
                        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                        max-width: 500px;
                        margin: 0 auto;
                    }}
                </style>
            </head>
            <body>
                <div class="error">
                    <h2>منصة الأستاذ أحمد حلي التعليمية</h2>
                    <p>عذراً، يحدث إعداد للمنصة حالياً</p>
                    <p>الرجاء المحاولة خلال دقائق قليلة</p>
                    <button onclick="location.reload()">إعادة المحاولة</button>
                </div>
            </body>
            </html>
            '''
        }