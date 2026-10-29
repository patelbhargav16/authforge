# AuthForge — Authentication API

A secure authentication and authorization REST API built with Python and FastAPI.

## Features

- User registration and login
- Secure password hashing using Argon2
- JWT access-token generation and verification
- Protected user profile endpoint
- Duplicate-email validation
- PostgreSQL database integration
- SQLAlchemy ORM and Alembic migrations
- Automated API tests with pytest
- Interactive API documentation with Swagger UI

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Migrations:** Alembic
- **Authentication:** JWT
- **Password Security:** Argon2
- **Testing:** pytest
- **Containerization:** Docker

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API welcome message |
| GET | `/health` | Health check |
| GET | `/api/v1/info` | API information |
| POST | `/api/v1/auth/register` | Register a user |
| POST | `/api/v1/auth/login` | Log in and receive a JWT |
| GET | `/api/v1/auth/me` | Get the authenticated user's profile |

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/patelbhargav16/authforge.git
cd authforge
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root. Set your PostgreSQL connection URL, a strong random JWT secret, the JWT algorithm, and the access-token expiration time.

Never commit `.env` or publish your secret key.

### 5. Start PostgreSQL

Start your configured PostgreSQL database using your local Docker setup or another PostgreSQL instance.

### 6. Apply database migrations

```bash
alembic upgrade head
```

### 7. Start the API

```bash
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` to explore and test the API.

## Run Tests

```bash
python -m pytest tests/test_auth.py -v
```

## Security Notes

- Passwords are stored as hashes, not plain text.
- Protected endpoints require a valid bearer token.
- JWT secrets and database credentials must be configured through environment variables.
- Use HTTPS and appropriate production settings before deploying.

## Author

**Bhargav Patel**  
Python Backend Developer

- GitHub: https://github.com/patelbhargav16
- LinkedIn: https://www.linkedin.com/in/bhargavpatel1608

## Disclaimer

This is a learning and portfolio project. Review configuration, security controls, and deployment practices before using it in production.