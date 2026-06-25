# 🤖 Autonomous AI Career Agent

An autonomous AI agent that helps professionals land better jobs by planning, executing, and tracking career-related tasks.

Unlike a traditional chatbot that only answers questions, this agent can reason about a user's goal, select the appropriate tools, execute multi-step workflows, maintain memory, and (with user approval) perform browser-based actions such as researching jobs and assisting with applications.

---

# Vision

### User Goal

> "Help me get a 15 LPA AI Engineer job."

Instead of simply replying with text, the agent plans and executes multiple tasks automatically.

Example workflow:

```
User Goal
     │
     ▼
Planner Agent
     │
     ▼
Analyze Resume
     │
     ▼
Find Skill Gaps
     │
     ▼
Search Jobs
     │
     ▼
Compare Resume with Job Descriptions
     │
     ▼
Generate Learning Roadmap
     │
     ▼
Generate Interview Questions
     │
     ▼
Create PDF Report & Study Tracker
     │
     ▼
(Optional) Apply to Jobs with User Approval
```

---

# Core Features

## Resume Intelligence

* Resume Analysis
* ATS Feedback
* Skill Extraction
* Skill Gap Detection
* Resume Improvement Suggestions

---

## Career Planning

* Personalized Learning Roadmaps
* Daily & Weekly Study Plans
* Progress Tracking
* Interview Preparation

---

## Job Intelligence

* Search AI/Software jobs
* Read Job Descriptions
* Compare Resume with JD
* Match Score Calculation
* Missing Skills Detection

---

## Autonomous Task Execution

The agent can autonomously:

* Plan multi-step workflows
* Select appropriate tools
* Execute tasks
* Generate reports
* Track progress

---

## Browser Automation (Future)

With user approval:

* Search LinkedIn/Naukri/Indeed jobs
* Open application pages
* Fill forms
* Upload resumes
* Assist in job applications

---

## Memory

The agent remembers:

* Previous resumes
* Completed skills
* Roadmaps
* Applications
* Interview history

---

# Architecture

```
                 User Goal
                     │
                     ▼
              Planner Agent
                     │
     ┌───────────────┼───────────────┐
     ▼               ▼               ▼
Resume Tool    Job Search Tool   Roadmap Tool
     │               │               │
     ▼               ▼               ▼
Interview Tool   PDF Tool      CSV Tool
          \          |          /
           \         |         /
            ───── Memory ─────
                     │
                     ▼
               Final Response
```

---

# Tech Stack

### AI

* OpenAI GPT-5
* LangGraph
* LangChain
* Structured Outputs
* Function Calling

### Backend

* FastAPI
* Python

### Database

* SQLite
* PostgreSQL (Planned)

### Browser Automation

* Playwright (Planned)

### Deployment

* Docker
* GitHub Actions
* AWS (Planned)

---

# Development Roadmap

## Phase 1 — Foundation

* [ ] Project Setup
* [ ] Resume Analysis Tool
* [ ] Resume Analysis API
* [ ] Project Architecture
* [ ] Logging
* [ ] Error Handling

---

## Phase 2 — Career Intelligence

* [ ] Skill Gap Analyzer
* [ ] Roadmap Generator
* [ ] Interview Generator
* [ ] Resume Improvement
* [ ] PDF Report Generator
* [ ] CSV Study Tracker

---

## Phase 3 — Agentic AI

* [ ] LangGraph Integration
* [ ] Planner Agent
* [ ] Tool Calling
* [ ] Conditional Routing
* [ ] Agent Memory
* [ ] Multi-Step Planning

---

## Phase 4 — Job Intelligence

* [ ] Job Search Tool
* [ ] Job Description Analysis
* [ ] Resume vs JD Matching
* [ ] ATS Score
* [ ] Company Research

---

## Phase 5 — Browser Automation

* [ ] Playwright Integration
* [ ] Login Automation
* [ ] Job Application Assistant
* [ ] Human Approval Workflow
* [ ] Browser Agent

---

## Phase 6 — Production

* [ ] PostgreSQL
* [ ] Redis
* [ ] Authentication
* [ ] Docker
* [ ] GitHub Actions
* [ ] AWS Deployment
* [ ] Monitoring
* [ ] Logging

---

# Current Status

🚧 Under Active Development

Current milestone:

✅ Resume Analysis Tool


