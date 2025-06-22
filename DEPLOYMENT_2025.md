# Deployment Guide 2025

## Updated Configuration Files

### Vercel Configuration (vercel.json)
- **Fixed**: Using proper versioned runtime @vercel/python@4.0.0
- **Updated**: Back to builds configuration with correct versioning
- **Runtime**: @vercel/python@4.0.0 (stable versioned runtime)
- **Fixed**: Runtime versioning issue for 2025 compliance

### Netlify Configuration (netlify.toml)
- **Fixed**: Removed deprecated `python_version` syntax
- **Updated**: Using 2025 `[functions."app"]` configuration
- **Runtime**: Python 3.11
- **Includes**: All necessary files for deployment

## Deployment Steps

### For Vercel:
1. Connect your GitHub repository
2. Set environment variables in Vercel dashboard:
   - `DATABASE_URL` (PostgreSQL connection string)
   - `SESSION_SECRET` (random string for sessions)
   - `STRIPE_SECRET_KEY` (if using payments)
   - `TWILIO_ACCOUNT_SID` (if using SMS)
   - `TWILIO_AUTH_TOKEN` (if using SMS)
   - `OPENAI_API_KEY` (if using AI features)
3. Deploy using the updated `vercel.json`

### For Netlify:
1. Connect your GitHub repository
2. Set environment variables in Netlify dashboard (same as Vercel)
3. Deploy using the updated `netlify.toml`

## Key Changes for 2025:
- Removed deprecated `builds` property from Vercel
- Updated Netlify functions syntax
- Proper Python 3.11 runtime specification
- Optimized memory allocation
- Included all required files for serverless deployment

## File Structure:
```
/
├── api/
│   └── index.py (Vercel handler)
├── netlify/
│   └── functions/
│       └── app.py (Netlify handler)
├── vercel.json (2025 compliant)
├── netlify.toml (2025 compliant)
└── runtime.txt (Python version)
```

Both platforms now support the 2025 deployment standards and should deploy successfully.