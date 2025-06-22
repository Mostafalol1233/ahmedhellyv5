# Ahmed Helly Educational Platform - Deployment Guide

## Quick Deployment Options

### Option 1: Vercel Deployment (Recommended)

1. **Fork/Clone the repository**
2. **Connect to Vercel:**
   - Visit [vercel.com](https://vercel.com)
   - Import your GitHub repository
   - Vercel will auto-detect the configuration

3. **Set Environment Variables in Vercel Dashboard:**
   ```
   DATABASE_URL=postgresql://your-database-url
   SESSION_SECRET=your-random-secret-key
   ```

4. **Optional Services (set if needed):**
   ```
   OPENAI_API_KEY=your-openai-key
   STRIPE_SECRET_KEY=your-stripe-key
   STRIPE_PUBLISHABLE_KEY=your-stripe-public-key
   TWILIO_ACCOUNT_SID=your-twilio-sid
   TWILIO_AUTH_TOKEN=your-twilio-token
   TWILIO_PHONE_NUMBER=your-twilio-number
   ```

5. **Deploy:** Click deploy and your app will be live!

### Option 2: Netlify Deployment

1. **Connect to Netlify:**
   - Visit [netlify.com](https://netlify.com)
   - Connect your GitHub repository

2. **Build Settings:**
   - Build command: `pip install -r requirements.txt`
   - Publish directory: `static`
   - Functions directory: `netlify/functions`

3. **Set the same environment variables as above**

4. **Deploy:** Your app will be live on Netlify!

## Database Setup

### Recommended: Neon.tech (Free PostgreSQL)
1. Visit [neon.tech](https://neon.tech)
2. Create a free account
3. Create a new project
4. Copy the connection string
5. Use it as your `DATABASE_URL`

### After First Deployment:
1. Visit your deployed app URL
2. The database tables will be created automatically
3. Default users will be set up on first run

## Testing Your Deployment

Visit these URLs after deployment:
- `/` - Home page
- `/login` - Login page
- `/register` - Registration page
- `/admin` - Admin dashboard (login required)

## Troubleshooting

### Common Issues:
1. **Database Connection Error:** Check your DATABASE_URL format
2. **Static Files Not Loading:** Verify file paths and deployment settings
3. **Environment Variables:** Ensure they're set correctly in your platform dashboard

### Getting Support:
- Check the deployment logs in your platform dashboard
- Verify all environment variables are set
- Test with minimal configuration first