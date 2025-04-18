# دليل نشر التطبيق على Netlify

هذا الدليل يشرح خطوات نشر تطبيق Flask على منصة Netlify باستخدام Netlify Functions.

## متطلبات مسبقة

1. حساب على Netlify [https://app.netlify.com/signup](https://app.netlify.com/signup)
2. تطبيق Flask جاهز للنشر
3. حساب GitHub (اختياري ولكن مفضل)

## إعداد التطبيق

1. تأكد من وجود الملفات التالية في مشروعك:

   - `main.py` - الملف الرئيسي للتطبيق
   - `netlify.toml` - ملف التكوين الخاص بـ Netlify
   - `netlify/functions/app.py` - ملف وظيفة Netlify للتطبيق
   - `requirements.txt` - قائمة المكتبات المطلوبة

2. تأكد من أن هيكل المشروع يتبع الشكل التالي:

   ```
   /
   ├── main.py                    # نقطة دخول التطبيق
   ├── app.py                     # ملف التكوين والإعداد
   ├── routes.py                  # مسارات التطبيق
   ├── models.py                  # تعريفات قاعدة البيانات
   ├── static/                    # الملفات الثابتة
   ├── templates/                 # قوالب HTML
   ├── netlify.toml               # تكوين Netlify
   ├── netlify/
   │   └── functions/
   │       └── app.py             # وظيفة Netlify
   ├── requirements.txt           # المكتبات المطلوبة
   └── ...
   ```

## خطوات النشر

### 1. رفع المشروع على GitHub (طريقة مفضلة)

1. قم بإنشاء مستودع جديد على GitHub
2. قم برفع مشروعك إليه:

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/username/project-name.git
   git push -u origin main
   ```

### 2. النشر على Netlify

#### باستخدام واجهة الويب

1. قم بتسجيل الدخول إلى [Netlify](https://app.netlify.com/)
2. انقر على "New site from Git"
3. اختر مستودع GitHub الذي رفعت إليه المشروع
4. في صفحة تكوين النشر:
   - اترك فرع النشر كـ `main`
   - اترك Command دومًا كـ `pip install -r requirements.txt`
   - اترك Publish directory فارغة
5. انقر على "Advanced build settings" وأضف المتغيرات البيئية التالية:
   - `DATABASE_URL`: رابط قاعدة البيانات PostgreSQL
   - `SESSION_SECRET`: مفتاح عشوائي لتأمين جلسات المستخدمين
6. انقر على "Deploy site"

#### باستخدام CLI (اختياري)

1. قم بتثبيت Netlify CLI:

   ```bash
   npm i -g netlify-cli
   ```

2. قم بتسجيل الدخول:

   ```bash
   netlify login
   ```

3. انتقل إلى مجلد المشروع وقم بربط المستودع:

   ```bash
   netlify init
   ```

4. قم بإعداد المتغيرات البيئية:

   ```bash
   netlify env:set DATABASE_URL "postgresql://..."
   netlify env:set SESSION_SECRET "your-secret-key"
   ```

5. قم بالنشر:

   ```bash
   netlify deploy --prod
   ```

## بعد النشر

1. قم بزيارة رابط المشروع المنشور للتأكد من عمله بشكل صحيح
2. إذا كنت تستخدم قاعدة بيانات، تأكد من تهيئتها:

   ```bash
   # يمكن تنفيذ هذا من بيئة Netlify CI أو Functions
   python -c "from db_migrate import run_migrations; run_migrations()"
   ```

3. لاختبار الوظائف محليًا، استخدم:

   ```bash
   netlify dev
   ```

## تخصيص إعدادات المشروع

### تعديل حجم الوظائف

إذا كنت بحاجة إلى زيادة حجم الوظائف، يمكنك تعديل ملف `netlify.toml`:

```toml
[functions]
  node_bundler = "esbuild"
  included_files = ["**/*.py"]
  external_node_modules = ["express"]
```

### تخصيص التوجيهات

يمكنك تعديل قسم `[[redirects]]` في `netlify.toml` لتخصيص توجيه الطلبات.

## ملاحظات مهمة

1. تأكد من أن تطبيق Flask يستخدم المتغيرات البيئية للإعدادات الحساسة
2. تجنب الوصول المباشر لنظام الملفات لأن الوظائف تعمل في بيئة serverless
3. تتقيد وظائف Netlify بمهلة زمنية قدرها 10 ثوانٍ - لا تنسَ هذه المحدودية

## المراجع

- [وثائق Netlify Functions](https://docs.netlify.com/functions/overview/)
- [مثال Python Flask لـ Netlify](https://github.com/netlify/netlify-lambda-functions-example)