# Product Requirements Document (PRD)

## PrimeHomes Realty — Real Estate Lead Bot

**Document Version:** 1.0  
**Status:** Draft  
**Product:** Real Estate Lead Bot  
**Client:** PrimeHomes Realty  
**Primary Automation Platform:** n8n  
**Frontend:** React  
**Backend:** Python / FastAPI  
**Database:** SQL  
**Operational Integration:** Google Sheets via n8n  
**AI Layer:** LLM-based natural language processing  

---

# 1. Product Overview

## 1.1 Product Name

**PrimeHomes Realty Lead Bot**

The PrimeHomes Realty Lead Bot is an automated lead intake, qualification, response, and follow-up system designed for a real estate company that receives potential customer enquiries through digital channels.

The system will act as a digital receptionist for PrimeHomes Realty.

It will receive customer messages, understand their requirements, extract structured information, store the lead, determine lead quality and urgency, respond to the customer, notify the appropriate sales personnel, and track the lead through the sales process.

---

# 2. Problem Statement

PrimeHomes Realty may receive a large number of enquiries from potential customers through channels such as websites, chat interfaces, messaging platforms, and other communication channels.

Customer messages are often unstructured.

For example:

> "Hi, I'm looking for a 3-bedroom apartment around Lekki. My budget is around ₦80 million."

Another customer may say:

> "Do you have any 2-bedroom apartments in Ikeja?"

Another may simply say:

> "Hello, I want to buy a house."

Manually processing these enquiries requires sales staff to read each message and determine:

- Customer name
- Phone number
- Email
- Property type
- Number of bedrooms
- Location
- Budget
- Buying or renting
- Customer intent
- Timeline
- Lead quality
- Follow-up requirements

As the number of enquiries increases, manual processing creates several problems:

1. Slow response times.
2. Leads being forgotten.
3. Inconsistent lead qualification.
4. Incomplete customer information.
5. Difficulty prioritizing high-value customers.
6. Poor visibility into lead status.
7. Increased administrative workload for sales staff.
8. Lost sales opportunities.

The PrimeHomes Realty Lead Bot will automate the repetitive parts of this process while keeping sales personnel involved where human intervention is required.

---

# 3. Product Goal

The primary goal is to build a system that converts unstructured customer enquiries into actionable, trackable real estate leads.

The system should allow PrimeHomes Realty to:

- Capture enquiries automatically.
- Understand customer intent.
- Extract structured requirements.
- Store leads reliably.
- Qualify and score leads.
- Respond quickly.
- Notify sales staff.
- Assign leads.
- Track follow-up.
- Track lead status.
- Maintain conversation history.
- Provide useful information to the sales team.

---

# 4. Product Objectives

## 4.1 Primary Objectives

The system must:

1. Receive a customer message.
2. Identify the customer and/or create a new lead.
3. Understand the customer's intent.
4. Extract relevant property requirements.
5. Identify missing information.
6. Ask appropriate follow-up questions.
7. Store the lead in the SQL database.
8. Calculate a lead qualification score.
9. Classify the lead.
10. Generate an appropriate customer response.
11. Notify the sales team when required.
12. Allow sales staff to follow up.
13. Track the lead lifecycle.
14. Maintain a record of customer interactions.

---

## 4.2 Secondary Objectives

The system should eventually support:

- Multiple communication channels.
- Lead assignment.
- Sales team dashboards.
- Lead search and filtering.
- Automated follow-up reminders.
- Lead analytics.
- Property matching.
- Sales performance reporting.
- Google Sheets reporting.
- Human takeover of conversations.

---

# 5. Non-Goals

The first version of the system will **not** attempt to solve everything.

The following are outside the initial MVP scope:

- Full property management software.
- Property listing management.
- Property payment processing.
- Legal documentation.
- Property valuation.
- Automated contract generation.
- Mortgage processing.
- Automated negotiation.
- Fully autonomous sales agents.
- Automated property booking without human approval.
- Replacing the sales team.

The bot is primarily a **lead intake, qualification, routing, response, and tracking system**.

---

# 6. Target Users

## 6.1 Potential Customer

A person interested in buying, renting, selling, or enquiring about real estate.

Examples:

- First-time buyer
- Property investor
- Tenant
- Land buyer
- Property seller
- Existing customer
- Person researching property prices

---

## 6.2 Sales Agent

