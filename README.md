# منصة الأستاذ أحمد حلي التعليمية
# Ahmed Helly Educational Platform

A comprehensive educational platform built with Flask, featuring video content, interactive tests, messaging, and payment integration.

## Quick Deploy

### One-Click Deploy to Vercel
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/your-username/your-repo)

### Deploy to Netlify
[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/your-username/your-repo)

## Features

- **User Management**: Role-based access (admin/student)
- **Video Content**: Upload and streaming with access control
- **Interactive Tests**: Multiple choice with automatic grading
- **Messaging System**: Direct messaging between users
- **Payment Integration**: Stripe for subscriptions
- **SMS Notifications**: Twilio integration
- **AI Chat**: OpenAI integration for assistance
- **Multilingual**: Arabic and English support

## Quick Setup

1. **Database**: Create a PostgreSQL database (recommend [Neon.tech](https://neon.tech))
2. **Environment Variables**: Set `DATABASE_URL` and `SESSION_SECRET`
3. **Deploy**: Use the buttons above or follow the deployment guide

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export DATABASE_URL="your-database-url"
export SESSION_SECRET="your-secret-key"

# Run the application
python main.py
```

## Environment Variables

### Required
- `DATABASE_URL`: PostgreSQL connection string
- `SESSION_SECRET`: Random secret key for sessions

### Optional (for full features)
- `OPENAI_API_KEY`: For AI chat features
- `STRIPE_SECRET_KEY`: For payment processing
- `STRIPE_PUBLISHABLE_KEY`: For payment forms
- `TWILIO_ACCOUNT_SID`: For SMS notifications
- `TWILIO_AUTH_TOKEN`: For SMS authentication
- `TWILIO_PHONE_NUMBER`: Your Twilio phone number

## Documentation

- [Deployment Guide](DEPLOYMENT_GUIDE.md) - Detailed deployment instructions
- [Deployment Checklist](deployment-checklist.md) - Pre-deployment checklist
- [Project Architecture](replit.md) - Technical documentation

## Support

For deployment issues, check the deployment logs in your platform dashboard and verify all environment variables are set correctly.

## License

This project is licensed under the MIT License.