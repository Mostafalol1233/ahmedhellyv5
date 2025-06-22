import { NextRequest, NextResponse } from 'next/server';
import bcrypt from 'bcryptjs';
import { db, users } from '@/server/storage';
import { eq } from 'drizzle-orm';

export async function POST(request: NextRequest) {
  try {
    const { username, password } = await request.json();

    if (!username || !password) {
      return NextResponse.json(
        { error: 'اسم المستخدم وكلمة المرور مطلوبان' },
        { status: 400 }
      );
    }

    // Find user by username
    const user = await db.select().from(users).where(eq(users.username, username)).limit(1);

    if (user.length === 0) {
      return NextResponse.json(
        { error: 'اسم المستخدم غير موجود' },
        { status: 401 }
      );
    }

    const foundUser = user[0];

    // Check password
    const isPasswordValid = await bcrypt.compare(password, foundUser.passwordHash);

    if (!isPasswordValid) {
      return NextResponse.json(
        { error: 'كلمة المرور غير صحيحة' },
        { status: 401 }
      );
    }

    // Create session data (excluding password hash)
    const userData = {
      id: foundUser.id,
      username: foundUser.username,
      fullName: foundUser.fullName,
      email: foundUser.email,
      role: foundUser.role,
      points: foundUser.points,
    };

    // In a real application, you would create a proper session/JWT token here
    const response = NextResponse.json({
      message: 'تم تسجيل الدخول بنجاح',
      user: userData,
    });

    // Set a simple session cookie (in production, use proper JWT)
    response.cookies.set('session-user-id', foundUser.id.toString(), {
      httpOnly: true,
      secure: process.env.NODE_ENV === 'production',
      sameSite: 'strict',
      maxAge: 60 * 60 * 24 * 7, // 7 days
    });

    return response;
  } catch (error) {
    console.error('Login error:', error);
    return NextResponse.json(
      { error: 'حدث خطأ في الخادم' },
      { status: 500 }
    );
  }
}