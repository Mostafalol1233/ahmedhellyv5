import sys
import os
import json

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

try:
    from main import app
    
    def handler(event, context):
        """Netlify Function handler for Flask app"""
        
        # Extract request information from event
        path = event.get('path', '/')
        method = event.get('httpMethod', 'GET')
        headers = event.get('headers', {})
        query_string_parameters = event.get('queryStringParameters') or {}
        body = event.get('body', '')
        is_base64_encoded = event.get('isBase64Encoded', False)
        
        # Decode base64 body if needed
        if is_base64_encoded and body:
            import base64
            body = base64.b64decode(body).decode('utf-8')
        
        # Build query string
        query_string = ''
        if query_string_parameters:
            from urllib.parse import urlencode
            query_string = urlencode(query_string_parameters)
        
        # Use Flask test client to handle the request
        with app.test_client() as client:
            try:
                # Make the request to Flask app
                if method == 'GET':
                    response = client.get(path, query_string=query_string, headers=headers)
                elif method == 'POST':
                    response = client.post(path, data=body, headers=headers, query_string=query_string)
                elif method == 'PUT':
                    response = client.put(path, data=body, headers=headers, query_string=query_string)
                elif method == 'DELETE':
                    response = client.delete(path, headers=headers, query_string=query_string)
                else:
                    response = client.open(path, method=method, data=body, headers=headers, query_string=query_string)
                
                # Convert Flask response to Netlify response format
                response_headers = dict(response.headers)
                
                # Ensure Content-Type is set
                if 'Content-Type' not in response_headers:
                    if path.endswith('.css'):
                        response_headers['Content-Type'] = 'text/css'
                    elif path.endswith('.js'):
                        response_headers['Content-Type'] = 'application/javascript'
                    elif path.endswith('.html'):
                        response_headers['Content-Type'] = 'text/html; charset=utf-8'
                    else:
                        response_headers['Content-Type'] = 'text/html; charset=utf-8'
                
                return {
                    'statusCode': response.status_code,
                    'headers': response_headers,
                    'body': response.get_data(as_text=True)
                }
                
            except Exception as e:
                # Return error response
                return {
                    'statusCode': 500,
                    'headers': {'Content-Type': 'text/html; charset=utf-8'},
                    'body': f'<h1>Application Error</h1><p>Error: {str(e)}</p>'
                }

except ImportError as e:
    # Fallback handler if main app cannot be imported
    def handler(event, context):
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'text/html; charset=utf-8'},
            'body': f'<h1>Import Error</h1><p>Could not import Flask app: {str(e)}</p>'
        }

# Export the handler for Netlify
app = handler