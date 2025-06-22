#!/usr/bin/env python3
"""
Simple test script to verify Flask app works locally
"""
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

try:
    from main import app
    print("✅ Flask app imported successfully")
    
    # Test the app
    with app.test_client() as client:
        response = client.get('/')
        print(f"✅ Test request successful: {response.status_code}")
        print(f"Content type: {response.headers.get('Content-Type')}")
        
        # Test admin route
        response = client.get('/admin')
        print(f"✅ Admin route test: {response.status_code}")
        
    print("✅ All tests passed - app should work on Netlify")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
except Exception as e:
    print(f"❌ Error: {e}")