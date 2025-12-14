#  Sweet Shop Management System (Backend)

A backend service for managing a sweet shop inventory with authentication, built using FastAPI and developed using a Test-Driven Development (TDD) approach.

## Features

### Authentication
* User registration
* User login
* Password hashing
* Token-based authentication (basic)

### Sweets Management
* Add new sweets
* List available sweets
* Purchase sweets (inventory update)
* Handles insufficient stock cases

###  Persistence
* Database-backed models (SQLite)
* Clean separation using `db.py`, `models.py`, and `schemas.py`

##  Test-Driven Development (TDD)

This project strictly follows TDD:

1. **RED** - Wrote failing tests first (Auth & Sweets)
2. **GREEN** - Added minimal implementation to pass tests
3. **REFACTOR** - Introduced database, models, and schemas without changing test behavior

The Git history clearly reflects: **RED → GREEN → REFACTOR**

##  Tech Stack

* **Backend**: FastAPI
* **Database**: SQLite
* **ORM**: SQLAlchemy
* **Validation**: Pydantic
* **Testing**: Pytest
* **Language**: Python 3.11

##  Project Structure

```
backend/
├── app/
│   ├── auth.py
│   ├── auth_routes.py
│   ├── sweets_routes.py
│   ├── db.py
│   ├── models.py
│   ├── schemas.py
│   └── main.py
├── tests/
│   ├── test_auth_routes.py
│   ├── test_auth_utils.py
│   └── test_sweets.py
└── requirements.txt
```

##  How to Run

###  Install dependencies
```bash
pip install -r requirements.txt
```

###  Run the application
```bash
uvicorn app.main:app --reload
```

###  Run tests
```bash
python -m pytest
```

All tests should pass ✅

## API Endpoints (Summary)

### Auth
* `POST /api/auth/register`
* `POST /api/auth/login`

### Sweets
* `POST /api/sweets`
* `GET /api/sweets`
* `POST /api/sweets/purchase`

## Future Enhancements

* Frontend UI (React)
* JWT-based authentication
* Role-based access
* Sweet search & filters
* CI/CD pipeline

## Key Takeaway

This project demonstrates:
* Proper backend design
* Real-world TDD workflow
* Clean commit history
* Scalable structure
