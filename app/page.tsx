import { redirect } from 'next/navigation'
import { LoginForm } from '@/components/login-form'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'

export default function HomePage() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100 p-4">
      <div className="w-full max-w-md space-y-8">
        <div className="text-center">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">
            منصة الأستاذ أحمد حلي
          </h1>
          <p className="text-gray-600">
            منصة تعليمية متطورة للتعلم التفاعلي
          </p>
        </div>
        
        <Card>
          <CardHeader>
            <CardTitle>تسجيل الدخول</CardTitle>
            <CardDescription>
              أدخل بياناتك للوصول إلى المنصة التعليمية
            </CardDescription>
          </CardHeader>
          <CardContent>
            <LoginForm />
          </CardContent>
        </Card>
        
        <div className="text-center text-sm text-gray-600">
          <p>© 2025 منصة الأستاذ أحمد حلي التعليمية. جميع الحقوق محفوظة.</p>
        </div>
      </div>
    </div>
  )
}