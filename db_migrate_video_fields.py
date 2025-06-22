#!/usr/bin/env python3
"""
Database migration script to add new video organization fields
"""

import os
import sys
import logging
from sqlalchemy import text

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, db

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def add_video_organization_fields():
    """Add new fields to videos table for better organization"""
    try:
        with app.app_context():
            # Check if the new fields already exist
            inspector = db.inspect(db.engine)
            columns = [col['name'] for col in inspector.get_columns('videos')]
            
            new_fields = [
                ('lesson_number', 'INTEGER DEFAULT 1'),
                ('section', 'VARCHAR(50) DEFAULT "sec1"'),
                ('is_featured', 'BOOLEAN DEFAULT FALSE'),
                ('video_order', 'INTEGER DEFAULT 0'),
                ('thumbnail_url', 'VARCHAR(200)'),
                ('duration', 'VARCHAR(20)'),
                ('tags', 'VARCHAR(200)')
            ]
            
            fields_to_add = []
            for field_name, field_type in new_fields:
                if field_name not in columns:
                    fields_to_add.append((field_name, field_type))
            
            if not fields_to_add:
                logger.info("جميع الحقول الجديدة موجودة بالفعل في جدول الفيديوهات")
                return True
            
            # Add missing fields
            for field_name, field_type in fields_to_add:
                try:
                    if 'postgresql' in str(db.engine.url):
                        # PostgreSQL syntax
                        if field_type.startswith('BOOLEAN'):
                            sql = f"ALTER TABLE videos ADD COLUMN {field_name} BOOLEAN DEFAULT FALSE"
                        elif 'DEFAULT' in field_type:
                            parts = field_type.split(' DEFAULT ')
                            sql = f"ALTER TABLE videos ADD COLUMN {field_name} {parts[0]} DEFAULT {parts[1]}"
                        else:
                            sql = f"ALTER TABLE videos ADD COLUMN {field_name} {field_type}"
                    else:
                        # SQLite syntax
                        sql = f"ALTER TABLE videos ADD COLUMN {field_name} {field_type}"
                    
                    db.session.execute(text(sql))
                    logger.info(f"تم إضافة الحقل {field_name} بنجاح")
                except Exception as e:
                    logger.error(f"خطأ في إضافة الحقل {field_name}: {str(e)}")
                    continue
            
            db.session.commit()
            logger.info("تم تحديث جدول الفيديوهات بنجاح")
            return True
            
    except Exception as e:
        logger.error(f"خطأ في تحديث قاعدة البيانات: {str(e)}")
        db.session.rollback()
        return False

def update_existing_videos():
    """Update existing videos with default lesson organization"""
    try:
        with app.app_context():
            from models import Video
            
            videos = Video.query.all()
            
            for i, video in enumerate(videos, 1):
                if not hasattr(video, 'lesson_number') or video.lesson_number is None:
                    video.lesson_number = i
                if not hasattr(video, 'section') or video.section is None:
                    video.section = 'sec1'
                if not hasattr(video, 'video_order') or video.video_order is None:
                    video.video_order = i
                if not hasattr(video, 'is_featured') or video.is_featured is None:
                    video.is_featured = False
                
                # Update title to include lesson number if not already formatted
                if not video.title.lower().startswith(('lesson', 'درس')):
                    video.title = f"Lesson {video.lesson_number}: {video.title}"
            
            db.session.commit()
            logger.info(f"تم تحديث {len(videos)} فيديو بالبيانات الافتراضية")
            return True
            
    except Exception as e:
        logger.error(f"خطأ في تحديث الفيديوهات الموجودة: {str(e)}")
        db.session.rollback()
        return False

if __name__ == "__main__":
    logger.info("بدء تحديث قاعدة البيانات لإضافة حقول تنظيم الفيديوهات...")
    
    if add_video_organization_fields():
        logger.info("تم إضافة الحقول الجديدة بنجاح")
        
        if update_existing_videos():
            logger.info("تم تحديث الفيديوهات الموجودة بنجاح")
            logger.info("اكتمل التحديث بنجاح!")
        else:
            logger.error("فشل في تحديث الفيديوهات الموجودة")
    else:
        logger.error("فشل في إضافة الحقول الجديدة")