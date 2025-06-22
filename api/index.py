import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from main import app

# This is the WSGI handler for Vercel
def handler(request, response):
    return app(request, response)

# Export the Flask app for Vercel
application = app

# For backward compatibility
app = app