A PrimeHomes Realty employee responsible for following up with leads.

Responsibilities include:

- Reviewing leads.
- Contacting customers.
- Providing property information.
- Scheduling viewings.
- Updating lead status.
- Recording follow-up activities.

---

## 6.3 Sales Manager

A manager responsible for monitoring the sales pipeline.

Responsibilities include:

- Monitoring incoming leads.
- Assigning leads.
- Reviewing high-value leads.
- Monitoring sales-agent performance.
- Reviewing lead conversion.
- Managing lead priorities.

---

## 6.4 System Administrator

Responsible for the technical configuration of the system.

Responsibilities include:

- Managing integrations.
- Managing workflows.
- Managing system configuration.
- Monitoring errors.
- Managing users and permissions.

---

# 7. User Stories

## 7.1 Customer

### US-001 — Submit enquiry

**As a potential customer,**

I want to send a message describing the property I am looking for,

so that PrimeHomes Realty can understand my requirements.

---

### US-002 — Receive an immediate response

**As a potential customer,**

I want to receive a quick response after sending an enquiry,

so that I know my request has been received.

---

### US-003 — Provide missing information

**As a potential customer,**

I want the bot to ask me relevant questions,

so that I can provide information required to help me find a property.

---

### US-004 — Speak naturally

**As a potential customer,**

I want to communicate naturally rather than filling out a complicated form,

so that providing my requirements is easy.

---

# 8. Sales Agent User Stories

### US-005 — View leads

**As a sales agent,**

I want to view leads assigned to me,

so that I know which customers I need to contact.

---

### US-006 — Prioritize leads

**As a sales agent,**

I want leads to have a qualification level,

so that I can prioritize valuable or urgent customers.

---

### US-007 — View customer requirements

**As a sales agent,**

I want to see structured customer requirements,

so that I do not have to manually read the entire conversation to understand the customer's needs.

---

### US-008 — Update lead status

**As a sales agent,**

I want to update the status of a lead,

so that the company can track its progress.

---

### US-009 — Follow up

**As a sales agent,**

I want to record follow-up activities,

so that the company has a history of interactions with each lead.

---

# 9. Core Functional Requirements

# 9.1 Lead Intake

The system must accept customer enquiries from supported channels.

The initial implementation may use the React frontend as the primary interface.

Future integrations may include:

- WhatsApp
- Website chat
- Email
- Facebook Messenger
- Instagram
- Other messaging platforms

### Required Input

A customer message should contain at minimum:

```text
message
channel
conversation_id
```

Where available, the system should also receive:

```text
customer_name
phone
email
external_customer_id
timestamp
```

---

# 9.2 Customer Identification

The system must determine whether an incoming message belongs to:

- An existing customer/lead.
- A new customer/lead.

The system should attempt to identify existing customers using available identifiers such as:

1. Customer ID.
2. Phone number.
3. Email.
4. Channel-specific user ID.
5. Conversation ID.

The system must avoid creating duplicate leads where an existing customer can be identified reliably.

---

# 9.3 Message Understanding

The AI layer should analyze the customer's message and identify relevant information.

Example input:

> "I'm looking for a 3 bedroom apartment in Lekki. My budget is around 80 million and I want to move within two months."

Expected structured result:

```json
{
  "intent": "buying",
  "property_type": "apartment",
  "location": "Lekki",
  "bedrooms": 3,
  "budget": 80000000,
  "currency": "NGN",
  "timeline": "within_3_months"
}
```

The AI must not invent information that the customer did not provide.

Unknown information should be represented as `null`, `unknown`, or an equivalent structured value.

---

# 9.4 Lead Information

The system should support the following lead attributes.

## Customer Information

- Lead ID
- Customer name
- Email
- Phone number
- Channel
- External customer ID
- Created date
- Updated date

## Property Requirements

- Property type
- Number of bedrooms
- Number of bathrooms
- Location
- Preferred areas
- Budget
- Currency
- Buy/rent
- Furnished/unfurnished where applicable
- Property purpose

## Customer Intent

Possible intents include:

- Buying
- Renting
- Selling
- Land enquiry
- Property enquiry
- Investment
- General enquiry
- Unknown

## Timeline

Possible values include:

- Immediate
- Within 1 month
- Within 3 months
- Within 6 months
- More than 6 months
- Just researching
- Unknown

---

# 9.5 Missing Information Detection

