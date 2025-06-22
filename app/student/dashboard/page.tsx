import { redirect } from 'next/navigation';
import { getCurrentUser } from '@/lib/auth';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { db, videos, tests, testAttempts } from '@/server/storage';
import { eq, count, desc } from 'drizzle-orm';

export default async function StudentDashboard() {
  const user = await getCurrentUser();
  
  if (!user || user.role !== 'student') {
    redirect('/');
  }

  // Get student statistics
  const [videoStats, testStats, attemptStats] = await Promise.all([
    db.select({ count: count() }).from(videos),
    db.select({ count: count() }).from(tests),
    db.select({ count: count() }).from(testAttempts).where(eq(testAttempts.userId, user.id)),
  ]);

  const totalVideos = videoStats[0]?.count || 0;
  const totalTests = testStats[0]?.count || 0;
  const totalAttempts = attemptStats[0]?.count || 0;

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-7xl mx-auto">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">
            لوحة تحكم الطالب
          </h1>
          <p className="text-gray-600">مرحباً {user.fullName || user.username}</p>
          <p className="text-sm text-gray-500">نقاطك الحالية: {user.points}</p>
        </div>

        {/* Statistics Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <Card>
            <CardHeader>
              <CardTitle>الفيديوهات المتاحة</CardTitle>
              <CardDescription>إجمالي عدد الفيديوهات التعليمية</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold text-blue-600">{totalVideos}</div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>الاختبارات المتاحة</CardTitle>
              <CardDescription>إجمالي عدد الاختبارات</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold text-green-600">{totalTests}</div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>محاولاتي</CardTitle>
              <CardDescription>عدد محاولات الاختبارات</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold text-purple-600">{totalAttempts}</div>
            </CardContent>
          </Card>
        </div>

        {/* Quick Actions */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <Card>
            <CardHeader>
              <CardTitle>المكتبة</CardTitle>
              <CardDescription>تصفح جميع الفيديوهات</CardDescription>
            </CardHeader>
            <CardContent>
              <Button className="w-full">تصفح المكتبة</Button>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>الاختبارات</CardTitle>
              <CardDescription>ابدأ اختبار جديد</CardDescription>
            </CardHeader>
            <CardContent>
              <Button className="w-full">ابدأ اختبار</Button>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>ملاحظاتي</CardTitle>
              <CardDescription>ملاحظاتك الشخصية</CardDescription>
            </CardHeader>
            <CardContent>
              <Button className="w-full">عرض الملاحظات</Button>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>الملف الشخصي</CardTitle>
              <CardDescription>إدارة بياناتك</CardDescription>
            </CardHeader>
            <CardContent>
              <Button className="w-full">الملف الشخصي</Button>
            </CardContent>
          </Card>
        </div>

        {/* Logout Button */}
        <div className="mt-8 flex justify-end">
          <form action="/api/auth/logout" method="POST">
            <Button type="submit" variant="outline">
              تسجيل الخروج
            </Button>
          </form>
        </div>
      </div>
    </div>
  );
}