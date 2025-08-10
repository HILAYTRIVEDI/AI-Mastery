#!/usr/bin/env python3
"""
Add sample data to the expense tracker
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from app import write_expense, init_csv
from datetime import datetime, timedelta

def add_sample_data():
    print("📊 Adding sample data to expense tracker...")
    
    # Initialize CSV
    init_csv()
    
    # Sample expenses
    sample_expenses = [
        {
            'date': (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d'),
            'category': 'Food',
            'description': 'Lunch at cafe',
            'amount': 15.50
        },
        {
            'date': (datetime.now() - timedelta(days=4)).strftime('%Y-%m-%d'),
            'category': 'Transportation',
            'description': 'Gas for car',
            'amount': 45.00
        },
        {
            'date': (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d'),
            'category': 'Entertainment',
            'description': 'Movie tickets',
            'amount': 25.00
        },
        {
            'date': (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d'),
            'category': 'Shopping',
            'description': 'Groceries',
            'amount': 78.25
        },
        {
            'date': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'),
            'category': 'Bills',
            'description': 'Electricity bill',
            'amount': 120.00
        },
        {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'category': 'Food',
            'description': 'Coffee',
            'amount': 4.75
        }
    ]
    
    # Add each expense
    for expense in sample_expenses:
        if write_expense(expense['date'], expense['category'], 
                        expense['description'], expense['amount']):
            print(f"✅ Added: {expense['description']} - ${expense['amount']}")
        else:
            print(f"❌ Failed to add: {expense['description']}")
    
    total_amount = sum(expense['amount'] for expense in sample_expenses)
    print(f"\n🎉 Added {len(sample_expenses)} sample expenses")
    print(f"💰 Total sample amount: ${total_amount:.2f}")
    print("🌐 Visit http://127.0.0.1:5000 to see the data!")

if __name__ == "__main__":
    add_sample_data()
