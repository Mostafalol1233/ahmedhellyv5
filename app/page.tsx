import React from 'react'

export default function HomePage() {
  return (
    <div style={{ padding: '2rem', maxWidth: '800px', margin: '0 auto' }}>
      <h1 style={{ fontSize: '2.5rem', marginBottom: '1rem', color: '#333' }}>
        منصة أحمد هلّي التعليمية
      </h1>
      <p style={{ fontSize: '1.2rem', marginBottom: '2rem', color: '#666' }}>
        منصة تعليمية متقدمة متعددة اللغات تستخدم الذكاء الاصطناعي لإنشاء تجارب تعلم شخصية وتفاعلية
      </p>
      
      <div style={{ display: 'grid', gap: '1rem', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))' }}>
        <div style={{ padding: '1.5rem', border: '1px solid #ddd', borderRadius: '8px' }}>
          <h2 style={{ fontSize: '1.5rem', marginBottom: '1rem', color: '#333' }}>للطلاب</h2>
          <p style={{ marginBottom: '1rem', color: '#666' }}>
            الوصول إلى المحتوى التعليمي والاختبارات التفاعلية
          </p>
          <a href="/student" style={{ 
            display: 'inline-block', 
            padding: '0.5rem 1rem', 
            backgroundColor: '#007bff', 
            color: 'white', 
            textDecoration: 'none', 
            borderRadius: '4px' 
          }}>
            دخول الطلاب
          </a>
        </div>
        
        <div style={{ padding: '1.5rem', border: '1px solid #ddd', borderRadius: '8px' }}>
          <h2 style={{ fontSize: '1.5rem', marginBottom: '1rem', color: '#333' }}>للإدارة</h2>
          <p style={{ marginBottom: '1rem', color: '#666' }}>
            إدارة المحتوى والطلاب والاختبارات
          </p>
          <a href="/admin" style={{ 
            display: 'inline-block', 
            padding: '0.5rem 1rem', 
            backgroundColor: '#28a745', 
            color: 'white', 
            textDecoration: 'none', 
            borderRadius: '4px' 
          }}>
            دخول الإدارة
          </a>
        </div>
      </div>
      
      <div style={{ marginTop: '3rem', padding: '1.5rem', backgroundColor: '#f8f9fa', borderRadius: '8px' }}>
        <h3 style={{ fontSize: '1.3rem', marginBottom: '1rem', color: '#333' }}>المميزات الرئيسية</h3>
        <ul style={{ listStyle: 'none', padding: 0 }}>
          <li style={{ marginBottom: '0.5rem', color: '#666' }}>✓ واجهات تعلم تكيفية مدعومة بالذكاء الاصطناعي</li>
          <li style={{ marginBottom: '0.5rem', color: '#666' }}>✓ نظام توصيات المحتوى الذكي</li>
          <li style={{ marginBottom: '0.5rem', color: '#666' }}>✓ نظام اختبارات تفاعلي مع تصحيح تلقائي</li>
          <li style={{ marginBottom: '0.5rem', color: '#666' }}>✓ أدوات إدارة المحتوى المرنة</li>
          <li style={{ marginBottom: '0.5rem', color: '#666' }}>✓ نظام إدارة النقاط للمدراء</li>
        </ul>
      </div>
    </div>
  )
}