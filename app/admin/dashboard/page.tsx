import { redirect } from 'next/navigation';
import { getCurrentUser } from '@/lib/auth';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { db, users, videos, tests } from '@/server/storage';
import { eq, count } from 'drizzle-orm';

export default async function AdminDashboard() {
  const user = await getCurrentUser();
  
  if (!user || user.role !== 'admin') {
    redirect('/');
  }

  // Get statistics
  const [userStats, videoStats, testStats] = await Promise.all([
    db.select({ count: count() }).from(users),
    db.select({ count: count() }).from(videos),
    db.select({ count: count() }).from(tests),
  ]);

  const totalUsers = userStats[0]?.count || 0;
  const totalVideos = videoStats[0]?.count || 0;
  const totalTests = testStats[0]?.count || 0;

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-7xl mx-auto">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">
            لوحة تحكم المشرف
          </h1>
          <p className="text-gray-600">مرحباً {user.fullName || user.username}</p>
        </div>

        {/* Statistics Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <Card>
            <CardHeader>
              <CardTitle>المستخدمون</CardTitle>
              <CardDescription>إجمالي عدد المستخدمين المسجلين</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold text-blue-600">{totalUsers}</div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>الفيديوهات</CardTitle>
              <CardDescription>إجمالي عدد الفيديوهات التعليمية</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold text-green-600">{totalVideos}</div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>الاختبارات</CardTitle>
              <CardDescription>إجمالي عدد الاختبارات</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold text-purple-600">{totalTests}</div>
            </CardContent>
          </Card>
        </div>

        {/* Action Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <Card>
            <CardHeader>
              <CardTitle>إدارة المستخدمين</CardTitle>
              <CardDescription>عرض وإدارة المستخدمين المسجلين</CardDescription>
            </CardHeader>
            <CardContent>
              <Button className="w-full">إدارة المستخدمين</Button>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>إدارة الفيديوهات</CardTitle>
              <CardDescription>رفع وإدارة المحتوى التعليمي</CardDescription>
            </CardHeader>
            <CardContent>
              <Button className="w-full">إدارة الفيديوهات</Button>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>إدارة الاختبارات</CardTitle>
              <CardDescription>إنشاء وإدارة الاختبارات</CardDescription>
            </CardHeader>
            <CardContent>
              <Button className="w-full">إدارة الاختبارات</Button>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>الإعلانات</CardTitle>
              <CardDescription>إنشاء وإدارة الإعلانات</CardDescription>
            </CardHeader>
            <CardContent>
              <Button className="w-full">إدارة الإعلانات</Button>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>التقارير</CardTitle>
              <CardDescription>عرض التقارير والإحصائيات</CardDescription>
            </CardHeader>
            <CardContent>
              <Button className="w-full">عرض التقارير</Button>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>الإعدادات</CardTitle>
              <CardDescription>إعدادات النظام العامة</CardDescription>
            </CardHeader>
            <CardContent>
              <Button className="w-full">الإعدادات</Button>
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