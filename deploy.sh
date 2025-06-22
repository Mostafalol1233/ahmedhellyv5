#!/bin/bash

# Ahmed Helly Educational Platform - Deployment Script
# This script helps prepare the application for deployment

echo "🚀 Preparing Ahmed Helly Educational Platform for deployment..."

# Check if required files exist
echo "📁 Checking deployment files..."

required_files=(
    "main.py"
    "app.py" 
    "requirements.txt"
    "vercel.json"
    "netlify.toml"
    "api/index.py"
    "netlify/functions/app.py"
)

missing_files=()
for file in "${required_files[@]}"; do
    if [[ ! -f "$file" ]]; then
        missing_files+=("$file")
    fi
done

if [[ ${#missing_files[@]} -gt 0 ]]; then
    echo "❌ Missing required files:"
    printf '   %s\n' "${missing_files[@]}"
    exit 1
else
    echo "✅ All deployment files present"
fi

# Check Python syntax
echo "🐍 Checking Python syntax..."
python -m py_compile main.py app.py models.py routes.py 2>/dev/null
if [[ $? -eq 0 ]]; then
    echo "✅ Python syntax check passed"
else
    echo "❌ Python syntax errors found"
    exit 1
fi

# Check if virtual environment variables are set (for production)
echo "🔧 Environment check..."
if [[ -z "$DATABASE_URL" && -z "$VERCEL" && -z "$NETLIFY" ]]; then
    echo "⚠️  DATABASE_URL not set (okay for development)"
else
    echo "✅ Production environment detected"
fi

echo ""
echo "🎉 Deployment preparation complete!"
echo ""
echo "Next steps:"
echo "1. For Vercel: Push to GitHub and connect to Vercel"
echo "2. For Netlify: Push to GitHub and connect to Netlify"
echo "3. Set environment variables in your platform dashboard"
echo "4. Deploy and test!"
echo ""
echo "See DEPLOYMENT_GUIDE.md for detailed instructions."