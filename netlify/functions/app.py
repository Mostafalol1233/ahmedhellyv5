import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from main import app as flask_app

def handler(event, context):
    """Main Netlify function handler"""
    
    # Get request details
    path = event.get('path', '/')
    method = event.get('httpMethod', 'GET').upper()
    headers = event.get('headers', {})
    query_params = event.get('queryStringParameters') or {}
    body = event.get('body', '')
    
    # Handle base64 encoded body
    if event.get('isBase64Encoded', False) and body:
        import base64
        body = base64.b64decode(body)
    
    # Create WSGI environ from Netlify event
    environ = {
        'REQUEST_METHOD': method,
        'PATH_INFO': path,
        'QUERY_STRING': '&'.join([f'{k}={v}' for k, v in query_params.items()]),
        'CONTENT_TYPE': headers.get('content-type', ''),
        'CONTENT_LENGTH': str(len(body)) if body else '0',
        'SERVER_NAME': headers.get('host', 'localhost').split(':')[0],
        'SERVER_PORT': '443' if headers.get('x-forwarded-proto') == 'https' else '80',
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': headers.get('x-forwarded-proto', 'http'),
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
    
    # Response data
    response_status = None
    response_headers = []
    
    def start_response(status, headers, exc_info=None):
        nonlocal response_status, response_headers
        response_status = status
        response_headers = headers
    
    # Call Flask app
    try:
        response_body = flask_app(environ, start_response)
        
        # Get response data
        if hasattr(response_body, '__iter__'):
            body_bytes = b''.join(response_body)
        else:
            body_bytes = response_body
            
        # Return Netlify response format
        return {
            'statusCode': int(response_status.split()[0]),
            'headers': dict(response_headers),
            'body': body_bytes.decode('utf-8', errors='replace')
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'text/html; charset=utf-8'},
            'body': f'<h1>خطأ في التطبيق</h1><p>Error: {str(e)}</p>'
        }