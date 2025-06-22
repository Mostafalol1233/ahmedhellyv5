# منصة الأستاذ أحمد حلّي التعليمية - المواصفات الكاملة للنسخة الجديدة

## نظرة عامة على المشروع

منصة تعليمية شاملة تهدف إلى تقديم تجربة تعلم متكاملة باللغة العربية مع دعم كامل للتكنولوجيا الحديثة والذكاء الاصطناعي.

## التقنيات المطلوبة

### Backend
- **Framework:** Next.js 14+ مع App Router
- **Language:** TypeScript
- **Database:** PostgreSQL مع Drizzle ORM
- **Authentication:** NextAuth.js مع JWT
- **API:** RESTful APIs مع Route Handlers
- **File Upload:** Next.js built-in file handling
- **Email:** Nodemailer أو Resend
- **SMS:** Twilio أو similar service
- **Payment:** Stripe أو PayPal integration
- **AI Integration:** OpenAI API للمساعد الذكي

### Frontend
- **Framework:** React 18+ مع Next.js
- **Styling:** Tailwind CSS مع shadcn/ui components
- **State Management:** Zustand أو React Context
- **Forms:** React Hook Form مع Zod validation
- **Icons:** Lucide React
- **RTL Support:** كامل للغة العربية
- **Responsive:** تصميم متجاوب لجميع الأجهزة

### DevOps & Deployment
- **Hosting:** Vercel للنشر التلقائي
- **Database:** Supabase أو Railway PostgreSQL
- **CDN:** Cloudinary للملفات
- **Monitoring:** Vercel Analytics
- **Environment:** متغيرات البيئة للإعدادات الحساسة

## الهيكل التنظيمي للمشروع

