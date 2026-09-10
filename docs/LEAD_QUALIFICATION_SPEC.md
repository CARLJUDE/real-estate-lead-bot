# LEAD_QUALIFICATION_SPEC.md

# Real Estate Lead Bot — Lead Qualification & Scoring

## 1. Purpose

This document defines how the Real Estate Lead Bot should qualify incoming real estate leads.

The objective is simple:

> Determine how ready and valuable a customer appears to be so the sales team knows which leads deserve the most immediate attention.

The qualification system should be:

- Simple.
- Understandable.
- Consistent.
- Easy to modify.
- Easy to explain to the sales team.

The system should not attempt to predict customer behavior perfectly.

---

# 2. Qualification Flow

The basic process is:

```text
Customer Message
      ↓
Extract Information
      ↓
Check Available Information
      ↓
Qualification Rules
      ↓
Calculate Score
      ↓
Classify Lead
      ↓
Take Action
```

Example:

```text
Score: 87
Classification: HOT
Action: Notify Sales Team
```

---

# 3. Lead Classification

The system uses four main classifications.

| Score | Classification |
|---:|---|
| 80–100 | HOT |
| 60–79 | WARM |
| 30–59 | COLD |
| 0–29 | UNQUALIFIED |

These thresholds can be adjusted later based on real business results.

---

# 4. What Makes a Good Lead?

The system should consider a few simple factors.

### 1. Clear Intent

Does the customer clearly want to:

- Buy?
- Rent?
- Sell?
- Acquire land?

A clear intent is stronger than a general enquiry.

---

### 2. Property Requirement

Does the customer know what they want?

For example:

```text
3-bedroom apartment
```

is more useful than:

```text
I need a property.
```

---

### 3. Location

A specific location provides more useful information.

Example:

```text
Lekki Phase 1
```

is more actionable than:

```text
Somewhere in Lagos.
```

---

### 4. Budget

A stated budget is an important qualification signal.

Example:

```text
My budget is ₦80 million.
```

is more actionable than:

```text
I don't know my budget yet.
```

---

### 5. Timeline

Customers who intend to make a decision soon should generally receive more attention.

Examples:

```text
I want to buy this month.
```

```text
I'm planning to buy within three months.
```

```text
I'm just researching for now.
```

---

### 6. Contact Information

A lead with usable contact information is easier for the sales team to follow up.

Useful information includes:

- Name.
- Phone number.
- Email.

---

# 5. Initial Scoring Model

The MVP can use a simple point-based system.

## Intent — Maximum 20 Points

| Condition | Points |
|---|---:|
| Clear BUY / RENT / SELL / LAND intent | 20 |
| Property enquiry / investment interest | 12 |
| General enquiry | 5 |
| Unclear / no intent | 0 |

## Property Requirement — Maximum 15 Points

| Condition | Points |
|---|---:|
| Specific property type + bedrooms | 15 |
| Property type only | 10 |
| Vague requirement | 5 |
| No requirement stated | 0 |

## Location — Maximum 15 Points

| Condition | Points |
|---|---:|
| Specific area / neighbourhood | 15 |
| Broad city / region | 8 |
| Unclear location | 3 |
| No location | 0 |

## Budget — Maximum 20 Points

| Condition | Points |
|---|---:|
| Clear budget range | 20 |
| Approximate budget | 12 |
| Budget mentioned vaguely | 6 |
| No budget | 0 |

## Timeline — Maximum 20 Points

| Condition | Points |
|---|---:|
| Immediate / within 1 month | 20 |
| Within 3 months | 15 |
| Within 6 months | 10 |
| Researching / longer | 5 |
| No timeline | 0 |

## Contact Information — Maximum 10 Points

| Condition | Points |
|---|---:|
| Name + phone or email | 10 |
| Phone or email only | 6 |
| Name only | 3 |
| No contact details | 0 |

---

# 6. Score Calculation

```text
TOTAL = Intent + Property Requirement + Location + Budget + Timeline + Contact
```

Maximum total: **100**

---

# 7. Classification Rules

```text
80–100 → HOT
60–79  → WARM
30–59  → COLD
0–29   → UNQUALIFIED
```

---

# 8. Recommended Actions by Classification

### HOT

- Notify sales team immediately.
- Prioritize follow-up.
- Assign to an agent if assignment is enabled.

### WARM

- Keep in active pipeline.
- Continue qualification questions if needed.
- Follow up within a reasonable time.

### COLD

- Continue light nurturing.
- Ask for missing information.
- Do not discard.

### UNQUALIFIED

- Request essential missing information.
- Do not push aggressive sales contact.
- Re-evaluate when more data arrives.

---

# 9. Progressive Qualification

A lead does not need a complete score on the first message.

Example:

```text
Customer: "I want a house in Lekki."
Score may be low.
Bot asks for budget and timeline.
Customer provides more details.
Score is recalculated.
```

The system should recalculate when new useful information is received.

---

# 10. Missing Information Handling

If important fields are missing, the bot should ask useful questions rather than forcing a final classification too early.

Priority questions often include:

1. Budget
2. Timeline
3. Contact details
4. Property type / bedrooms
5. Location refinement

