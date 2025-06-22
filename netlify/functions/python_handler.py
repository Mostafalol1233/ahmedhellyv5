#!/usr/bin/env python3
import sys
import json
import os

# Add project root to path
project_root = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.insert(0, project_root)

def main():
    try:
        # Read event data from stdin
        event_data = json.loads(sys.stdin.read())
        
        # Set basic environment variables for production
        os.environ.setdefault('SESSION_SECRET', 'ahmed-helly-educational-platform-production-key-2025')
        os.environ.setdefault('DATABASE_URL', '')  # Will use SQLite fallback
        
        # Import Flask app and initialize database
        from main import app
        from app import db
        
        # Create tables and add sample data for production
        with app.app_context():
            db.create_all()
            
            # Initialize with existing users if available
            try:
                from models import User
                admin_user = User.query.filter_by(username='admin').first()
            except:
                # Database may not exist yet, will be created automatically
                pass
        
        # Create test client
        with app.test_client() as client:
            path = event_data.get('path', '/')
            method = event_data.get('method', 'GET')
            headers = event_data.get('headers', {})
            query = event_data.get('query', {})
            body = event_data.get('body', '')
            
            # Build query string
            query_string = '&'.join([f'{k}={v}' for k, v in query.items()]) if query else ''
            
            # Make request to Flask app
            if method == 'GET':
                response = client.get(path, query_string=query_string)
            elif method == 'POST':
                content_type = headers.get('content-type', 'application/x-www-form-urlencoded')
                if 'application/json' in content_type:
                    response = client.post(path, json=json.loads(body) if body else {})
                else:
                    response = client.post(path, data=body, content_type=content_type)
            else:
                response = client.get(path, query_string=query_string)
            
            # Prepare response
            result = {
                'statusCode': response.status_code,
                'headers': dict(response.headers),
                'body': response.get_data(as_text=True)
            }
            
            # Clean headers
            clean_headers = {}
            for key, value in result['headers'].items():
                if key.lower() not in ['content-length', 'transfer-encoding']:
                    clean_headers[key] = str(value)
            
            result['headers'] = clean_headers
            
            print(json.dumps(result, ensure_ascii=False))
            
    except Exception as e:
        # Error response
        error_response = {
            'statusCode': 500,
            'headers': {'Content-Type': 'text/html; charset=utf-8'},
            'body': f'''
            <!DOCTYPE html>
            <html lang="ar" dir="rtl">
            <head>
                <meta charset="UTF-8">
                <title>منصة الأستاذ أحمد حلي</title>
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
                        max-width: 500px;
                        margin: 0 auto;
                        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                    }}
                </style>
            </head>
            <body>
                <div class="error">
                    <h2>منصة الأستاذ أحمد حلي التعليمية</h2>
                    <p>المنصة قيد الإعداد حالياً</p>
                    <p>الرجاء المحاولة خلال دقائق قليلة</p>
                    <button onclick="location.reload()">إعادة المحاولة</button>
                </div>
            </body>
            </html>
            '''
        }
        print(json.dumps(error_response))

if __name__ == '__main__':
    main()