After extracting information, the system should determine whether enough information exists to meaningfully proceed.

For example:

Customer:

> "I want to buy a house."

The system may determine that important information is missing.

It may respond:

> "Absolutely. I can help with that. Which location are you interested in, and what budget range are you considering?"

The bot should ask only useful questions.

It should avoid asking for information that has already been provided.

---

# 9.6 Lead Qualification

Each lead should receive a qualification score.

The score should be based on business rules rather than relying entirely on AI.

Possible factors:

- Budget
- Timeline
- Property type
- Customer intent
- Location
- Completeness of requirements
- Customer engagement
- Buying vs researching
- Other business-specific criteria

Example:

```text
Lead Score: 85/100
Classification: HOT
```

---

# 9.7 Lead Classification

The initial system should support:

### HOT

High-priority lead with strong buying/renting intent and/or high business value.

Example:

```text
3-bedroom apartment
Lekki
₦80 million
Buying
Moving within 1 month
```

### WARM

Potential customer with reasonable intent but some uncertainty or longer timeline.

Example:

```text
2-bedroom apartment
Ikeja
Budget unknown
Buying
Within 3 months
```

### COLD

Low urgency, incomplete requirements, or primarily researching.

Example:

```text
"I just want to know how much houses cost in Lagos."
```

### UNQUALIFIED

Insufficient information or an enquiry outside the company's supported services.

---

# 9.8 AI Response Generation

The AI should generate customer responses based on structured lead information and conversation context.

Responses should be:

- Professional.
- Friendly.
- Concise.
- Relevant.
- Helpful.
- Non-deceptive.

The AI must not claim that a property exists, is available, or is reserved unless that information has been verified by the system.

For example, the bot should not say:

> "We have a 3-bedroom apartment available in Lekki for ₦80 million."

unless the property database has confirmed this.

---

# 9.9 Human Handoff

The system must support escalation to a human sales agent.

A human handoff may occur when:

- Lead is HOT.
- Customer explicitly requests an agent.
- Customer asks a complex question.
- AI confidence is low.
- Customer wants to schedule a viewing.
- Customer wants to negotiate.
- Customer asks for unavailable information.
- An automation or integration fails.

The system should record that the conversation has been handed over.

---

# 9.10 Sales Notification

The system should notify the appropriate sales team when a lead meets configured criteria.

Example:

```text
🔥 HOT LEAD

Name: John
Property: 3-bedroom apartment
Location: Lekki
Budget: ₦80,000,000
Timeline: Within 1 month
Score: 92/100

Action required:
Contact customer.
```

The notification channel may initially be:

- Email
- Google Sheets
- Internal dashboard

Future options:

- WhatsApp
- Slack
- Microsoft Teams
- CRM

---

# 9.11 Lead Assignment

Leads should eventually be assigned to sales agents.

The system should support configurable assignment strategies such as:

- Manual assignment.
- Round robin.
- Location-based assignment.
- Property-type assignment.
- Workload-based assignment.

For the MVP, manual assignment or simple round-robin assignment is sufficient.

---

# 9.12 Lead Status

Each lead should have a lifecycle status.

Initial statuses:

```text
NEW
CONTACTED
QUALIFIED
FOLLOW_UP
VIEWING_SCHEDULED
NEGOTIATION
WON
LOST
UNQUALIFIED
```

The exact status model may be refined during system design.

---

# 9.13 Follow-Up Tracking

The system should allow sales personnel to record follow-up actions.

Examples:

```text
Called customer
Sent property listings
Scheduled viewing
Customer requested callback
Customer did not respond
Sent reminder
```

Each activity should record:

- Lead ID
- Agent
- Activity type
- Notes
- Timestamp
- Next follow-up date where applicable

---

# 10. Conversation Management

The system should maintain conversation history.

A conversation should contain:

- Conversation ID
- Lead ID
- Channel
- Messages
- Sender
- Timestamp
- Message type
- AI processing result where applicable

Example:

```text
Customer:
I'm looking for a house in Lekki.

Bot:
Sure. What type of property are you looking for?

Customer:
A 3-bedroom apartment.

Bot:
Great. What budget range are you considering?
```

Conversation history should be available to authorized sales staff.

---

# 11. React Frontend Requirements

The frontend will be built using **React**.

The first version should provide a customer-facing chat interface.

## Customer Chat

The interface should include:

