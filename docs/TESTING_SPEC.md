# TESTING_SPEC.md

# Real Estate Lead Bot — Testing Specification

## 1. Purpose

This document defines how the Real Estate Lead Bot should be tested.

The goal is to make sure that:

- The application works as expected.
- Customer messages are processed correctly.
- Leads are stored correctly.
- AI extraction works reliably.
- Lead qualification works correctly.
- n8n workflows execute correctly.
- Customer responses are generated correctly.
- Existing features are not broken when new features are added.

Testing should remain practical and proportional to the project.

---

# 2. Testing Philosophy

The project should follow:

> **Test the important things first.**

We do not need hundreds of tests before the application can run.

The priority is to test the critical customer journey:

```text
Customer Message
      ↓
FastAPI
      ↓
Lead / Conversation
      ↓
n8n
      ↓
AI
      ↓
Qualification
      ↓
Database
      ↓
Customer Response
      ↓
Sales Notification
```

---

# 3. Main Testing Areas

The project should initially have five testing areas:

```text
1. Backend/API
2. Database
3. AI
4. n8n Workflows
5. Frontend
```

---

# 4. Backend/API Testing

Backend tests should verify that the API behaves correctly.

## Health Check

Test:

```text
GET /api/v1/health
```

Expected:

```text
HTTP 200
```

Example response:

```json
{
  "status": "ok"
}
```

---

# 5. Lead API Tests

Test lead creation.

### Valid request

```json
{
  "name": "John Doe",
  "phone": "08000000000",
  "property_type": "APARTMENT",
  "bedrooms": 3,
  "location": "Lekki",
  "budget_max": 80000000,
  "transaction_type": "BUY"
}
```

Expected:

```text
Lead created successfully.
```

---

## Invalid Request

Test missing or invalid information.

Example:

```json
{
  "name": "",
  "bedrooms": -2
}
```

Expected:

```text
HTTP 400 / 422
```

The API should reject invalid data.

---

# 6. Lead Retrieval

Test:

```text
GET /api/v1/leads
```

Verify:

- Leads are returned.
- Pagination works.
- Filters work.
- Search works.
- Sorting works.

---

# 7. Lead Update

Test:

```text
PATCH /api/v1/leads/{id}
```

Verify that fields can be updated correctly.

Example:

```text
Status:
NEW → QUALIFIED
```

and:

```text
Score:
55 → 82
```

---

# 8. Conversation Testing

Test that conversations can be:

- Created.
- Retrieved.
- Associated with the correct lead.
- Associated with the correct customer/session.

Example:

```text
Lead
  ↓
Conversation
  ↓
Messages
```

The relationship should remain consistent.

---

# 9. Message Testing

Test:

```text
POST /api/v1/messages
```

Verify:

- Customer messages can be stored.
- Bot messages can be stored.
- Message order is preserved.
- Conversation context is maintained.
- Idempotency prevents duplicate processing when required.

---

# 10. Authentication Testing

Test login and protected endpoints.

Verify:

- Valid credentials succeed.
- Invalid credentials fail.
- Protected endpoints reject unauthenticated requests.
- Role-based access works where implemented.

---

# 11. Database Testing

Database tests should verify:

- Models create correctly.
- Relationships work.
- Constraints are enforced.
- Indexes exist where required.
- Timestamps are set.
- UUID generation works.
- Migrations apply cleanly.
- Rollback works when needed.

---

# 12. AI Testing

AI tests should focus on extraction reliability and safety.

### Intent scenarios

- BUY
- RENT
- SELL
- LAND
- GENERAL_ENQUIRY
- HUMAN_AGENT
- Unclear message

### Extraction scenarios

- Complete requirements in one message
- Incomplete requirements
- Multi-turn progressive information
- Ambiguous budget
- Ambiguous location
- Mixed intents

### Failure scenarios

- Invalid AI JSON
- Missing fields in AI output
- Low confidence extraction
- Timeout
- Provider failure

AI must not invent property availability or prices.

---

# 13. Qualification Testing

Test score calculation and classification boundaries.

Examples:

- Score 0 → UNQUALIFIED
- Score 29 → UNQUALIFIED
- Score 30 → COLD
- Score 59 → COLD
- Score 60 → WARM
- Score 79 → WARM
- Score 80 → HOT
- Score 100 → HOT

Also test recalculation when new information arrives.

---

# 14. n8n Workflow Testing

Test the main workflows for:

- Successful path
- Invalid input
- Duplicate event / idempotency
- AI failure handling
- API / database failure handling
- Notification failure handling
- Google Sheets failure handling (must not block core lead storage)

---

# 15. Frontend Testing

Customer interface:

- Send message
- Receive response
- Loading state
- Error state
- Retry

Sales dashboard:

- Lead list
- Lead details
- Conversation history
- Score / classification display
- Status update

---

# 16. End-to-End Testing

At least one complete journey should pass:

```text
Customer sends message
  → System stores message
  → AI extracts information
  → Lead is created/updated
  → Score is calculated
  → Response is returned
  → HOT leads notify sales
```

Also test:

- Incomplete lead journey
- Human handoff journey
- Failed AI journey with graceful fallback

---

# 17. Test Data

Use synthetic data only.

Do not use real customer information in development or automated tests.

---

# 18. Test Environment

Development and testing should use a separate environment from production.

Do not run automated tests against the production database.

---

# 19. Test Naming

Tests should have clear names.

Good:

```text
test_create_lead_with_valid_data
test_reject_invalid_bedroom_count
test_classify_score_80_as_hot
test_extract_buy_intent
test_handle_ai_failure
```

Avoid vague names such as `test_one`, `test_new`, `test_stuff`.

---

# 20. Minimum Test Coverage for MVP

Before calling the MVP stable, verify at minimum:

### Backend
- Health endpoint
- Lead creation
- Lead retrieval
- Lead update
- Message creation
- Validation errors

### AI
- BUY / RENT / LAND
- Missing information
- Human handoff
- Unclear requests

### Qualification
- Correct score calculation
- Classification boundaries
- Score updates

### n8n
- Successful workflow
- AI failure
- Notification failure
- Duplicate message

### Frontend
- Send message
- Display response
- Display error
- View lead
- Update lead

### End-to-End
At least one complete customer journey should pass successfully.

---

# 21. Testing Before Deployment

```text
1. Run backend tests
2. Run AI tests
3. Run qualification tests
4. Test n8n workflow
5. Test frontend
6. Run end-to-end test
7. Review errors
8. Deploy
```

---

# 22. Definition of Done

A feature is considered tested when:

- The normal case works.
- Invalid input is handled.
- Important edge cases are considered.
- Errors do not corrupt data.
- Existing functionality still works.
- Relevant automated tests pass.
- The complete customer flow still works when applicable.

---

# 23. Final Testing Principle

The purpose of testing is not to make the project complicated.

The purpose is to give us confidence that:

```text
Customer
   ↓
Message
   ↓
AI
   ↓
Lead
   ↓
Qualification
   ↓
Database
   ↓
Sales Team
```

works reliably.

Start with the critical paths.

Add more tests when the application grows or real-world problems reveal new cases.
