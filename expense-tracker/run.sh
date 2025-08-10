#!/bin/bash

# Expense Tracker Startup Script

echo "🚀 Starting Expense Tracker..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run setup first."
    exit 1
fi

# Activate virtual environment
echo "📦 Activating virtual environment..."
source venv/bin/activate

# Check if dependencies are installed
if ! python -c "import flask, pandas" 2>/dev/null; then
    echo "📥 Installing dependencies..."
    pip install -r requirements.txt
fi

# Navigate to app directory and run the application
echo "🎯 Starting Flask application..."
cd app && python app.py