```
ahmed-helly-platform/
├── app/                          # Next.js App Router
│   ├── (auth)/                   # Auth group routes
│   │   ├── login/                
│   │   │   └── page.tsx
│   │   ├── register/
│   │   │   └── page.tsx
│   │   └── forgot-password/
│   │       └── page.tsx
│   ├── admin/                    # Admin dashboard
│   │   ├── dashboard/
│   │   │   └── page.tsx
│   │   ├── users/
│   │   │   ├── page.tsx
│   │   │   └── [id]/
│   │   │       └── page.tsx
│   │   ├── content/
│   │   │   ├── videos/
│   │   │   │   ├── page.tsx
│   │   │   │   ├── create/
│   │   │   │   │   └── page.tsx
│   │   │   │   └── [id]/
│   │   │   │       ├── page.tsx
│   │   │   │       └── edit/
│   │   │   │           └── page.tsx
│   │   │   └── tests/
│   │   │       ├── page.tsx
│   │   │       ├── create/
│   │   │       │   └── page.tsx
│   │   │       └── [id]/
│   │   │           ├── page.tsx
│   │   │           ├── edit/
│   │   │           │   └── page.tsx
│   │   │           └── results/
│   │   │               └── page.tsx
│   │   ├── points/
│   │   │   ├── transfer/
│   │   │   │   └── page.tsx
│   │   │   └── history/
│   │   │       └── page.tsx
│   │   ├── announcements/
│   │   │   ├── page.tsx
│   │   │   └── create/
│   │   │       └── page.tsx
│   │   └── layout.tsx            # Admin layout wrapper
│   ├── student/                  # Student portal
│   │   ├── dashboard/
│   │   │   └── page.tsx
│   │   ├── videos/
│   │   │   ├── page.tsx
│   │   │   └── [id]/
│   │   │       └── page.tsx
│   │   ├── tests/
│   │   │   ├── page.tsx
│   │   │   ├── [id]/
│   │   │   │   ├── page.tsx
│   │   │   │   ├── take/
│   │   │   │   │   └── page.tsx
│   │   │   │   └── result/
│   │   │   │       └── page.tsx
│   │   │   └── results/
│   │   │       └── page.tsx
│   │   ├── profile/
│   │   │   └── page.tsx
│   │   ├── chat/                 # AI Assistant
│   │   │   └── page.tsx
│   │   └── layout.tsx            # Student layout wrapper
│   ├── api/                      # API Routes
│   │   ├── auth/
│   │   │   ├── login/
│   │   │   │   └── route.ts
│   │   │   ├── register/
│   │   │   │   └── route.ts
│   │   │   └── reset-password/
│   │   │       └── route.ts
│   │   ├── admin/
│   │   │   ├── users/
│   │   │   │   ├── route.ts
│   │   │   │   └── [id]/
│   │   │   │       └── route.ts
│   │   │   ├── videos/
│   │   │   │   ├── route.ts
│   │   │   │   └── [id]/
│   │   │   │       └── route.ts
│   │   │   ├── tests/
│   │   │   │   ├── route.ts
│   │   │   │   └── [id]/
│   │   │   │       └── route.ts
│   │   │   └── points/
│   │   │       └── transfer/
│   │   │           └── route.ts
│   │   ├── student/
│   │   │   ├── videos/
│   │   │   │   └── route.ts
│   │   │   ├── tests/
│   │   │   │   ├── route.ts
│   │   │   │   └── [id]/
│   │   │   │       ├── submit/
│   │   │   │       │   └── route.ts
│   │   │   │       └── route.ts
│   │   │   └── profile/
│   │   │       └── route.ts
│   │   ├── upload/
│   │   │   └── route.ts
│   │   ├── payment/
│   │   │   ├── create-intent/
│   │   │   │   └── route.ts
│   │   │   └── webhook/
│   │   │       └── route.ts
│   │   ├── sms/
│   │   │   └── send/
│   │   │       └── route.ts
│   │   └── ai/
│   │       └── chat/
│   │           └── route.ts
│   ├── globals.css               # Global styles
│   ├── layout.tsx                # Root layout
│   └── page.tsx                  # Homepage
├── components/                   # Reusable components
│   ├── ui/                       # shadcn/ui components
│   │   ├── button.tsx
│   │   ├── input.tsx
│   │   ├── card.tsx
│   │   ├── dialog.tsx
│   │   ├── table.tsx
│   │   ├── tabs.tsx
│   │   ├── badge.tsx
│   │   ├── alert.tsx
│   │   └── ...
│   ├── layout/                   # Layout components
│   │   ├── header.tsx
│   │   ├── footer.tsx
│   │   ├── sidebar.tsx
│   │   └── nav.tsx
│   ├── forms/                    # Form components
│   │   ├── login-form.tsx
│   │   ├── register-form.tsx
│   │   ├── video-upload-form.tsx
│   │   ├── test-creation-form.tsx
│   │   └── profile-form.tsx
│   ├── dashboard/                # Dashboard components
│   │   ├── stats-card.tsx
│   │   ├── recent-activity.tsx
│   │   ├── user-table.tsx
│   │   └── charts.tsx
│   ├── video/                    # Video components
│   │   ├── video-player.tsx
│   │   ├── video-card.tsx
│   │   ├── video-list.tsx
│   │   └── video-upload.tsx
│   ├── test/                     # Test components
│   │   ├── test-card.tsx
│   │   ├── question-form.tsx
│   │   ├── test-taking.tsx
│   │   ├── test-results.tsx
│   │   └── answer-review.tsx
│   ├── chat/                     # AI Chat components
│   │   ├── chat-interface.tsx
│   │   ├── message.tsx
│   │   └── typing-indicator.tsx
│   └── common/                   # Common components
│       ├── loading.tsx
│       ├── error-boundary.tsx
│       ├── pagination.tsx
│       ├── search.tsx
│       └── filters.tsx
├── lib/                          # Utilities and configs
│   ├── auth.ts                   # Authentication logic
│   ├── db.ts                     # Database connection
│   ├── utils.ts                  # Helper functions
│   ├── validations.ts            # Zod schemas
│   ├── constants.ts              # App constants
│   ├── email.ts                  # Email service
│   ├── sms.ts                    # SMS service
│   ├── payment.ts                # Payment processing
│   ├── ai.ts                     # AI integration
│   └── upload.ts                 # File upload handling
├── server/                       # Server-side logic
│   ├── auth.ts                   # Auth server actions
│   ├── users.ts                  # User operations
│   ├── videos.ts                 # Video operations
│   ├── tests.ts                  # Test operations
│   ├── points.ts                 # Points system
│   └── analytics.ts              # Analytics
├── drizzle/                      # Database schema
│   ├── schema.ts                 # Database models
│   ├── migrations/               # DB migrations
│   └── seed.ts                   # Sample data
├── types/                        # TypeScript types
│   ├── auth.ts
│   ├── user.ts
│   ├── video.ts
│   ├── test.ts
│   └── index.ts
├── hooks/                        # Custom React hooks
│   ├── use-auth.ts
│   ├── use-videos.ts
│   ├── use-tests.ts
│   └── use-points.ts
├── middleware.ts                 # Next.js middleware
├── next.config.js               # Next.js config
├── tailwind.config.js           # Tailwind config
├── drizzle.config.ts            # Drizzle config
└── package.json                 # Dependencies
```

## قاعدة البيانات - المخطط الكامل

