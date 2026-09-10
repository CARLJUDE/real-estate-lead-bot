# Database — PostgreSQL

PostgreSQL is the primary source of truth for the Real Estate Lead Bot.

## Core tables (planned)

- `users`
- `roles`
- `leads`
- `conversations`
- `messages`
- `lead_scores`
- `lead_assignments`
- `follow_ups`
- `activities`
- `integration_syncs`

## Migrations

Migrations are managed with **Alembic** from the backend package:

```bash
cd backend
alembic revision --autogenerate -m "initial schema"
alembic upgrade head
```

SQL scripts or seed data can live in this directory for reference.

## Structure

```text
database/
├── seeds/
├── scripts/
└── README.md
```
