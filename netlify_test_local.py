#!/usr/bin/env python3
"""
Test script to verify Netlify function works locally
"""
import sys
import os
import json

# Add project root to path
sys.path.insert(0, os.path.dirname(__file__))

def test_netlify_function():
    """Test the Netlify function handler locally"""
    
    # Import the handler
    from netlify.functions.app import handler
    
    # Test multiple routes
    test_events = [
        {
            'path': '/login',
            'httpMethod': 'GET',
            'headers': {'host': 'test.netlify.app'},
            'queryStringParameters': None,
            'body': '',
            'isBase64Encoded': False
        },
        {
            'path': '/register',
            'httpMethod': 'GET', 
            'headers': {'host': 'test.netlify.app'},
            'queryStringParameters': None,
            'body': '',
            'isBase64Encoded': False
        }
    ]
    
    # Test context (minimal)
    test_context = {
        'requestId': 'test-request-id',
        'functionName': 'app',
        'functionVersion': '1'
    }
    
    success_count = 0
    total_tests = len(test_events)
    
    for i, test_event in enumerate(test_events, 1):
        try:
            print(f"\n--- Test {i}: {test_event['path']} ---")
            response = handler(test_event, test_context)
            
            print(f"Status Code: {response['statusCode']}")
            print(f"Headers: {list(response['headers'].keys())}")
            print(f"Body length: {len(response['body'])} characters")
            
            if response['statusCode'] in [200, 302]:
                print("✅ Test passed")
                success_count += 1
            else:
                print(f"⚠️  Unexpected status: {response['statusCode']}")
                
        except Exception as e:
            print(f"❌ Test failed: {e}")
    
    return success_count == total_tests

if __name__ == "__main__":
    print("Testing Netlify function locally...")
    success = test_netlify_function()
    
    if success:
        print("\n🎉 Your app is ready for Netlify deployment!")
        print("\nNext steps:")
        print("1. Connect your GitHub repo to Netlify")
        print("2. Set environment variables (DATABASE_URL, SESSION_SECRET)")
        print("3. Deploy!")
    else:
        print("\n❌ Issues found. Check the errors above.")