Ask only what is useful.

---

# 11. AI vs Deterministic Scoring

```text
AI
 ↓
Extract structured information
 ↓
Application validation
 ↓
Deterministic scoring rules
 ↓
Score + Classification
```

AI should not invent the final business score.

The scoring rules should remain explicit and testable.

---

# 12. Score History

Each meaningful recalculation should be stored.

Useful history fields:

- Previous score
- New score
- Classification
- Reason / contributing factors
- Timestamp

---

# 13. Example Scores

### Example 1 — HOT

```text
Intent: BUY (20)
Property: 3-bedroom apartment (15)
Location: Lekki (15)
Budget: ₦80m (20)
Timeline: Within 1 month (20)
Contact: phone provided (10)
Total: 100 → HOT
```

### Example 2 — WARM

```text
Intent: BUY (20)
Property: apartment (10)
Location: Ikeja (15)
Budget: unknown (0)
Timeline: within 3 months (15)
Contact: name only (3)
Total: 63 → WARM
```

### Example 3 — COLD

```text
Intent: general enquiry (5)
Property: house (10)
Location: Lagos (8)
Budget: unknown (0)
Timeline: researching (5)
Contact: none (0)
Total: 28 → borderline UNQUALIFIED / COLD depending on exact rules
```

---

# 14. Recalculation Triggers

Recalculate when:

- New budget is provided
- Timeline changes
- Location becomes more specific
- Property requirements become clearer
- Contact details are added
- Intent becomes clearer

---

# 15. Human Override

Sales staff should be able to override classification when needed.

The system should record:

- Who changed it
- Why it was changed
- When it was changed

---

# 16. What Qualification Must Not Do

- Invent missing customer data
- Assume budget
- Assume location
- Permanently discard low-scoring leads
- Rely solely on AI judgment for the final score
- Confuse extraction confidence with business value

---

# 17. Testing Scenarios

The qualification logic should be tested with:

- Complete HOT leads
- Incomplete first messages
- Progressive multi-message qualification
- Missing budget
- Missing contact details
- Research-only customers
- Human-agent requests
- Score boundary cases (29/30, 59/60, 79/80)

---

# 18. Implementation Location

Recommended ownership:

- Extraction → AI layer
- Validation → FastAPI / application layer
- Scoring → dedicated qualification service or deterministic workflow step
- Storage → PostgreSQL

Do not duplicate scoring rules across React, FastAPI, and n8n.

---

# 19. Output Contract Example

```json
{
  "score": 87,
  "classification": "HOT",
  "breakdown": {
    "intent": 20,
    "property_requirement": 15,
    "location": 15,
    "budget": 20,
    "timeline": 15,
    "contact": 2
  },
  "missing_fields": ["phone", "email"],
  "recommended_action": "NOTIFY_SALES"
}
```

---

# 20. Clarification Preference

When information is ambiguous, prefer asking the customer to clarify rather than guessing.

Example:

```text
Just to confirm, is your budget around ₦50 million?
```

---

# 21. Important Qualification Rules

### Rule 1
Never invent missing customer information.

### Rule 2
Never assume budget.

### Rule 3
Never assume location.

### Rule 4
Never assume buying or renting.

### Rule 5
Do not permanently classify a customer based on the first message.

### Rule 6
Recalculate when important information changes.

### Rule 7
Keep the scoring rules understandable.

### Rule 8
A low score should not prevent future qualification.

### Rule 9
AI extraction and lead scoring are separate processes.

### Rule 10
Sales staff should be able to understand why a lead received its classification.

---

# 22. Future Improvements

The MVP should use the simple scoring system above.

Later, the system may consider additional signals such as:

- Previous conversations.
- Response frequency.
- Property viewing requests.
- Sales agent interactions.
- Customer engagement.
- Follow-up responses.
- Appointment scheduling.
- Historical conversion data.
- Property availability.
- Lead source.

These should only be introduced when there is enough real-world data to justify them.

---

# 23. Qualification Example Flow

```text
Customer
"I want to buy a house in Lekki."
        ↓
Extract
        ↓
BUY + HOUSE + LEKKI
        ↓
Score
        ↓
45
        ↓
COLD
        ↓
Ask for budget + timeline
        ↓
Customer
"My budget is ₦100m and I want to buy this month."
        ↓
Extract new information
        ↓
Recalculate
        ↓
85
        ↓
HOT
        ↓
Notify Sales
```

---

# 24. Definition of Done

The qualification system is complete when:

- A lead can receive a score from 0–100.
- The score follows documented rules.
- Leads are classified as HOT, WARM, COLD, or UNQUALIFIED.
- Scores can be recalculated.
- Score history can be stored.
- Missing information can trigger further questions.
- AI extraction is separated from scoring.
- Sales staff can understand the reason for a score.
- Low-scoring leads are not automatically discarded.
- Tests cover common qualification scenarios.

---

# 25. Final Principle

The qualification system should answer one simple question:

> **"How much attention should the sales team give this lead right now?"**

It should not pretend to know exactly whether a customer will eventually buy.

Start with simple, explainable rules.

Use real customer data to improve the system later.