- Chat window.
- Message input.
- Send button.
- Loading state.
- Error state.
- Bot responses.
- Conversation initialization.

The UI should be responsive and work on:

- Desktop
- Tablet
- Mobile

---

# 12. Sales Dashboard Requirements

A sales dashboard may be implemented as part of the MVP or immediately after the initial customer chat system.

The dashboard should allow authorized users to:

- View leads.
- Search leads.
- Filter leads.
- View lead score.
- View lead status.
- View customer requirements.
- View conversation history.
- Assign leads.
- Update status.
- Record follow-up.
- View upcoming follow-ups.

Example lead table:

| Lead | Property | Location | Budget | Score | Status | Assigned To |
|---|---|---|---:|---:|---|---|
| John | 3 Bedroom | Lekki | ₦80M | 92 | New | Agent A |
| Mary | 2 Bedroom | Ikeja | ₦45M | 74 | Contacted | Agent B |

---

# 13. FastAPI Backend Requirements

The backend will be implemented using **Python and FastAPI**.

The backend will provide APIs between the React frontend and the automation system.

Initial API candidates include:

```http
POST /api/leads
POST /api/chat
GET /api/leads/{lead_id}
GET /api/leads
PATCH /api/leads/{lead_id}
POST /api/leads/{lead_id}/activities
GET /api/leads/{lead_id}/conversation
```

The final API contract will be defined during the System Design phase.

---

# 14. n8n Requirements

n8n will act as the **automation and orchestration layer**.

n8n should coordinate:

```text
Frontend / API
      ↓
    n8n
      ↓
   AI Processing
      ↓
 Data Validation
      ↓
 Qualification
      ↓
 SQL Database
      ↓
 Notifications
      ↓
 Customer Response
```

n8n should not be responsible for every piece of business logic.

Where appropriate:

- FastAPI handles API concerns.
- SQL handles persistent data.
- n8n handles orchestration and integrations.
- AI handles natural-language understanding.
- React handles user interaction.

---

# 15. AI Requirements

The AI system should perform the following tasks.

## 15.1 Intent Classification

Determine what the customer wants.

Example:

```text
"I want to rent a 2 bedroom apartment in Ikeja."

intent = renting
```

---

## 15.2 Entity Extraction

Extract relevant entities.

Example:

```json
{
  "location": "Ikeja",
  "property_type": "apartment",
  "bedrooms": 2,
  "intent": "renting"
}
```

---

## 15.3 Conversation Understanding

The AI should use previous messages when interpreting new messages.

Example:

Customer:

> "Around 50 million."

The AI should understand that the customer may be answering a previous budget question.

---

## 15.4 Response Generation

The AI should generate appropriate responses based on:

- Conversation history.
- Extracted requirements.
- Missing fields.
- Business rules.
- Lead status.
- Available property information where integrated.

---

## 15.5 Structured AI Output

AI extraction should preferably produce structured JSON rather than free-form text.

Example:

```json
{
  "intent": "buying",
  "property_type": "apartment",
  "location": "Lekki",
  "bedrooms": 3,
  "budget": 80000000,
  "currency": "NGN",
  "timeline": "within_3_months",
  "confidence": 0.94
}
```

The backend/n8n workflow should validate AI output before storing it.

---

# 16. Database Requirements

## 16.1 Primary Database

The system will use a **SQL database as the primary system of record**.

The SQL database should store authoritative application data.

Potential options include:

- PostgreSQL
- MySQL

**Recommended:** PostgreSQL.

Reasons:

- Strong relational data model.
- Good support for structured relationships.
- Reliable transactions.
- Suitable for conversations and lead records.
- Good support for future scaling.
- Works well with FastAPI and n8n.

---

# 16.2 Google Sheets

Google Sheets should **not** be the primary database.

Instead, n8n can synchronize selected information into Google Sheets for:

- Sales team visibility.
- Simple reporting.
- Quick exports.
- Temporary operational workflows.
- Non-technical staff access.

Architecture:

```text
                ┌──────────────┐
                │ PostgreSQL   │
                │ System of    │
                │ Record       │
                └──────┬───────┘
                       │
                      n8n
                       │
                ┌──────▼───────┐
                │ Google Sheets│
                │ Reporting /  │
                │ Operations   │
                └──────────────┘
```

This prevents the system from becoming dependent on spreadsheet data integrity.

---

# 17. Proposed Core Data Entities

