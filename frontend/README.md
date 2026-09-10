# Frontend — React

React application for customer chat interface and sales dashboard.

## Responsibilities

- Customer chat UI
- Sales dashboard (lead list, details, filters, follow-ups)
- Authentication screens
- Loading / error / retry states

React must **not**:
- Connect directly to PostgreSQL
- Calculate official lead scores
- Contain core business rules
- Store sensitive backend credentials

All communication goes through the FastAPI API.

## Recommended structure

```text
frontend/
├── src/
│   ├── components/
│   │   ├── ui/
│   │   ├── chat/
│   │   ├── leads/
│   │   ├── dashboard/
│   │   └── followups/
│   ├── pages/
│   │   ├── customer/
│   │   ├── auth/
│   │   └── dashboard/
│   ├── services/
│   ├── hooks/
│   ├── types/
│   ├── utils/
│   └── app/
├── package.json
└── README.md
```

## Local development (to be initialized)

```bash
cd frontend
npm create vite@latest . -- --template react-ts   # or similar
npm install
npm run dev
```

The frontend scaffolding (Vite + React + TypeScript) will be created in a later step when the customer interface phase begins.
