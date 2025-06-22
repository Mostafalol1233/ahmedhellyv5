# Netlify Hybrid Approach - Node.js + Python

## Strategy
Using Node.js as a wrapper to call Python, avoiding Netlify's Python version conflicts.

## Architecture
```
Netlify Function (Node.js) → Python Script → Flask App
```

## Files Structure
```
netlify/functions/
├── app.js                 # Node.js handler (main function)
├── python_handler.py      # Python script for Flask
├── requirements.txt       # Python dependencies
├── package.json           # Node.js config
└── app.py.backup         # Original Python function
```

## How It Works
1. **app.js**: Node.js function receives HTTP requests
2. **python_handler.py**: Spawned as subprocess to handle Flask
3. **Flask App**: Processes requests and returns responses
4. **Response**: JSON data passed back through Node.js

## Advantages
- Avoids Python version conflicts
- Uses Netlify's stable Node.js runtime
- Maintains full Flask functionality
- Cleaner error handling

## Configuration
- Simple netlify.toml without Python specifications
- No version files needed
- Dependencies installed via requirements.txt when Python runs

This approach should work reliably on Netlify's platform.