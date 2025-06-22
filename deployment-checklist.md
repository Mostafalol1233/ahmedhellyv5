# Deployment Checklist

## Pre-deployment Steps

### 1. Environment Variables Setup
- [ ] Set `DATABASE_URL` (PostgreSQL connection string)
- [ ] Set `SESSION_SECRET` (random secure string)
- [ ] Set API keys if using external services:
  - [ ] `OPENAI_API_KEY` (for AI chat features)
  - [ ] `STRIPE_SECRET_KEY` & `STRIPE_PUBLISHABLE_KEY` (for payments)
  - [ ] `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER` (for SMS)

### 2. Database Setup
- [ ] Create PostgreSQL database (recommend Neon.tech for free tier)
- [ ] Run database migrations: `python db_migrate.py create`
- [ ] Create default users: `python create_users.py`

### 3. File Structure Check
- [ ] Verify all static files are in `/static/` directory
- [ ] Check that uploaded files directory exists
- [ ] Ensure templates are properly organized

## Vercel Deployment

### Files Required:
- [ ] `vercel.json` - Deployment configuration
- [ ] `api/index.py` - WSGI handler
- [ ] `requirements.txt` - Python dependencies
- [ ] `runtime.txt` - Python version specification

### Steps:
1. Connect GitHub repository to Vercel
2. Set environment variables in Vercel dashboard
3. Deploy using Vercel CLI or web interface
4. Test all functionality after deployment

## Netlify Deployment

### Files Required:
- [ ] `netlify.toml` - Build configuration
- [ ] `netlify/functions/app.py` - Lambda handler
- [ ] `requirements.txt` - Python dependencies
- [ ] `runtime.txt` - Python version

### Steps:
1. Connect GitHub repository to Netlify
2. Set environment variables in Netlify dashboard
3. Configure build settings in netlify.toml
4. Deploy and test functionality

## Post-deployment Testing

### Essential Tests:
- [ ] User registration and login
- [ ] Database connectivity
- [ ] Static file serving (CSS, JS, images)
- [ ] File uploads functionality
- [ ] External API integrations (if configured)
- [ ] Payment processing (if Stripe is configured)
- [ ] SMS functionality (if Twilio is configured)

### Performance Tests:
- [ ] Page load times
- [ ] Database query performance
- [ ] File upload limits
- [ ] Concurrent user handling

## Common Issues and Solutions

### Database Connection Issues:
- Verify DATABASE_URL format
- Check database server accessibility
- Ensure SSL requirements are met

### Static Files Not Loading:
- Check file paths in templates
- Verify static file routing configuration
- Test file permissions

### Environment Variables:
- Double-check variable names (case-sensitive)
- Verify values don't contain extra spaces
- Test with minimal configuration first

### Memory/Timeout Issues:
- Optimize database queries
- Reduce file upload sizes
- Check function timeout limits