The database will eventually contain entities similar to:

```text
Lead
Customer
Conversation
Message
PropertyRequirement
LeadActivity
SalesAgent
LeadAssignment
FollowUp
Notification
```

The exact schema will be designed during the System Design phase.

---

# 18. Lead Scoring Requirements

The scoring engine should produce a numerical score.

Example:

```text
0 - 39    COLD
40 - 69   WARM
70 - 100  HOT
```

The exact thresholds should be configurable.

A possible scoring model:

| Factor | Example Weight |
|---|---:|
| Purchase/rental intent | 20 |
| Timeline | 20 |
| Budget provided | 15 |
| Property requirements complete | 15 |
| Location provided | 10 |
| Customer engagement | 10 |
| Business-specific value | 10 |
| **Total** | **100** |

These values are examples and must be validated with the actual business.

The final score should be calculated by deterministic business logic rather than allowing the AI to arbitrarily assign a score.

---

# 19. Notifications

Notifications should be triggered based on business rules.

Examples:

### HOT Lead

```text
Lead score >= configured HOT threshold
```

Action:

```text
Notify sales team immediately.
```

### Customer Requests Agent

Action:

```text
Create human handoff event.
Notify assigned agent.
```

### Follow-Up Due

Action:

```text
Notify assigned agent.
```

---

# 20. Error Handling

The system must handle failures gracefully.

Potential failures include:

- AI provider unavailable.
- n8n workflow failure.
- Database unavailable.
- FastAPI unavailable.
- Invalid AI output.
- Notification failure.
- Duplicate message.
- Invalid customer input.
- Network failure.
- Third-party API failure.

The system should:

1. Detect the failure.
2. Log the failure.
3. Avoid corrupting lead data.
4. Retry where appropriate.
5. Notify an administrator for critical failures.
6. Provide a safe fallback response to the customer where possible.

---

# 21. Security Requirements

The system should implement appropriate security controls.

## Authentication

Sales dashboard users should be authenticated.

## Authorization

Users should only have access to information appropriate to their role.

Example:

```text
Sales Agent
    ↓
Assigned leads

Sales Manager
    ↓
All sales leads

Administrator
    ↓
System configuration
```

## Data Protection

The system should protect:

- Customer phone numbers.
- Customer emails.
- Conversation history.
- Lead information.
- Sales information.

API credentials and secrets must never be stored directly in source code.

---

# 22. Logging and Monitoring

The system should maintain logs for important events.

Examples:

```text
Lead created
Lead updated
AI extraction performed
Lead scored
Notification sent
Sales agent assigned
Customer message received
Customer response generated
Follow-up created
Workflow failed
```

Logs should help developers diagnose problems without exposing unnecessary sensitive customer information.

---

# 23. Reliability Requirements

The system should avoid losing customer enquiries.

If an external service fails, the system should preserve the incoming request where possible and allow processing to continue after recovery.

Important operations should be designed to be **idempotent** where practical.

For example, receiving the same external message twice should not create two separate leads unnecessarily.

---

# 24. Performance Requirements

The initial MVP should target:

### Customer Response

Normal requests should receive a response within a few seconds where external AI/API latency permits.

### Lead Processing

Lead extraction and storage should occur automatically without requiring manual intervention.

### Dashboard

Common dashboard operations should respond quickly under the expected initial user load.

The exact performance targets will be established after deployment requirements are known.

---

# 25. Scalability

The initial system should be designed for a small-to-medium real estate company but should not unnecessarily prevent future growth.

The architecture should allow:

```text
1 channel
    ↓
multiple channels
```

and:

```text
10 leads/day
    ↓
100 leads/day
    ↓
1,000+ leads/day
```

without requiring a complete rewrite of the system.

---

# 26. Initial End-to-End Workflow

The MVP workflow should approximately follow:

```text
Customer
   │
   ▼
React Chat UI
   │
   ▼
FastAPI
   │
   ▼
n8n Webhook
   │
   ▼
Validate Request
   │
   ▼
Identify/Create Lead
   │
   ▼
AI Processing
   │
   ▼
Extract Requirements
   │
   ▼
Validate AI Output
   │
   ▼
Check Missing Information
   │
   ├───────────────┐
   │               │
   ▼               ▼
Missing Data     Complete
   │               │
   ▼               ▼
Ask Question    Calculate Score
                   │
                   ▼
               Store Lead
                   │
                   ▼
             Determine Priority
                   │
          ┌────────┴────────┐
          ▼                 ▼
        HOT              NORMAL
          │                 │
          ▼                 ▼
   Notify Sales       Standard Flow
          │                 │
          └────────┬────────┘
                   ▼
             Generate Reply
                   │
                   ▼
             Customer
```

