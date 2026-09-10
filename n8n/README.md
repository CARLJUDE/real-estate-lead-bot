# n8n — Workflow Orchestration

n8n handles automation and workflow orchestration for the Real Estate Lead Bot.

## Principle

> **FastAPI manages the application. n8n manages the workflows.**

## Planned workflows

| Workflow ID | Name | Purpose |
|---|---|---|
| PRH-LEAD-PROCESS-MESSAGE | lead-process-message | Main message processing pipeline |
| PRH-LEAD-QUALIFY | lead-qualify | Deterministic lead scoring & classification |
| PRH-LEAD-NOTIFY-SALES | lead-notify-sales | Notify sales on HOT leads |
| PRH-FOLLOWUP-REMINDER | followup-reminder | Due follow-up reminders |
| PRH-SHEET-SYNC-LEAD | sheet-sync-lead | Google Sheets operational sync |
| PRH-ERROR-HANDLER | error-handler | Central error handling |

## Structure

```text
n8n/
├── workflows/
│   ├── lead-process-message.json
│   ├── lead-qualify.json
│   ├── lead-notify-sales.json
│   ├── followup-reminder.json
│   ├── sheet-sync-lead.json
│   └── error-handler.json
└── README.md
```

Workflow JSON files will be added as each workflow is built and exported from n8n.

## Local access

When running via docker-compose:

- n8n UI: http://localhost:5678