### جدول المستخدمين (users)
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  full_name VARCHAR(100) NOT NULL,
  phone VARCHAR(20),
  password_hash VARCHAR(255) NOT NULL,
  role VARCHAR(20) NOT NULL DEFAULT 'student', -- 'admin' | 'student'
  points INTEGER DEFAULT 0,
  avatar_url TEXT,
  email_verified BOOLEAN DEFAULT false,
  phone_verified BOOLEAN DEFAULT false,
  reset_token VARCHAR(100),
  reset_token_expiry TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### جدول الفيديوهات (videos)
```sql
CREATE TABLE videos (
  id SERIAL PRIMARY KEY,
  title VARCHAR(200) NOT NULL,
  description TEXT,
  url TEXT, -- YouTube/Vimeo URL
  file_path TEXT, -- Local file path
  thumbnail_url TEXT,
  duration INTEGER, -- في الثواني
  section VARCHAR(50) DEFAULT 'sec1', -- 'sec1' | 'sec2' | 'sec3' | 'sec4'
  lesson_number INTEGER DEFAULT 1,
  requires_code BOOLEAN DEFAULT true,
  access_code VARCHAR(20),
  points_cost INTEGER DEFAULT 0,
  view_count INTEGER DEFAULT 0,
  is_featured BOOLEAN DEFAULT false,
  is_published BOOLEAN DEFAULT true,
  upload_progress INTEGER DEFAULT 100,
  uploader_id INTEGER REFERENCES users(id),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### جدول مشاهدات الفيديو (video_views)
```sql
CREATE TABLE video_views (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  video_id INTEGER REFERENCES videos(id),
  watch_time INTEGER DEFAULT 0, -- بالثواني
  completed BOOLEAN DEFAULT false,
  viewed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(user_id, video_id)
);
```

### جدول الإعجابات (video_likes)
```sql
CREATE TABLE video_likes (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  video_id INTEGER REFERENCES videos(id),
  liked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(user_id, video_id)
);
```

### جدول الاختبارات (tests)
```sql
CREATE TABLE tests (
  id SERIAL PRIMARY KEY,
  title VARCHAR(200) NOT NULL,
  description TEXT,
  instructions TEXT,
  time_limit INTEGER, -- بالدقائق
  max_attempts INTEGER DEFAULT 1,
  passing_score DECIMAL(5,2) DEFAULT 60.00, -- من 100
  points_reward INTEGER DEFAULT 0,
  requires_code BOOLEAN DEFAULT false,
  access_code VARCHAR(20),
  is_published BOOLEAN DEFAULT true,
  randomize_questions BOOLEAN DEFAULT false,
  show_results_immediately BOOLEAN DEFAULT true,
  creator_id INTEGER REFERENCES users(id),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### جدول أسئلة الاختبار (test_questions)
```sql
CREATE TABLE test_questions (
  id SERIAL PRIMARY KEY,
  test_id INTEGER REFERENCES tests(id) ON DELETE CASCADE,
  question_text TEXT NOT NULL,
  question_type VARCHAR(20) NOT NULL, -- 'multiple_choice' | 'true_false' | 'short_answer'
  points DECIMAL(5,2) DEFAULT 1.00,
  correct_answer TEXT, -- للأسئلة القصيرة
  question_order INTEGER NOT NULL,
  image_url TEXT,
  explanation TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### جدول خيارات الأسئلة (question_choices)
```sql
CREATE TABLE question_choices (
  id SERIAL PRIMARY KEY,
  question_id INTEGER REFERENCES test_questions(id) ON DELETE CASCADE,
  choice_text TEXT NOT NULL,
  is_correct BOOLEAN DEFAULT false,
  choice_order INTEGER NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### جدول محاولات الاختبار (test_attempts)
```sql
CREATE TABLE test_attempts (
  id SERIAL PRIMARY KEY,
  test_id INTEGER REFERENCES tests(id),
  user_id INTEGER REFERENCES users(id),
  score DECIMAL(5,2) DEFAULT 0.00,
  total_points DECIMAL(5,2) DEFAULT 0.00,
  time_taken INTEGER, -- بالثواني
  passed BOOLEAN DEFAULT false,
  started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  completed_at TIMESTAMP,
  attempt_number INTEGER DEFAULT 1
);
```

### جدول إجابات الطلاب (test_answers)
```sql
CREATE TABLE test_answers (
  id SERIAL PRIMARY KEY,
  attempt_id INTEGER REFERENCES test_attempts(id) ON DELETE CASCADE,
  question_id INTEGER REFERENCES test_questions(id),
  choice_id INTEGER REFERENCES question_choices(id), -- للاختيار المتعدد
  answer_text TEXT, -- للأسئلة القصيرة
  is_correct BOOLEAN DEFAULT false,
  points_earned DECIMAL(5,2) DEFAULT 0.00,
  answered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### جدول طلبات المحاولة الإضافية (test_retry_requests)
```sql
CREATE TABLE test_retry_requests (
  id SERIAL PRIMARY KEY,
  test_id INTEGER REFERENCES tests(id),
  user_id INTEGER REFERENCES users(id),
  reason TEXT NOT NULL,
  status VARCHAR(20) DEFAULT 'pending', -- 'pending' | 'approved' | 'rejected'
  admin_response TEXT,
  admin_id INTEGER REFERENCES users(id),
  request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  response_date TIMESTAMP
);
```

### جدول تحويل النقاط (point_transfers)
```sql
CREATE TABLE point_transfers (
  id SERIAL PRIMARY KEY,
  from_user_id INTEGER REFERENCES users(id),
  to_user_id INTEGER REFERENCES users(id),
  amount INTEGER NOT NULL,
  reason TEXT,
  transfer_type VARCHAR(20) DEFAULT 'manual', -- 'manual' | 'reward' | 'purchase'
  admin_id INTEGER REFERENCES users(id),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### جدول الإعلانات (announcements)
```sql
CREATE TABLE announcements (
  id SERIAL PRIMARY KEY,
  title VARCHAR(200) NOT NULL,
  content TEXT NOT NULL,
  target_role VARCHAR(20) DEFAULT 'all', -- 'all' | 'admin' | 'student'
  is_published BOOLEAN DEFAULT true,
  is_urgent BOOLEAN DEFAULT false,
  expires_at TIMESTAMP,
  author_id INTEGER REFERENCES users(id),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### جدول الرسائل المباشرة (direct_messages)
```sql
CREATE TABLE direct_messages (
  id SERIAL PRIMARY KEY,
  sender_id INTEGER REFERENCES users(id),
  recipient_id INTEGER REFERENCES users(id),
  subject VARCHAR(200),
  content TEXT NOT NULL,
  is_read BOOLEAN DEFAULT false,
  sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  read_at TIMESTAMP
);
```

### جدول ملاحظات الطلاب (student_notes)
```sql
CREATE TABLE student_notes (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  video_id INTEGER REFERENCES videos(id),
  note_text TEXT NOT NULL,
  timestamp_in_video INTEGER, -- الثانية في الفيديو
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### جدول محادثات المساعد الذكي (ai_chat_messages)
```sql
CREATE TABLE ai_chat_messages (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  message TEXT NOT NULL,
  response TEXT NOT NULL,
  message_type VARCHAR(20) DEFAULT 'general', -- 'general' | 'test_help' | 'video_help'
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## واجهات المستخدم المفصلة

### 1. الصفحة الرئيسية
```tsx
// app/page.tsx
- Hero section مع مقدمة عن المنصة
- إحصائيات سريعة (عدد الطلاب، الفيديوهات، الاختبارات)
- آخر الفيديوهات المضافة
- شهادات الطلاب
- زر دخول/تسجيل واضح
- معاينة المميزات
- معلومات التواصل
```

### 2. نظام تسجيل الدخول والحسابات
```tsx
// app/(auth)/login/page.tsx
- نموذج تسجيل دخول بسيط
- خيار "تذكرني"
- رابط نسيان كلمة المرور
- رابط إنشاء حساب جديد
- تسجيل دخول بـ Google (اختياري)

// app/(auth)/register/page.tsx  
- نموذج إنشاء حساب شامل
- التحقق من البيانات في الوقت الفعلي
- رسالة تأكيد البريد الإلكتروني
- شروط الاستخدام

// app/(auth)/forgot-password/page.tsx
- نموذج استعادة كلمة المرور
- إرسال رمز التحقق بالبريد/SMS
- إعادة تعيين كلمة المرور
```

### 3. لوحة تحكم المدير - التفاصيل الكاملة

#### 3.1 الصفحة الرئيسية للمدير
```tsx
// app/admin/dashboard/page.tsx
interface AdminDashboardStats {
  totalStudents: number;
  totalVideos: number; 
  totalTests: number;
  totalPoints: number;
  newStudentsThisWeek: number;
  videoViewsThisMonth: number;
  testsCompletedToday: number;
  averageTestScore: number;
}

المكونات المطلوبة:
- بطاقات الإحصائيات (4 بطاقات رئيسية)
- رسم بياني لنشاط الطلاب (آخر 30 يوم)
- قائمة بآخر 10 طلاب مسجلين
- قائمة بآخر النشاطات (مشاهدات، اختبارات)
- تنبيهات سريعة (طلبات محاولة إضافية، رسائل جديدة)
- روابط سريعة للوظائف الشائعة
```

#### 3.2 إدارة المستخدمين
```tsx
// app/admin/users/page.tsx
المميزات المطلوبة:
- جدول شامل بجميع المستخدمين مع:
  * الصورة الشخصية
  * الاسم الكامل واسم المستخدم
  * البريد الإلكتروني ورقم الهاتف
  * الدور (مدير/طالب)
  * النقاط الحالية
  * تاريخ التسجيل
  * آخر نشاط
  * حالة التفعيل
- بحث متقدم بالاسم/البريد/الهاتف
- فلترة حسب الدور والحالة
- ترتيب حسب أي عمود
- تصدير البيانات (CSV/Excel)
- إجراءات مجمعة (حذف، تعطيل، إضافة نقاط)

// app/admin/users/[id]/page.tsx  
صفحة تفاصيل المستخدم:
- معلومات شخصية كاملة قابلة للتعديل
- تاريخ النشاطات (مشاهدات فيديو، اختبارات)
- سجل النقاط (إضافة، خصم، تحويل)
- الرسائل المباشرة
- إحصائيات مفصلة للأداء
- زر حظر/إلغاء حظر
- زر إعادة تعيين كلمة المرور
```

#### 3.3 إدارة المحتوى - الفيديوهات
```tsx
// app/admin/content/videos/page.tsx
الواجهة الرئيسية للفيديوهات:
- عرض شبكي للفيديوهات مع صور مصغرة
- معلومات سريعة (العنوان، المدة، المشاهدات)
- فلترة حسب القسم ورقم الدرس
- بحث بالعنوان والوصف
- ترتيب حسب التاريخ، المشاهدات، النقاط
- زر رفع فيديو جديد
- إجراءات سريعة (تعديل، حذف، نشر/إخفاء)

// app/admin/content/videos/create/page.tsx
نموذج رفع فيديو جديد:
- العنوان والوصف (باللغة العربية)
- رفع ملف الفيديو أو رابط YouTube/Vimeo
- اختيار القسم (القسم الأول، الثاني، الثالث، الرابع)
- رقم الدرس (ترقيم تلقائي مع إمكانية التعديل)
- صورة مصغرة مخصصة
- هل يتطلب كود دخول؟
- كود الدخول (إذا مطلوب)
- سعر المشاهدة بالنقاط
- وصف تفصيلي
- علامات تصنيف
- زر معاينة قبل النشر
- جدولة النشر (اختياري)

// app/admin/content/videos/[id]/page.tsx
عرض تفاصيل الفيديو:
- مشغل فيديو مدمج
- جميع معلومات الفيديو
- إحصائيات المشاهدة المفصلة
- تعليقات الطلاب
- تقييمات الطلاب
- سجل التعديلات

// app/admin/content/videos/[id]/edit/page.tsx
تعديل الفيديو:
- نفس نموذج الإنشاء مع البيانات المملوءة
- خيار استبدال الفيديو
- سجل التغييرات
```

#### 3.4 إدارة الاختبارات
```tsx
// app/admin/content/tests/page.tsx
الواجهة الرئيسية للاختبارات:
- قائمة جميع الاختبارات مع معلومات سريعة
- إحصائيات لكل اختبار (عدد المحاولات، متوسط الدرجات)
- فلترة حسب التاريخ والحالة
- بحث بالعنوان
- زر إنشاء اختبار جديد
- إجراءات سريعة (تعديل، حذف، نشر/إخفاء، عرض النتائج)

// app/admin/content/tests/create/page.tsx
إنشاء اختبار جديد - نموذج متعدد الخطوات:

الخطوة 1: معلومات الاختبار الأساسية
- عنوان الاختبار
- وصف مختصر
- تعليمات للطلاب
- الحد الزمني (بالدقائق)
- عدد المحاولات المسموحة
- الدرجة المطلوبة للنجاح
- مكافأة النقاط عند النجاح
- هل يتطلب كود دخول؟
- كود الدخول (إذا مطلوب)
- خلط الأسئلة؟
- إظهار النتائج فوراً؟

الخطوة 2: إضافة الأسئلة
يمكن إضافة الأسئلة بثلاث طرق:

أ) إضافة يدوية:
- نوع السؤال (اختيار متعدد، صح/خطأ، إجابة قصيرة)
- نص السؤال
- النقاط المخصصة
- إضافة صورة (اختياري)
- شرح الإجابة (اختياري)
- للاختيار المتعدد: إضافة الخيارات وتحديد الصحيح
- للصح/خطأ: تحديد الإجابة الصحيحة
- للإجابة القصيرة: الإجابة النموذجية

ب) استيراد من ملف:
- رفع ملف PDF أو Word
- استخراج الأسئلة تلقائياً بالذكاء الاصطناعي
- مراجعة وتعديل الأسئلة المستخرجة
- تأكيد الإجابات الصحيحة

ج) نسخ من اختبار موجود:
- اختيار اختبار موجود
- نسخ جميع الأسئلة
- إمكانية التعديل والحذف

الخطوة 3: المراجعة والنشر
- معاينة الاختبار كاملاً
- فحص الأخطاء
- جدولة النشر
- إرسال إشعارات للطلاب

// app/admin/content/tests/[id]/results/page.tsx
نتائج الاختبار المفصلة:
- إحصائيات عامة (عدد المحاولات، متوسط الدرجات، معدل النجاح)
- رسوم بيانية للأداء
- قائمة بجميع المحاولات مع تفاصيل كل طالب
- تحليل الأسئلة (أصعب الأسئلة، أكثر الأخطاء)
- تصدير النتائج
- إمكانية إعادة تصحيح الإجابات القصيرة
```

#### 3.5 إدارة النقاط والمحفظة
```tsx
// app/admin/points/transfer/page.tsx
تحويل النقاط:
- بحث عن المستخدم المستهدف
- تحديد نوع العملية (إضافة، خصم، تحويل)
- كمية النقاط
- سبب التحويل
- إشعار الطالب
- تأكيد العملية

// app/admin/points/history/page.tsx
سجل عمليات النقاط:
- جميع عمليات النقاط مع التفاصيل
- فلترة حسب النوع والفترة الزمنية
- بحث بالمستخدم
- إحصائيات النقاط المضافة والمخصومة
- تصدير التقارير
```

#### 3.6 إدارة الإعلانات
```tsx
// app/admin/announcements/page.tsx
قائمة الإعلانات:
- جميع الإعلانات مع معاينة سريعة
- حالة النشر والانتهاء
- فلترة حسب الفئة المستهدفة
- إحصائيات المشاهدة

// app/admin/announcements/create/page.tsx
إنشاء إعلان جديد:
- عنوان الإعلان
- المحتوى (محرر نص غني)
- الفئة المستهدفة (الجميع، الطلاب، المدراء)
- مستوى الأهمية (عادي، عاجل)
- تاريخ انتهاء الصلاحية
- إرسال إشعار فوري
- جدولة النشر
```

### 4. بوابة الطلاب - التفاصيل الكاملة

#### 4.1 لوحة تحكم الطالب
```tsx
// app/student/dashboard/page.tsx
المكونات المطلوبة:
- ترحيب شخصي بالطالب
- رصيد النقاط الحالي
- التقدم في المشاهدة (نسبة مئوية)
- آخر الفيديوهات المشاهدة (للمتابعة)
- الاختبارات المتاحة
- النتائج الأخيرة
- الإعلانات الجديدة
- إحصائيات سريعة (ساعات مشاهدة، اختبارات مكتملة)
- روابط سريعة للوظائف الشائعة
- المساعد الذكي (نافذة دردشة صغيرة)
```

#### 4.2 مكتبة الفيديوهات
```tsx
// app/student/videos/page.tsx
استعراض الفيديوهات:
- تصنيف حسب الأقسام (القسم الأول، الثاني، الثالث، الرابع)
- عرض شبكي مع صور مصغرة جذابة
- معلومات كل فيديو (العنوان، المدة، النقاط المطلوبة)
- حالة المشاهدة (لم يُشاهد، جاري، مكتمل)
- فلترة حسب الحالة والقسم
- بحث بالعنوان
- ترتيب حسب الأحدث، الأقدم، الأطول
- نظام تقييم الفيديوهات (نجوم)

// app/student/videos/[id]/page.tsx
صفحة مشاهدة الفيديو:
- مشغل فيديو متقدم مع:
  * تحكم في السرعة
  * إمكانية التقديم السريع
  * الترجمات (إذا متوفرة)
  * وضع ملء الشاشة
  * تذكر آخر موقع توقف
- معلومات الفيديو (العنوان، الوصف، المدة)
- شريط التقدم مع النقاط المهمة
- منطقة الملاحظات (يمكن إضافة ملاحظة في أي ثانية)
- قسم التعليقات
- تقييم الفيديو
- فيديوهات ذات صلة
- زر تحميل المرفقات (إن وجدت)
```

#### 4.3 مركز الاختبارات
```tsx
// app/student/tests/page.tsx
استعراض الاختبارات:
- قائمة الاختبارات المتاحة مع معلومات شاملة
- حالة كل اختبار (متاح، مكتمل، منتهي الوقت)
- نتائج المحاولات السابقة
- عدد المحاولات المتبقية
- الوقت المطلوب والنقاط المكافأة
- فلترة حسب الحالة والنتيجة
- بحث بالعنوان

// app/student/tests/[id]/page.tsx
معاينة الاختبار:
- معلومات الاختبار الكاملة
- التعليمات المفصلة
- عدد الأسئلة والوقت المطلوب
- محاولاتك السابقة ونتائجها
- متطلبات النجاح
- زر بدء الاختبار
- طلب محاولة إضافية (إذا انتهت المحاولات)

// app/student/tests/[id]/take/page.tsx
واجهة أداء الاختبار:
- مؤقت عد تنازلي واضح
- شريط تقدم الأسئلة
- عرض سؤال واحد في كل مرة أو جميع الأسئلة
- أزرار التنقل (السابق، التالي)
- حفظ تلقائي للإجابات
- تحذير عند محاولة الخروج
- ملخص الإجابات قبل التسليم
- زر التسليم النهائي مع تأكيد

// app/student/tests/[id]/result/page.tsx
عرض نتيجة الاختبار:
- النتيجة الإجمالية بصريا جذاب
- تفصيل النقاط لكل سؤال
- الإجابات الصحيحة والخاطئة
- شرح الإجابات (إذا متوفر)
- مقارنة بمتوسط الطلاب
- توصيات للتحسين
- زر إعادة المحاولة (إذا متاح)
- زر طباعة الشهادة (إذا نجح)

// app/student/tests/results/page.tsx
سجل جميع نتائج الاختبارات:
- قائمة شاملة بجميع الاختبارات المكتملة
- النتائج والتواريخ
- رسوم بيانية للأداء عبر الوقت
- إحصائيات شاملة
- تصدير النتائج
- شهادات الإنجاز
```

#### 4.4 الملف الشخصي
```tsx
// app/student/profile/page.tsx
إدارة الملف الشخصي:
- تعديل المعلومات الشخصية
- تغيير الصورة الشخصية
- تغيير كلمة المرور
- ربط رقم الهاتف والبريد الإلكتروني
- إعدادات الإشعارات
- إحصائيات شاملة للأداء
- سجل النشاطات
- إعدادات الخصوصية
```

#### 4.5 المساعد الذكي
```tsx
// app/student/chat/page.tsx
واجهة المحادثة مع المساعد الذكي:
- واجهة دردشة حديثة ومريحة
- قوالب أسئلة سريعة
- إمكانية رفع صور للأسئلة
- سجل المحادثات السابقة
- اقتراحات ذكية للأسئلة
- ربط بالمحتوى (فيديوهات، اختبارات)
- وضع المساعدة في الواجبات
- إرشادات دراسية مخصصة
```

## المميزات التقنية المتقدمة

### 1. نظام الإشعارات الشامل
```tsx
// المميزات المطلوبة:
- إشعارات فورية في المتصفح
- إشعارات بريد إلكتروني
- إشعارات SMS (للأمور المهمة)
- إشعارات داخل التطبيق
- تخصيص أنواع الإشعارات لكل مستخدم
```

### 2. نظام البحث المتقدم
```tsx
// مميزات البحث:
- بحث فوري أثناء الكتابة
- بحث في العناوين والأوصاف
- فلترة متقدمة متعددة المعايير
- حفظ عمليات البحث المفضلة
- اقتراحات بحث ذكية
- بحث صوتي (اختياري)
```

### 3. نظام التقارير والتحليلات
```tsx
// للمدراء:
- تقارير مفصلة عن أداء الطلاب
- إحصائيات استخدام المنصة
- تحليل الفيديوهات الأكثر مشاهدة
- تقارير الاختبارات والنتائج
- رسوم بيانية تفاعلية
- تصدير التقارير بصيغ متعددة

// للطلاب:
- تقرير التقدم الشخصي
- مقارنة الأداء مع الآخرين
- توصيات التحسين
- إحصائيات وقت الدراسة
```

### 4. نظام النسخ الاحتياطي والأمان
```tsx
// الأمان:
- تشفير البيانات الحساسة
- مصادقة ثنائية اختيارية
- حماية من CSRF وXSS
- تسجيل العمليات الحساسة
- إدارة الجلسات المتقدمة

// النسخ الاحتياطي:
- نسخ احتياطي تلقائي يومي
- نسخ احتياطي للملفات والقاعدة
- استرداد البيانات
- مراقبة صحة النظام
```

### 5. التكامل مع الخدمات الخارجية
```tsx
// المدفوعات:
- Stripe للمدفوعات الإلكترونية
- PayPal كبديل
- إدارة الاشتراكات الشهرية
- نظام كوبونات الخصم

// الإشعارات:
- Twilio للرسائل النصية
- SendGrid أو Resend للإيميل
- Firebase للإشعارات الفورية

// التخزين:
- Cloudinary للصور والفيديوهات
- AWS S3 كبديل
- CDN لتسريع التحميل

// المراقبة:
- Vercel Analytics للأداء
- Sentry لتتبع الأخطاء
- Uptime monitoring
```

## سير العمل للمطور

### 1. إعداد المشروع
```bash
# إنشاء مشروع Next.js جديد
npx create-next-app@latest ahmed-helly-platform --typescript --tailwind --eslint --app

# تثبيت المكتبات المطلوبة
npm install drizzle-orm drizzle-kit postgres
npm install next-auth bcryptjs
npm install @hookform/resolvers react-hook-form zod
npm install @radix-ui/react-* lucide-react
npm install tailwindcss-animate class-variance-authority clsx tailwind-merge
npm install zustand
npm install nodemailer twilio stripe
npm install openai

# أدوات التطوير
npm install -D @types/bcryptjs @types/nodemailer
npm install -D drizzle-kit dotenv
```

### 2. هيكل متغيرات البيئة
```env
# Database
DATABASE_URL="postgresql://username:password@host:port/database"

# NextAuth
NEXTAUTH_URL="http://localhost:3000"
NEXTAUTH_SECRET="your-secret-key"

# External Services
OPENAI_API_KEY="sk-..."
TWILIO_ACCOUNT_SID="AC..."
TWILIO_AUTH_TOKEN="..."
TWILIO_PHONE_NUMBER="+1..."
STRIPE_SECRET_KEY="sk_test_..."
STRIPE_WEBHOOK_SECRET="whsec_..."

# Email
SMTP_HOST="smtp.gmail.com"
SMTP_PORT="587"
SMTP_USER="your-email@gmail.com"
SMTP_PASS="your-app-password"

# File Upload
CLOUDINARY_CLOUD_NAME="your-cloud-name"
CLOUDINARY_API_KEY="your-api-key"
CLOUDINARY_API_SECRET="your-api-secret"

# Security
ENCRYPTION_KEY="your-encryption-key"
JWT_SECRET="your-jwt-secret"
```

### 3. خطوات التطوير المرحلية

#### المرحلة 1: الأساسيات (الأسبوع 1-2)
- إعداد قاعدة البيانات مع Drizzle
- نظام المصادقة مع NextAuth.js
- التصميم الأساسي مع Tailwind CSS
- الصفحات الأساسية (الرئيسية، تسجيل الدخول، التسجيل)

#### المرحلة 2: لوحة تحكم المدير (الأسبوع 3-4)
- واجهة إدارة المستخدمين
- نظام رفع وإدارة الفيديوهات
- إنشاء وإدارة الاختبارات
- نظام النقاط والتحويلات

#### المرحلة 3: بوابة الطلاب (الأسبوع 5-6)
- واجهة مشاهدة الفيديوهات
- نظام أداء الاختبارات
- لوحة تحكم الطالب
- الملف الشخصي والإعدادات

#### المرحلة 4: المميزات المتقدمة (الأسبوع 7-8)
- المساعد الذكي مع OpenAI
- نظام الإشعارات الشامل
- التقارير والتحليلات
- تكامل المدفوعات

#### المرحلة 5: التحسين والنشر (الأسبوع 9-10)
- اختبار الأداء والتحسين
- إصلاح الأخطاء
- إعداد النشر على Vercel
- التوثيق النهائي

## دليل النشر والصيانة

### النشر على Vercel
```bash
# ربط المشروع بـ Vercel
npx vercel

# إعداد متغيرات البيئة في Vercel Dashboard
# النشر التلقائي عند كل commit

# أوامر مفيدة
npx vercel --prod  # نشر الإنتاج
npx vercel logs   # عرض السجلات
```

### المراقبة والصيانة
- مراقبة الأداء يومياً
- فحص السجلات أسبوعياً
- تحديث المكتبات شهرياً
- نسخ احتياطي أسبوعي
- اختبار الأمان ربع سنوي

## الخلاصة

هذا المستند يوفر خارطة طريق شاملة لبناء منصة تعليمية متطورة باستخدام أحدث التقنيات. كل قسم يحتوي على التفاصيل اللازمة للتطوير مع التركيز على تجربة المستخدم والأداء والأمان.

المنصة مصممة لتكون قابلة للتوسع والصيانة مع إمكانية إضافة المزيد من المميزات في المستقبل.