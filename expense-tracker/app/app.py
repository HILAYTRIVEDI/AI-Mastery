from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import pandas as pd
import os
import datetime
from datetime import datetime as dt

# Configure Flask app
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.secret_key = 'your-secret-key-here'  # Change this in production

# CSV file path
CSV_FILE = os.path.join(os.path.dirname(__file__), '..', 'expenses.csv')

# Initialize CSV file if it doesn't exist
def init_csv():
    # Ensure the directory exists
    os.makedirs(os.path.dirname(CSV_FILE), exist_ok=True)
    
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=['date', 'category', 'description', 'amount'])
        df.to_csv(CSV_FILE, index=False)

# Read expenses from CSV
def read_expenses():
    try:
        df = pd.read_csv(CSV_FILE)
        expenses = df.to_dict('records')
        # Add index to each expense for easier deletion
        for i, expense in enumerate(expenses):
            expense['index'] = i
        return expenses
    except (FileNotFoundError, pd.errors.EmptyDataError):
        return []

# Write expense to CSV
def write_expense(date, category, description, amount):
    try:
        # Read existing data
        try:
            df = pd.read_csv(CSV_FILE)
        except (FileNotFoundError, pd.errors.EmptyDataError):
            df = pd.DataFrame(columns=['date', 'category', 'description', 'amount'])
        
        # Add new expense
        new_expense = {
            'date': date,
            'category': category,
            'description': description,
            'amount': float(amount)
        }
        
        # Create new dataframe with the new expense
        new_df = pd.DataFrame([new_expense])
        df = pd.concat([df, new_df], ignore_index=True)
        
        # Save to CSV
        df.to_csv(CSV_FILE, index=False)
        return True
    except Exception as e:
        print(f"Error writing expense: {e}")
        return False

# Delete expense from CSV
def delete_expense(index):
    try:
        df = pd.read_csv(CSV_FILE)
        if 0 <= index < len(df):
            df = df.drop(df.index[index])
            df.reset_index(drop=True, inplace=True)  # Reset index after deletion
            df.to_csv(CSV_FILE, index=False)
            return True
        return False
    except Exception as e:
        print(f"Error deleting expense: {e}")
        return False

# Calculate statistics
def get_statistics():
    try:
        df = pd.read_csv(CSV_FILE)
        if df.empty:
            return {
                'total': 0,
                'count': 0,
                'average': 0,
                'by_category': {},
                'monthly': {}
            }
        
        # Convert date column to datetime
        df['date'] = pd.to_datetime(df['date'])
        df['month'] = df['date'].dt.strftime('%Y-%m')
        
        stats = {
            'total': round(df['amount'].sum(), 2),
            'count': len(df),
            'average': round(df['amount'].mean(), 2) if len(df) > 0 else 0,
            'by_category': df.groupby('category')['amount'].sum().round(2).to_dict(),
            'monthly': df.groupby('month')['amount'].sum().round(2).to_dict()
        }
        return stats
    except Exception as e:
        print(f"Error calculating statistics: {e}")
        return {
            'total': 0,
            'count': 0,
            'average': 0,
            'by_category': {},
            'monthly': {}
        }

@app.route('/')
def index():
    init_csv()
    expenses = read_expenses()
    stats = get_statistics()
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    return render_template('index.html', expenses=expenses, stats=stats, today=today)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    try:
        date = request.form['date']
        category = request.form['category']
        description = request.form['description']
        amount = request.form['amount']
        
        # Validate inputs
        if not all([date, category, description, amount]):
            flash('All fields are required!', 'error')
            return redirect(url_for('index'))
        
        try:
            amount = float(amount)
            if amount <= 0:
                flash('Amount must be greater than 0!', 'error')
                return redirect(url_for('index'))
        except ValueError:
            flash('Invalid amount format!', 'error')
            return redirect(url_for('index'))
        
        # Validate date
        try:
            dt.strptime(date, '%Y-%m-%d')
        except ValueError:
            flash('Invalid date format!', 'error')
            return redirect(url_for('index'))
        
        if write_expense(date, category, description, amount):
            flash('Expense added successfully!', 'success')
        else:
            flash('Error adding expense!', 'error')
            
    except Exception as e:
        flash(f'Error: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route('/delete_expense/<int:index>')
def delete_expense_route(index):
    if delete_expense(index):
        flash('Expense deleted successfully!', 'success')
    else:
        flash('Error deleting expense!', 'error')
    return redirect(url_for('index'))

@app.route('/api/stats')
def api_stats():
    return jsonify(get_statistics())

@app.route('/api/expenses')
def api_expenses():
    return jsonify(read_expenses())

if __name__ == '__main__':
    init_csv()
    app.run(debug=True, port=5000)