---

# 27. Example Scenario

## Customer Message

> "Hi, I'm looking for a 3-bedroom apartment around Lekki. My budget is around ₦80 million. I'd like to move within two months."

## AI Extraction

```json
{
  "intent": "buying",
  "property_type": "apartment",
  "bedrooms": 3,
  "location": "Lekki",
  "budget": 80000000,
  "currency": "NGN",
  "timeline": "within_3_months"
}
```

## Qualification

```text
Score: 90/100
Classification: HOT
```

## Database

The lead is stored in PostgreSQL.

## Sales Notification

The sales team receives:

```text
🔥 HOT LEAD

3-bedroom apartment
Location: Lekki
Budget: ₦80M
Timeline: Within 2 months

Score: 90/100

Immediate follow-up recommended.
```

## Customer Response

The customer receives an appropriate response confirming that the enquiry has been received and, where necessary, asking for the next missing piece of information.

---

# 28. MVP Scope

The first production-capable MVP should focus on the following.

## Customer Side

- React chat interface.
- Message submission.
- Bot response.
- Basic conversation history.

## Backend

- FastAPI application.
- Lead API.
- Chat API.
- Validation.
- Basic authentication architecture.

## n8n

- Webhook trigger.
- Lead processing workflow.
- AI extraction.
- Lead qualification.
- Database integration.
- Customer response generation.
- Sales notification.

## Database

- PostgreSQL.
- Customer records.
- Lead records.
- Requirements.
- Conversations.
- Messages.
- Lead activities.

## Sales

- Basic lead dashboard.
- Lead status.
- Lead score.
- Lead assignment.
- Follow-up notes.

## Google Sheets

- Optional synchronization of leads for operational visibility.

---

# 29. Future Features

The architecture should allow future development of:

## Communication Channels

- WhatsApp.
- Email.
- Website chat.
- Instagram.
- Facebook Messenger.

## Property Matching

Automatically match customer requirements against available properties.

Example:

```text
Customer requirements
        ↓
Property database
        ↓
Matching engine
        ↓
Matching properties
```

## Automated Follow-Up

For example:

```text
Day 0 → Initial response
Day 1 → Follow-up
Day 3 → Follow-up
Day 7 → Final follow-up
```

## Advanced Sales Dashboard

- Conversion rate.
- Lead source.
- Lead funnel.
- Agent performance.
- Revenue attribution.
- Average response time.
- Lead response rate.

## Analytics

Potential metrics:

```text
Total leads
Hot leads
Warm leads
Cold leads
Converted leads
Lost leads
Average lead score
Average response time
Conversion rate
```

---

# 30. Success Metrics

The system should be evaluated using measurable business outcomes.

## Lead Processing

Target:

> 95%+ of valid incoming enquiries are successfully captured.

## Lead Data Extraction

Target:

> 90%+ accuracy for clearly stated customer requirements.

## Response Time

Target:

> Automated responses should normally be generated within seconds, subject to external service latency.

## Lead Follow-Up

Target:

> High-priority leads should be surfaced to sales staff immediately.

## Data Completeness

Target:

> Reduce the number of leads requiring manual information extraction.

## Lead Loss

Target:

> Reduce leads lost due to delayed or forgotten follow-up.

---

# 31. Acceptance Criteria

The MVP will be considered functional when the following scenario works end-to-end.

### Scenario

A customer enters:

> "Hi, I want to buy a 3 bedroom apartment in Lekki. My budget is ₦80 million and I want to move within two months."

### Expected Result

The system must:

- Receive the message.
- Create or identify the customer.
- Create a lead.
- Extract:
  - Buying intent.
  - Apartment.
  - 3 bedrooms.
  - Lekki.
  - ₦80 million.
  - Two-month timeline.
- Store the information.
- Calculate a lead score.
- Classify the lead.
- Generate a customer response.
- Notify the sales team if the lead meets the configured threshold.
- Allow the sales team to view the lead.
- Allow the sales team to update its status.
- Preserve the conversation history.
- Allow follow-up activity to be recorded.

