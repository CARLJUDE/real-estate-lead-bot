# Backend — FastAPI

FastAPI application layer for the Real Estate Lead Bot.

## Responsibilities

- REST API endpoints
- Request / response validation
- Authentication & authorization
- Business rules & lead state transitions
- Database access (PostgreSQL via SQLAlchemy)
- Communication with n8n webhooks

## Structure

```text
backend/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── v1/
│   │       ├── auth.py
│   │       ├── leads.py
│   │       ├── conversations.py
│   │       ├── messages.py
│   │       ├── followups.py
│   │       └── health.py
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── repositories/
│   ├── core/
│   └── db/
├── tests/
├── alembic/
├── requirements.txt
├── Dockerfile
└── README.md
```

## Local development

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt

# Ensure PostgreSQL is running (e.g. via docker-compose)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API docs: http://localhost:8000/docs
