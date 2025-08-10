#!/usr/bin/env python3
"""
Test script for the Expense Tracker app
"""

import requests
import json
from datetime import datetime

BASE_URL = "http://127.0.0.1:5000"

def test_app():
    print("🧪 Testing Expense Tracker App")
    print("=" * 40)
    
    # Test 1: Check if app is running
    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            print("✅ App is running successfully")
        else:
            print(f"❌ App returned status code: {response.status_code}")
            return
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to app. Make sure it's running at http://127.0.0.1:5000")
        return
    
    # Test 2: Check API endpoints
    try:
        stats_response = requests.get(f"{BASE_URL}/api/stats")
        expenses_response = requests.get(f"{BASE_URL}/api/expenses")
        
        if stats_response.status_code == 200:
            print("✅ Stats API endpoint working")
            stats = stats_response.json()
            print(f"   📊 Current stats: {stats}")
        else:
            print("❌ Stats API endpoint failed")
            
        if expenses_response.status_code == 200:
            print("✅ Expenses API endpoint working")
            expenses = expenses_response.json()
            print(f"   📝 Current expenses count: {len(expenses)}")
        else:
            print("❌ Expenses API endpoint failed")
            
    except Exception as e:
        print(f"❌ API test failed: {e}")
    
    # Test 3: Test adding an expense (this would require form submission)
    print("\n📝 To test adding expenses:")
    print("   1. Go to http://127.0.0.1:5000")
    print("   2. Fill out the form with:")
    print("      - Date: Today's date")
    print("      - Category: Food")
    print("      - Description: Test expense")
    print("      - Amount: 10.50")
    print("   3. Click 'Add Expense'")
    
    print("\n🎯 Manual tests to perform:")
    print("   ✓ Add a new expense")
    print("   ✓ View the expense in the table")
    print("   ✓ Check that statistics update")
    print("   ✓ Delete an expense")
    print("   ✓ Verify charts display (if you have expenses)")
    
    print("\n✨ App should be fully functional!")

if __name__ == "__main__":
    test_app()
