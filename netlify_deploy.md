# Netlify Deployment Guide - Fixed 2025

## Files Updated for Deployment

### 1. `netlify.toml` - Main Configuration
- Updated to use main `requirements.txt`
- Added Python 3.11 runtime specification
- Configured functions directory properly

### 2. `netlify/functions/app.py` - Serverless Function
- Improved error handling for import failures
- Better WSGI environment setup
- Proper JSON and form data handling
- Enhanced debugging output

### 3. `runtime.txt` - Python Version
- Set to `python-3.11` (correct format for Netlify)

### 4. `netlify/_headers` - Security Headers
- Added security headers for production
- Configured caching for static files

## Environment Variables Required

Set these in Netlify dashboard under Site Settings > Environment Variables:

### Required:
- `DATABASE_URL` - PostgreSQL connection string
- `SESSION_SECRET` - Random string for Flask sessions

### Optional (based on your features):
- `OPENAI_API_KEY` - For AI features
- `STRIPE_SECRET_KEY` & `STRIPE_PUBLISHABLE_KEY` - For payments
- `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER` - For SMS

## Deployment Steps

1. **Connect Repository**
   - Go to Netlify dashboard
   - Click "New site from Git"
   - Connect your GitHub repository

2. **Build Settings** (Auto-detected from netlify.toml)
   - Build command: `pip install -r requirements.txt`
   - Publish directory: `static`
   - Functions directory: `netlify/functions`

3. **Environment Variables**
   - Add all required environment variables
   - Test with minimal setup first (just DATABASE_URL and SESSION_SECRET)

4. **Deploy**
   - Click "Deploy site"
   - Monitor build logs for any issues

## Database Setup

For production database, recommend:
- **Neon.tech** (free PostgreSQL)
- **Supabase** (free PostgreSQL with extras)
- **Railway** (simple PostgreSQL hosting)

## Testing After Deployment

1. Check main page loads
2. Test user registration/login
3. Verify database connectivity
4. Test static file serving
5. Check admin functionality

## Troubleshooting

### Common Issues:
- **Build fails**: Check Python version in logs
- **Function timeout**: Database connection issues
- **Static files 404**: Verify file paths in templates
- **Database errors**: Check DATABASE_URL format

### Build Logs:
Monitor Netlify build logs for specific error messages and adjust accordingly.

## Next Steps After Successful Deployment

1. Test all functionality
2. Set up custom domain (if needed)
3. Configure SSL (automatic with Netlify)
4. Set up form handling (if using Netlify forms)
5. Configure redirects for SEO

Your Flask app should now be properly configured for Netlify deployment with all necessary fixes applied.