export default function SimplePage() {
  return (
    <div style={{ padding: '20px', textAlign: 'center', fontFamily: 'Arial, sans-serif' }}>
      <h1>منصة الأستاذ أحمد حلي التعليمية</h1>
      <p>منصة تعليمية متطورة مبنية بـ Next.js و TypeScript</p>
      <div style={{ marginTop: '20px' }}>
        <h2>الميزات الرئيسية:</h2>
        <ul style={{ textAlign: 'right', margin: '0 auto', display: 'inline-block' }}>
          <li>نظام تسجيل دخول آمن للطلاب والمشرفين</li>
          <li>لوحة تحكم شاملة لإدارة المحتوى</li>
          <li>نظام اختبارات تفاعلي مع تصحيح تلقائي</li>
          <li>إدارة الفيديوهات التعليمية</li>
          <li>قاعدة بيانات PostgreSQL للأداء العالي</li>
        </ul>
      </div>
    </div>
  )
}