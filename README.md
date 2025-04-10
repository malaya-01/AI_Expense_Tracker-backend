# 💰 Expense Tracker Backend

This is a **FastAPI**-based backend service for an **Expense Tracker** application, leveraging **SQLAlchemy** for ORM and **PostgreSQL** for database management.

---

## 🚀 Getting Started

Follow the steps below to set up and run the backend server locally:

### 1. Create & Activate Virtual Environment

```bash
# On Linux/macOS
python3 -m venv venv
source venv/bin/activate  
```
``` bash
# On Windows
python -m venv venv
venv\Scripts\activate
```

### 2. Install Dependencies

``` bash
pip install -r requirements.txt
```

### 3. Run the Development Server
```bash
uvicorn main:app --reload
```
## 📘 API Documentation
🔹 Swagger UI
Access the interactive API docs at:
[http://localhost:8000/api/v1](http://localhost:8000/api/v1)

🔹 Using cURL
You can also interact with the API via command-line using curl at:
[http://localhost:8000](http://localhost:8000)

## 🛠️ Development
To start customizing endpoints and business logic, edit the main.py file.
The server supports hot reloading, so changes will reflect immediately during development.

## 🧩 Tech Stack
FastAPI – for building high-performance APIs

SQLAlchemy – for database ORM

PostgreSQL – as the primary database

