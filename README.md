# Expense Tracker API 💰

A modern backend REST API for tracking personal expenses, built with FastAPI and Python.

## Features

- **FastAPI Framework**: High-performance API with interactive Swagger documentation (`/docs`)
- **Pydantic Validation**: Strict data validation schemas for requests and responses (`AddExpense`, `AddCategory`, `ExpensesListResponse`)
- **Automatic ID Generation**: Dynamic ID calculation (`get_next_id`) for new expenses
- **Category Management**: Built-in validation and dynamic creation of custom expense categories
- **Search & Filtering**: Retrieve expenses with custom limits and search queries
- **Data Persistence**: JSON-based state management (`expenses.json`, `categories.json`)

## Technologies

- Python
- FastAPI
- Pydantic
- Uvicorn
- JSON

## How to run

1. Clone the repository:
   ```bash
   git clone [https://github.com/alyyevsuleymanwork-boop/expense-tracker.git](https://github.com/alyyevsuleymanwork-boop/expense-tracker.git)
   ```

Navigate to the project folder:
```bash
cd expense-tracker
```

Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
```bash
pip install fastapi uvicorn pydantic
```

Run the application:
```bash
uvicorn main:app --reload
```

Open your browser and go to http://127.0.0.1:8000/docs to test the API.

Project status
In active development