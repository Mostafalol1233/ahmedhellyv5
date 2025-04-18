# دليل نشر التطبيق على Vercel

هذا الدليل يشرح خطوات نشر تطبيق Flask على منصة Vercel.

## متطلبات مسبقة

1. حساب على Vercel [https://vercel.com/signup](https://vercel.com/signup)
2. تطبيق Flask جاهز للنشر
3. حساب GitHub (اختياري ولكن مفضل)

## إعداد التطبيق

1. تأكد من وجود الملفات التالية في مشروعك:

   - `main.py` - الملف الرئيسي للتطبيق
   - `vercel.json` - ملف التكوين الخاص بـ Vercel
   - `requirements.txt` - قائمة المكتبات المطلوبة

2. قم بتشغيل سكريبت إعداد Vercel (اختياري):

   ```bash
   python vercel_setup.py
   ```

3. تأكد من أن هيكل المشروع يتبع الشكل التالي:

   ```
   /
   ├── main.py           # نقطة دخول التطبيق
   ├── app.py           # ملف التكوين والإعداد
   ├── routes.py         # مسارات التطبيق
   ├── models.py         # تعريفات قاعدة البيانات
   ├── static/           # الملفات الثابتة
   ├── templates/        # قوالب HTML
   ├── vercel.json       # تكوين Vercel
   ├── requirements.txt  # المكتبات المطلوبة
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

### 2. النشر على Vercel

#### باستخدام واجهة الويب

1. قم بتسجيل الدخول إلى [Vercel](https://vercel.com/)
2. انقر على "New Project"
3. اختر مستودع GitHub الذي رفعت إليه المشروع
4. في صفحة تكوين المشروع:
   - اختر "Other" من قائمة Framework Preset
   - اترك Root Directory كـ `./`
   - اترك Build Command فارغًا (أو `pip install -r requirements.txt` إذا كان مطلوبًا)
   - اترك Output Directory فارغًا
5. انتقل إلى قسم Environment Variables وأضف المتغيرات التالية:
   - `DATABASE_URL`: رابط قاعدة البيانات PostgreSQL
   - `SESSION_SECRET`: مفتاح عشوائي لتأمين جلسات المستخدمين
6. انقر على "Deploy"

#### باستخدام CLI (اختياري)

1. قم بتثبيت Vercel CLI:

   ```bash
   npm i -g vercel
   ```

2. قم بتسجيل الدخول:

   ```bash
   vercel login
   ```

3. انتقل إلى مجلد المشروع ونفذ الأمر:

   ```bash
   vercel
   ```

## بعد النشر

1. قم بزيارة رابط المشروع المنشور للتأكد من عمله بشكل صحيح
2. إذا كنت تستخدم قاعدة بيانات، تأكد من تهيئتها باستخدام سكريبت الهجرة:

   ```python
   # يمكن تنفيذ هذا من لوحة تحكم Vercel Functions
   from db_migrate import run_migrations
   run_migrations()
   ```

3. تواصل مع فريق Vercel إذا واجهت أي مشكلات في النشر

## ملاحظات مهمة

1. تأكد من أن تطبيق Flask يستخدم المتغيرات البيئية للإعدادات الحساسة
2. تجنب الوصول المباشر لنظام الملفات - Vercel يعمل كـ serverless وله قيود على الكتابة
3. استخدم قاعدة بيانات خارجية (مثل PostgreSQL من Supabase أو Railway) بدلاً من SQLite

## المراجع

- [وثائق Vercel Python](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
- [دليل نشر تطبيقات Flask على Vercel](https://vercel.com/guides/deploying-flask-with-vercel)