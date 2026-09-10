# AI Specification

## PrimeHomes Realty — Real Estate Lead Bot

**Document:** AI Specification  
**Version:** 1.0  
**Status:** Draft  
**AI Role:** Natural Language Understanding, Extraction, Classification, Response Generation  
**Orchestration:** n8n  
**Backend:** FastAPI / Python  

---

# 1. Purpose

This document defines the AI responsibilities, capabilities, constraints, and output contracts for the Real Estate Lead Bot.

AI is used where natural-language understanding and generation are required.

AI is **not** the system of record and must not own authentication, authorization, database integrity, or final business rules.

---

# 2. AI Responsibilities

AI should:

- Identify customer intent
- Extract property requirements
- Extract budget and currency
- Extract location
- Extract bedrooms and property type
- Extract timeline
- Extract contact details when present
- Detect missing information
- Generate clarification questions
- Generate customer-facing responses
- Summarize conversations for sales staff
- Detect when human assistance is required
- Provide confidence information where supported

---

# 3. AI Non-Responsibilities

AI must not:

- Authenticate or authorize users
- Write directly to PostgreSQL
- Decide final database integrity rules
- Assign sales ownership as the final authority
- Invent property availability
- Invent prices
- Confirm bookings without system verification
- Replace deterministic lead scoring
- Silently override business rules

---

# 4. Intent Detection

Supported intents include:

```text
BUY
RENT
SELL
LAND
PROPERTY_ENQUIRY
GENERAL_ENQUIRY
HUMAN_AGENT
OTHER
```

---

# 5. Entity Extraction

AI should extract structured fields such as:

```json
{
  "intent": "BUY",
  "transaction_type": "BUY",
  "property_type": "APARTMENT",
  "bedrooms": 3,
  "location": "Lekki",
  "budget_min": null,
  "budget_max": 80000000,
  "currency": "NGN",
  "timeline": "WITHIN_3_MONTHS",
  "customer_name": null,
  "email": null,
  "phone": null,
  "confidence": 0.96
}
```

Unknown values must be represented as null (or an equivalent explicit unknown value). AI must not invent missing information.

---

# 6. Structured Output Contract

AI responses used by the application should be structured and validated before persistence.

Example:

```json
{
  "intent": "BUY",
  "confidence": 0.94,
  "extracted_data": {
    "property_type": "apartment",
    "bedrooms": 3,
    "location": "Lekki",
    "budget_max": 80000000,
    "currency": "NGN",
    "timeline": "WITHIN_3_MONTHS"
  },
  "missing_fields": ["phone"],
  "suggested_action": "ASK_FOR_PHONE",
  "response": "Great. Could you please provide your phone number so our team can contact you?"
}
```

---

# 7. Confidence & Clarification

Low-confidence extractions should not automatically become authoritative customer data. Prefer clarification questions when confidence is below an application threshold.

---

# 8. Response Generation Rules

Responses should be:

- Professional
- Friendly
- Concise
- Relevant
- Helpful
- Non-deceptive

The AI must not claim a property exists, is available, or is reserved unless verified by the system.

---

# 9. Human Handoff

AI should support escalation when:

- The customer requests a human
- Confidence is low
- The enquiry is complex
- The lead is high-value and needs immediate human attention
- Negotiation begins
- The AI cannot safely answer

---

# 10. Failure Handling

If AI fails:

```text
Retry → Fallback response → Preserve original customer message → Allow human review
```

The original customer message must never be lost.

---

# 11. Implementation Notes

- Prompts should be versioned
- Evaluation datasets should be maintained for regression testing
- Extraction and response generation may use different prompts
- Application validation remains mandatory before database writes

---

# 12. Final Principle

AI understands and generates.

The application validates, stores, scores, and decides.

Keep the boundary clear.

---

*Full original document content is preserved in git history (see commits prior to root cleanup). This file provides the operational AI contract for development.*
