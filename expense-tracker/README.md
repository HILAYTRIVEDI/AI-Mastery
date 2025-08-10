# Personal Expense Tracker

A simple Flask-based web application to track personal expenses with data visualization and statistics.

## Quick Start

1. **Navigate to the project directory:**
   ```bash
   cd expense-tracker
   ```

2. **Activate virtual environment and run:**
   ```bash
   source venv/bin/activate
   cd app && python app.py
   ```

3. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000
   ```

4. **Optional - Add sample data:**
   ```bash
   python add_sample_data.py
   ```

## Features

- ✅ Add, view, and delete expenses
- 📊 Interactive charts showing spending by category and monthly trends
- 📈 Real-time statistics (total spent, average expense, etc.)
- 💾 Data stored in CSV format
- 📱 Responsive design for mobile and desktop
- 🎨 Beautiful Bootstrap UI with custom styling

## Installation

1. **Create and activate virtual environment:**
   ```bash
   cd expense-tracker
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application:**
   ```bash
   cd app
   python app.py
   ```

2. **Open your browser and navigate to:**
   ```
   http://localhost:5000
   ```

3. **Start adding expenses:**
   - Fill out the form with date, category, description, and amount
   - View your expenses in the table
   - Check statistics and charts
   - Delete expenses by clicking the trash icon

## File Structure

```
expense-tracker/
├── app/
│   └── app.py              # Main Flask application
├── templates/
│   └── index.html          # HTML template
├── static/
│   └── style.css           # Custom CSS styles
├── venv/                   # Virtual environment
├── expenses.csv            # Data storage (created automatically)
└── requirements.txt        # Python dependencies
```

## Data Storage

Expenses are stored in a CSV file (`expenses.csv`) with the following columns:
- `date`: Date of the expense (YYYY-MM-DD format)
- `category`: Category of the expense
- `description`: Description of the expense
- `amount`: Amount spent (float)

## Categories

Pre-defined expense categories:
- 🍔 Food
- 🚗 Transportation
- 🎬 Entertainment
- 🛍️ Shopping
- 💡 Bills
- 🏥 Healthcare
- 📚 Education
- ✈️ Travel
- 📝 Other

## API Endpoints

The application also provides REST API endpoints:
- `GET /api/expenses` - Get all expenses as JSON
- `GET /api/stats` - Get statistics as JSON

## Technologies Used

- **Backend:** Python Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **UI Framework:** Bootstrap 5
- **Charts:** Chart.js
- **Data Processing:** Pandas
- **Icons:** Font Awesome

## Future Enhancements

- 🔐 User authentication and multi-user support
- 📄 Export data to PDF/Excel
- 🔍 Advanced filtering and search
- 💰 Budget tracking and alerts
- 📊 More detailed analytics
- 🌐 Database integration (SQLite/PostgreSQL)

## License

This project is open source and available under the MIT License.
