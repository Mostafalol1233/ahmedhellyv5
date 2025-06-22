import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

try:
    from main import app
    import json
    
    # Simple function wrapper for Netlify Functions
    def handler(event, context):
        # Convert AWS Lambda event to Flask-compatible request
        from werkzeug.test import EnvironBuilder
        from io import StringIO
        
        # Extract request data from event
        path = event.get('path', '/')
        method = event.get('httpMethod', 'GET')
        headers = event.get('headers', {})
        query_params = event.get('queryStringParameters') or {}
        body = event.get('body', '')
        
        # Create WSGI environment
        with app.test_request_context(
            path=path,
            method=method,
            headers=headers,
            query_string=query_params,
            data=body
        ):
            try:
                response = app.full_dispatch_request()
                return {
                    'statusCode': response.status_code,
                    'headers': dict(response.headers),
                    'body': response.get_data(as_text=True)
                }
            except Exception as e:
                return {
                    'statusCode': 500,
                    'body': f'Application error: {str(e)}'
                }
    
except ImportError as e:
    # Fallback for import errors
    def handler(event, context):
        return {
            'statusCode': 500,
            'body': f'Import error: {str(e)}'
        }

# Main lambda handler function
def lambda_handler(event, context):
    return handler(event, context)