---

# 32. Technical Architecture Direction

The initial technical responsibility boundaries are:

```text
┌───────────────────────────────┐
│           CUSTOMER            │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│        REACT FRONTEND         │
│                               │
│ Chat / Lead UI                │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│          FASTAPI              │
│                               │
│ API / Validation /            │
│ Application Business Logic    │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│             n8n               │
│                               │
│ Workflow Orchestration        │
│ Integrations                  │
│ AI Processing                 │
│ Notifications                 │
└───────┬─────────────┬─────────┘
        │             │
        ▼             ▼
┌──────────────┐  ┌──────────────┐
│ PostgreSQL   │  │      AI      │
│              │  │   Provider   │
│ System of    │  │              │
│ Record       │  │ NLP /        │
│              │  │ Extraction   │
└──────┬───────┘  └──────────────┘
        │
        ▼
┌───────────────────────────────┐
│       GOOGLE SHEETS           │
│                               │
│ Reporting / Operational View  │
└───────────────────────────────┘
```

---

# 33. Architectural Principles

The following principles will guide development.

## Principle 1 — Single Source of Truth

PostgreSQL is the authoritative source for application data.

Google Sheets is a supporting integration, not the primary database.

---

## Principle 2 — Separation of Responsibilities

React handles presentation.

FastAPI handles API and application-level backend responsibilities.

n8n handles workflow orchestration and integrations.

AI handles natural-language understanding.

PostgreSQL handles persistent relational data.

---

## Principle 3 — AI Does Not Control Critical Business Logic

AI may extract information and generate responses.

However, critical decisions such as:

- Lead scoring.
- Required fields.
- Lead status.
- Database writes.
- Notification thresholds.

should be controlled by deterministic application/workflow logic wherever possible.

---

## Principle 4 — Never Trust Raw AI Output

AI output must be validated before it is stored or used by downstream automation.

---

## Principle 5 — Human-in-the-Loop

The system should automate repetitive work but allow humans to take over whenever necessary.

---

## Principle 6 — Design for Extension

The initial implementation should not unnecessarily lock the system into one communication channel, AI provider, notification platform, or frontend implementation.

---

# 34. Project Development Phases

## Phase 1 — Requirements

Deliverables:

- PRD
- User stories
- Functional requirements
- Non-functional requirements
- Success criteria

**Current phase.**

---

## Phase 2 — System Design

Deliverables:

- System architecture.
- Component architecture.
- Data flow diagrams.
- Database schema.
- API specification.
- n8n workflow architecture.
- Authentication design.
- AI processing design.

---

## Phase 3 — Database

Deliverables:

- PostgreSQL setup.
- Database schema.
- Tables.
- Relationships.
- Indexes.
- Migrations.
- Seed data.

---

## Phase 4 — FastAPI Backend

Deliverables:

- FastAPI project.
- API routes.
- Models.
- Services.
- Validation.
- Error handling.
- Database integration.

---

## Phase 5 — React Frontend

Deliverables:

- React application.
- Chat interface.
- API integration.
- Loading/error states.
- Basic sales dashboard.

---

## Phase 6 — n8n

Deliverables:

- Lead intake workflow.
- AI extraction workflow.
- Qualification workflow.
- Database workflow.
- Notification workflow.
- Response workflow.
- Follow-up workflow.

---

## Phase 7 — AI

Deliverables:

- Extraction prompts.
- Structured output schema.
- Intent classification.
- Missing-information detection.
- Response generation.
- Confidence handling.

---

## Phase 8 — Integration

Connect:

```text
React
 ↓
FastAPI
 ↓
n8n
 ↓
AI
 ↓
PostgreSQL
 ↓
Sales notification
```

---

## Phase 9 — Testing

Test:

- Complete enquiries.
- Incomplete enquiries.
- Ambiguous enquiries.
- Multiple messages.
- Existing customers.
- Duplicate messages.
- Hot leads.
- Warm leads.
- Cold leads.
- Invalid data.
- AI failures.
- Database failures.
- n8n failures.
- Notification failures.

---

## Phase 10 — Optimization

Improve:

- Performance.
- Reliability.
- User experience.
- AI accuracy.
- Workflow simplicity.
- Observability.
- Security.
- Maintainability.

---

# 35. Initial Project Structure

The initial repository may follow:

