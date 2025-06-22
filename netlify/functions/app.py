import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# Import the Flask app once at module level
from main import app

def handler(event, context):
    """Netlify function handler - simplified approach"""
    
    # Get request details from Netlify event
    path = event.get('path', '/')
    method = event.get('httpMethod', 'GET')
    headers = event.get('headers', {})
    query_params = event.get('queryStringParameters') or {}
    body = event.get('body', '')
    
    # Build query string
    query_string = ''
    if query_params:
        query_string = '&'.join([f'{k}={v}' for k, v in query_params.items()])
    
    try:
        # Use Flask test client for clean request handling
        with app.test_client() as client:
            
            # Make request to Flask app
            if method == 'GET':
                flask_response = client.get(path, query_string=query_string)
            elif method == 'POST':
                flask_response = client.post(path, data=body, query_string=query_string)
            elif method == 'PUT':
                flask_response = client.put(path, data=body, query_string=query_string)
            elif method == 'DELETE':
                flask_response = client.delete(path, query_string=query_string)
            else:
                # Default to GET for unknown methods
                flask_response = client.get(path, query_string=query_string)
            
            # Extract response data
            response_body = flask_response.get_data(as_text=True)
            response_headers = dict(flask_response.headers)
            response_status = flask_response.status_code
            
            # Ensure proper content type
            if 'Content-Type' not in response_headers:
                if path.endswith('.css'):
                    response_headers['Content-Type'] = 'text/css'
                elif path.endswith('.js'):
                    response_headers['Content-Type'] = 'application/javascript'
                else:
                    response_headers['Content-Type'] = 'text/html; charset=utf-8'
            
            # Return Netlify function response
            return {
                'statusCode': response_status,
                'headers': response_headers,
                'body': response_body
            }
            
    except Exception as e:
        # Simple error response
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