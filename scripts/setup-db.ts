import { db, users } from '../server/storage';
import bcrypt from 'bcryptjs';

async function setupDatabase() {
  try {
    console.log('Setting up database...');

    // Check if admin user exists
    const existingUsers = await db.select().from(users).limit(1);
    
    if (existingUsers.length === 0) {
      console.log('Creating default users...');
      
      // Create admin user
      const adminPasswordHash = await bcrypt.hash('admin123', 10);
      await db.insert(users).values({
        username: 'admin',
        fullName: 'المشرف الرئيسي',
        email: 'admin@ahmedhelly.com',
        passwordHash: adminPasswordHash,
        role: 'admin',
        points: 0,
      });

      // Create student user
      const studentPasswordHash = await bcrypt.hash('student123', 10);
      await db.insert(users).values({
        username: 'student',
        fullName: 'طالب تجريبي',
        email: 'student@ahmedhelly.com',
        passwordHash: studentPasswordHash,
        role: 'student',
        points: 100,
      });

      console.log('Default users created successfully!');
      console.log('Admin login: admin / admin123');
      console.log('Student login: student / student123');
    } else {
      console.log('Users already exist in database');
    }

  } catch (error) {
    console.error('Error setting up database:', error);
    process.exit(1);
  }
}

setupDatabase();