# 💰 Money Usage Management App

A lightweight **Money Usage Management App** built with **FastAPI** and **SQLite** to track, record, and manage personal or business transactions efficiently.

---

## 📋 Features

- 📥 Add and store money usage records
- 👤 Track transactions by username
- 🕒 Automatic timestamp logging
- 🗄️ SQLite-based persistent storage
- ⚡ Fast and lightweight REST API

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | FastAPI |
| Database | SQLite |
| Language | Python 3.x |

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<username>/Ganesh.git
   cd Ganesh
   ```

2. Install dependencies:
   ```bash
   pip install fastapi uvicorn sqlite3
   ```

---

## 🚀 Running the App

Start the development server:
```bash
uvicorn main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

---

## 📡 API Endpoints

### GET /
Check database connection status.

**Response:**
```json
"Database connection successful"
```

---

## 🗂️ Database Schema

The `data` table stores transaction records:

| Column       | Type         | Description                        |
|--------------|--------------|------------------------------------|
| `id`         | INTEGER      | Primary key (auto-increment)       |
| `username`   | TEXT         | User who made the transaction      |
| `name`       | TEXT         | Transaction name / category        |
| `value`      | TEXT         | Transaction amount / value         |
| `timestamp`  | DATETIME     | Time of transaction (auto-set)     |

---

## 🔧 Configuration

- Database file: `database.db` (auto-created on first run)
- Modify `main.py` and `database.py` to extend API endpoints and database logic.

---

## 📝 Project Structure

```
Ganesh/
├── main.py          # FastAPI app entry point
├── database.py      # SQLite database connection & schema
├── database.db      # SQLite database file (auto-generated)
└── Readme.md        # Project documentation
```

---

## 📌 Notes

- The app currently handles basic transaction storage. You can extend it with CRUD endpoints, user authentication, and analytics features.
- Ensure proper error handling is added for production use.

---

## 👨‍💻 Author

Built for managing money usage and transaction tracking efficiently.
