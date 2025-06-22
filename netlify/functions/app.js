const { exec } = require('child_process');
const path = require('path');

exports.handler = async (event, context) => {
  return new Promise((resolve) => {
    const pythonScript = path.join(__dirname, 'python_handler.py');
    
    const eventData = JSON.stringify({
      path: event.path || '/',
      method: event.httpMethod || 'GET',
      headers: event.headers || {},
      query: event.queryStringParameters || {},
      body: event.body || '',
      isBase64: event.isBase64Encoded || false
    });
    
    const command = `echo '${eventData}' | python3 "${pythonScript}"`;
    
    exec(command, { 
      timeout: 30000,
      cwd: __dirname,
      env: { ...process.env, PYTHONPATH: path.join(__dirname, '..', '..') }
    }, (error, stdout, stderr) => {
      if (error) {
        resolve({
          statusCode: 500,
          headers: { 'Content-Type': 'text/html; charset=utf-8' },
          body: `
            <!DOCTYPE html>
            <html lang="ar" dir="rtl">
            <head>
              <meta charset="UTF-8">
              <title>منصة الأستاذ أحمد حلي</title>
              <style>
                body { font-family: Arial, sans-serif; text-align: center; padding: 50px; background: #f4f4f4; }
                .error { background: white; padding: 30px; border-radius: 10px; max-width: 500px; margin: 0 auto; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
              </style>
            </head>
            <body>
              <div class="error">
                <h2>منصة الأستاذ أحمد حلي التعليمية</h2>
                <p>المنصة قيد الإعداد حالياً</p>
                <p>الرجاء المحاولة خلال دقائق قليلة</p>
                <button onclick="location.reload()">إعادة المحاولة</button>
              </div>
            </body>
            </html>
          `
        });
        return;
      }
      
      try {
        const response = JSON.parse(stdout.trim());
        resolve(response);
      } catch (e) {
        resolve({
          statusCode: 200,
          headers: { 'Content-Type': 'text/html; charset=utf-8' },
          body: stdout || `
            <!DOCTYPE html>
            <html lang="ar" dir="rtl">
            <head>
              <meta charset="UTF-8">
              <title>منصة الأستاذ أحمد حلي</title>
              <style>
                body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
                .content { background: white; padding: 30px; border-radius: 10px; max-width: 600px; margin: 0 auto; }
              </style>
            </head>
            <body>
              <div class="content">
                <h1>منصة الأستاذ أحمد حلي التعليمية</h1>
                <p>مرحباً بكم في المنصة التعليمية</p>
                <a href="/login">تسجيل الدخول</a> | <a href="/register">إنشاء حساب</a>
              </div>
            </body>
            </html>
          `
        });
      }
    });
  });
};