from flask import Flask, redirect
import subprocess
import os
import threading

app = Flask(__name__)

def start_nextjs():
    """Start Next.js in the background"""
    os.chdir('/home/runner/workspace')
    env = os.environ.copy()
    env['NODE_ENV'] = 'development'
    
    subprocess.Popen([
        'npx', 'next', 'dev',
        '--port', '3000',
        '--hostname', '0.0.0.0'
    ], env=env)

@app.route('/')
def index():
    return redirect('http://localhost:3000')

@app.route('/<path:path>')
def proxy(path):
    return redirect(f'http://localhost:3000/{path}')

if __name__ == "__main__":
    # Start Next.js in background
    threading.Thread(target=start_nextjs, daemon=True).start()
    
    # Start Flask proxy
    app.run(host="0.0.0.0", port=5000, debug=False)