import sys
import os

# Add the project root to Python path
project_root = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, project_root)

# Import the Flask app
try:
    from main import app
    
    # Vercel handler
    def handler(request):
        return app(request.environ, lambda x, y: None)
    
    # Export for Vercel
    app = app
    
except ImportError as e:
    # Fallback minimal Flask app
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return f'<h1>Import Error</h1><p>Could not import main app: {str(e)}</p>'
    
    @app.route('/<path:path>')
    def catch_all(path):
        return f'<h1>Import Error</h1><p>Could not import main app: {str(e)}</p><p>Path: {path}</p>'