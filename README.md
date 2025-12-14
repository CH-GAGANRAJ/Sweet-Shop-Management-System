#  Sweet Shop Management System

A full-stack Sweet Shop Management System built with FastAPI (Backend) and React (Frontend), developed using Test-Driven Development (TDD) principles.

##  Project Overview

This application allows users to:
* Register and log in
* View available sweets
* Add new sweets
* Purchase sweets with inventory updates

The backend focuses on clean architecture and TDD, while the frontend is a minimal Single Page Application (SPA) to demonstrate end-to-end functionality.

## Test-Driven Development (TDD)

The backend was developed using a strict **RED → GREEN → REFACTOR** approach:

1. **RED** – Tests written first and pushed while failing
2. **GREEN** – Minimal implementation added to pass tests
3. **REFACTOR** – Database, models, and schemas introduced without changing test behavior

The Git commit history clearly reflects this workflow.

##  Tech Stack

### Backend
* FastAPI
* Python 3.11
* SQLite
* SQLAlchemy
* Pydantic
* Pytest

### Frontend
* React (Vite)
* JavaScript
* Fetch API
* Minimal CSS

##  Project Structure

```
Sweet-Shop-Management-System/
├── backend/
│   ├── app/
│   │   ├── auth.py
│   │   ├── auth_routes.py
│   │   ├── sweets_routes.py
│   │   ├── db.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── main.py
│   ├── tests/
│   │   ├── test_auth_routes.py
│   │   ├── test_auth_utils.py
│   │   └── test_sweets.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── src/
│       ├── App.jsx
│       ├── Login.jsx
│       ├── Sweets.jsx
│       ├── api.js
│       ├── main.jsx
│       └── style.css
├── screenshots/
└── README.md
```

##  How to Run Locally

### 1️ Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend runs at: `http://localhost:8000`

### 2️ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at: `http://localhost:5173`

## 🧪 Running Tests

From the `backend` directory:

```bash
python -m pytest
```

All tests should pass successfully.

## 📡 API Endpoints

### Authentication
* `POST /api/auth/register`
* `POST /api/auth/login`

### Sweets
* `POST /api/sweets`
* `GET /api/sweets`
* `POST /api/sweets/purchase`

##  Screenshots

📁 Screenshots are available in the `project_screenshots/` folder.

Include:
* Login page
* Sweets list page
* Purchase action result
* Test execution output

## 🧾 Test Report

All backend tests executed using `pytest` passed successfully.

Screenshot of test results is included in `project_screenshots/`.

## 🤖 My AI Usage

AI tools such as ChatGPT and Cursor were used to:
* Understand and clarify assignment requirements
* Design backend architecture
* Follow Test-Driven Development correctly
* Generate boilerplate code and improve productivity

All code was written, reviewed, and integrated by me. No external repositories or third-party codebases were copied.
