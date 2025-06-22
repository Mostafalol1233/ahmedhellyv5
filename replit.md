# Overview

This is a Flask-based educational platform called "منصة الأستاذ أحمد حلي التعليمية" (Ahmed Helly's Educational Platform) built with Python/Flask. It's a comprehensive learning management system that supports video content, tests, direct messaging, payment integration, and SMS notifications.

# System Architecture

## Backend Architecture
- **Framework**: Flask 3.1.0 with SQLAlchemy ORM
- **Database**: PostgreSQL (primary) with SQLite fallback for development
- **Authentication**: Flask-Login for session management
- **Forms**: Flask-WTF with CSRF protection
- **File Storage**: Local file system for uploads
- **Session Management**: Server-side sessions with configurable secret key

## Frontend Architecture
- **Template Engine**: Jinja2 templates with Arabic RTL support
- **CSS Framework**: Bootstrap 5.3.0 with RTL layout
- **Icons**: Font Awesome 6.0.0
- **Fonts**: Google Fonts (Tajawal) for Arabic typography
- **JavaScript**: Vanilla JS with Bootstrap components

## Database Schema
The application uses a comprehensive relational database with the following key tables:
- **Users**: Stores user accounts with roles (admin/student), points system, and profile data
- **Videos**: Video content with access control, points cost, and view tracking
- **Tests**: Educational assessments with time limits, passing scores, and attempt tracking
- **Messages**: Direct messaging system between users
- **Payments**: Subscription and transaction management (Stripe integration)
- **SMS**: Message logging for Twilio integration

# Key Components

## User Management
- Role-based access control (admin/student)
- Profile management with email/phone verification
- Password reset functionality with secure tokens
- Points-based wallet system for content access

## Content Management
- Video upload and streaming with YouTube integration
- Test creation with multiple choice questions and image support
- Announcement system for platform-wide notifications
- File upload support for PDF and Word documents

## Assessment System
- Comprehensive test management with question banks
- Multiple attempt tracking with retry request system
- Automatic grading with configurable passing scores
- Time-limited test sessions

## Communication
- Direct messaging between users
- AI chat integration (OpenAI API)
- SMS notifications via Twilio
- Real-time message status tracking

## Payment Integration
- Stripe payment processing for subscriptions
- Transaction logging and webhook handling
- Subscription management with expiration tracking

# Data Flow

## User Authentication Flow
1. User submits login credentials
2. Flask-Login validates against database
3. Session created with user context
4. Role-based navigation and permissions applied

## Content Access Flow
1. User requests video/test content
2. System checks access permissions and points balance
3. Content served or payment/code required
4. View/attempt logged for analytics

## Payment Processing Flow
1. User selects subscription plan
2. Stripe checkout session created
3. Payment processed via Stripe webhook
4. User permissions updated in database
5. Confirmation sent via SMS/email

# External Dependencies

## Required Services
- **PostgreSQL Database**: Primary data storage (Neon.tech configured)
- **Stripe**: Payment processing (requires API keys)
- **Twilio**: SMS notifications (requires account SID and auth token)
- **OpenAI**: AI chat functionality (optional)

## Python Dependencies
- Flask ecosystem (Flask, SQLAlchemy, Login, WTF)
- Database drivers (psycopg2-binary, pymysql)
- External APIs (stripe, twilio, openai)
- File processing (pypdf, python-docx, reportlab)
- Production server (gunicorn)

# Deployment Strategy

## Supported Platforms
- **Vercel**: Primary deployment target with serverless functions
- **Netlify**: Alternative deployment with Netlify Functions
- **Railway/Render**: Container-based deployment options
- **Replit**: Development and prototyping environment

## Environment Configuration
- Database URL configured for PostgreSQL connection
- API keys managed via environment variables
- Session secrets for security
- File upload paths and limits configured

## Database Migration
- Automated schema creation on first run
- Migration scripts for schema updates
- Data seeding for default users and content

# Changelog
- June 22, 2025: Initial setup
- June 22, 2025: Complete deployment configuration for Vercel and Netlify
  - Added proper WSGI handlers for both platforms
  - Fixed environment variable handling for production
  - Created deployment guides and checklists
  - Optimized for serverless deployment constraints
  - Updated to 2025 deployment standards (fixed functions/builds conflict)
  - Fixed Netlify Python version configuration (3.11 format)
  - Fixed Vercel runtime versioning (@vercel/python@4.0.0)
  - Fixed Netlify function handler with proper Flask integration
  - Enhanced SEO with meta tags, structured data, and sitemap
  - Improved video organization with lesson numbers and sections
  - Added developer credit footer with Mustafa Bemo link
  - Successfully deployed and live on Netlify with working function handler
  - Fixed Vercel pip3.9 error with explicit Python 3.11 configuration
  - Created streamlined vercel_requirements.txt for optimal Vercel deployment
  - Focused on Netlify deployment with simplified WSGI integration
  - Enhanced Arabic UI with proper loading page and redirect system
  - Created ultra-simplified Netlify handler with minimal dependencies
  - Separate requirements-netlify.txt for streamlined deployment

# User Preferences

Preferred communication style: Simple, everyday language.