```text
real-estate-lead-bot/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── README.md
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── core/
│   │   └── main.py
│   │
│   ├── tests/
│   ├── requirements.txt
│   └── README.md
│
├── n8n/
│   ├── workflows/
│   └── README.md
│
├── database/
│   ├── migrations/
│   ├── seeds/
│   └── README.md
│
├── docs/
│   ├── PRD.md
│   ├── SYSTEM_DESIGN.md
│   ├── API.md
│   ├── DATABASE.md
│   └── N8N_WORKFLOWS.md
│
├── tests/
│
├── .env.example
├── .gitignore
└── README.md
```

The exact structure will be finalized during the System Design phase.

---

# 36. Open Questions

The following questions must be resolved before the architecture is finalized.

### Business

1. Which property types does PrimeHomes Realty actually sell/rent?
2. Which geographic locations are supported?
3. What qualifies as a HOT lead?
4. How should leads be assigned to sales agents?
5. What notification channels should sales staff use?
6. What information is mandatory before a lead is considered qualified?

### Communication

7. What will be the first customer communication channel?
8. Will WhatsApp be part of the MVP or a later integration?
9. Should the bot support voice messages in the future?

### AI

10. Which AI provider will be used?
11. What level of confidence is required before accepting AI-extracted information?
12. Which questions should the AI ask automatically?

### Database

13. Which PostgreSQL deployment method will be used?
14. Will the database be local during development and hosted in production?
15. Which data should be synchronized to Google Sheets?

### Sales

16. Will the MVP include a sales dashboard?
17. Will agents have individual accounts?
18. Should agents see all leads or only assigned leads?

These questions should be resolved progressively rather than blocking the entire project.

---

# 37. Definition of Done — MVP

The MVP is considered complete when:

- A customer can send a message through the React interface.
- FastAPI can receive and validate the request.
- n8n can process the request.
- AI can extract structured requirements.
- Extracted data is validated.
- A lead can be created in PostgreSQL.
- Existing leads can be identified.
- Missing information can be detected.
- The bot can ask follow-up questions.
- A lead score can be calculated.
- Leads can be classified.
- The customer can receive a response.
- HOT leads can trigger a sales notification.
- Sales staff can view leads.
- Sales staff can update lead status.
- Follow-up activities can be recorded.
- Conversation history is preserved.
- Google Sheets can optionally receive synchronized lead information.
- Errors are logged and handled appropriately.
- The complete workflow can be tested end-to-end.

---

# 38. Final Product Vision

The final system should evolve from a simple chatbot into a **Lead Management and Sales Automation Platform for PrimeHomes Realty**.

The long-term system should look like:

```text
                    CUSTOMERS
                        │
          ┌─────────────┼─────────────┐
          │             │             │
       Website       WhatsApp       Email
          │             │             │
          └─────────────┼─────────────┘
                        │
                        ▼
                 ┌─────────────┐
                 │   FastAPI   │
                 └──────┬──────┘
                        │
                        ▼
                 ┌─────────────┐
                 │     n8n     │
                 │ Orchestrator│
                 └──────┬──────┘
                        │
              ┌─────────┼─────────┐
              │         │         │
              ▼         ▼         ▼
             AI      PostgreSQL  Rules
              │         │         │
              └─────────┼─────────┘
                        │
                        ▼
                LEAD QUALIFICATION
                        │
              ┌─────────┴─────────┐
              │                   │
             HOT               NORMAL
              │                   │
              ▼                   ▼
        SALES ALERT          AUTOMATION
              │                   │
              └─────────┬─────────┘
                        │
                        ▼
                 SALES DASHBOARD
                        │
                        ▼
                    FOLLOW-UP
                        │
                        ▼
                 LEAD CONVERSION
```

The core objective is not simply to automate messages.

The objective is to build a reliable system that turns **customer conversations into structured sales opportunities** and gives PrimeHomes Realty a repeatable process for managing those opportunities from first contact through conversion.

---

# Document Status

**Status:** Draft — Ready for System Design

**Next document:** System Design Document (SDD)

The System Design Document should translate this PRD into:

1. Detailed architecture.
2. Component responsibilities.
3. Database schema.
4. API contracts.
5. n8n workflow design.
6. AI processing pipeline.
7. Lead scoring implementation.
8. Authentication/authorization design.
9. Error-handling strategy.
10. React application structure.
11. Development sequence.