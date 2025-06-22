import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from main import app

# Export the Flask app for Vercel
application = app

# This is the handler for Vercel
if __name__ == "__main__":
    app.run()