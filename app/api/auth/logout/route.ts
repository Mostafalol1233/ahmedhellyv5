import { NextResponse } from 'next/server';

export async function POST() {
  const response = NextResponse.json({ message: 'تم تسجيل الخروج بنجاح' });
  
  // Clear session cookie
  response.cookies.set('session-user-id', '', {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'strict',
    maxAge: 0,
  });
  
  return response;
}