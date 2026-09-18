# 🏭 Sovereign On-Premise Agentic AI Workbench

## SIH 2026 — Problem Statement 26117

**Organization:** Mangalore Refinery and Petrochemicals Limited (MRPL)  
**Category:** Software  
**Theme:** Smart Automation  

An on-premise, sovereign AI workbench for confidential industrial work using open-weight multimodal language models. The system processes internal documents, images, scanned PDFs, handwritten notes, engineering drawings, and photographs without sending organizational data outside the local network.

> **Important:** The official screenshot shows Problem Statement ID **26117**. Always verify the final ID and wording on the official SIH portal before submission.

---

## Table of Contents

- [1. Problem Summary](#1-problem-summary)
- [2. Our Proposed Solution](#2-our-proposed-solution)
- [3. Objectives](#3-objectives)
- [4. Core Features](#4-core-features)
- [5. Demonstration Scenario](#5-demonstration-scenario)
- [6. System Architecture](#6-system-architecture)
- [7. Technology Stack](#7-technology-stack)
- [8. Project Structure](#8-project-structure)
- [9. Local Setup](#9-local-setup)
- [10. Usage Workflow](#10-usage-workflow)
- [11. API Plan](#11-api-plan)
- [12. Security and Sovereignty](#12-security-and-sovereignty)
- [13. Team Responsibilities](#13-team-responsibilities)
- [14. Development Roadmap](#14-development-roadmap)
- [15. Evaluation and Demo Checklist](#15-evaluation-and-demo-checklist)
- [16. Contribution Guidelines](#16-contribution-guidelines)
- [17. License](#17-license)

---

## 1. Problem Summary

Industrial organizations handle confidential manuals, SOPs, inspection reports, approval notes, engineering drawings, photographs, and correspondence. A normal chatbot is insufficient because the required system must:

- Search internal organizational knowledge.
- Understand text, scans, handwriting, images, and engineering documents.
- Perform multi-step tasks instead of giving only one answer.
- Produce real deliverables such as Word, Excel, PDF, and code files.
- Work entirely on-premise using open-weight models.
- Provide visible evidence that no external network calls occur.

The challenge is to build a working local AI system that can complete practical industrial tasks from beginning to end while protecting confidential information.

---

## 2. Our Proposed Solution

We propose **SovereignAI Workbench**, a local agentic AI platform with five major layers:

1. **Document ingestion:** Upload PDFs, images, office files, and text documents.
2. **Multimodal understanding:** Use local OCR, vision models, and language models.
3. **Knowledge grounding:** Search local manuals, SOPs, templates, and past correspondence.
4. **Agentic execution:** Plan and execute multi-step tasks with visible progress and logs.
5. **Deliverable generation:** Create approval notes, reports, spreadsheets, summaries, and code.

### Example

```text
Upload scanned inspection report
        ↓
Local OCR and image understanding
        ↓
Extract findings and measurements
        ↓
Search relevant local SOPs and manuals
        ↓
Check findings against procedures
        ↓
Draft approval note and action list
        ↓
Generate Word/PDF/Excel deliverables
        ↓
Display complete audit and network logs
```

---

## 3. Objectives

- Build a fully local AI assistant for confidential industrial workflows.
- Support at least two different task types.
- Demonstrate multimodal document understanding.
- Ground every answer in the local knowledge base where applicable.
- Generate useful files instead of only chat responses.
- Run with open-weight models and local embeddings.
- Prevent and visibly verify external calls.
- Preserve an audit trail for every upload, model call, tool call, and generated file.

---

## 4. Core Features

### 4.1 Multimodal document ingestion

Supported initial formats:

- PDF and scanned PDF
- PNG, JPG, and JPEG images
- DOCX and XLSX
- TXT, CSV, and Markdown

Processing capabilities:

- File type detection
- Page rendering
- OCR for scanned content
- Image preprocessing
- Table extraction
- Metadata extraction
- Document chunking

### 4.2 Local OCR and vision

- OCR scanned pages and handwritten notes where supported.
- Analyze photographs and diagrams with a local vision model.
- Preserve page numbers and source references.
- Show extracted text for user verification.

### 4.3 Local knowledge base

The knowledge base may contain:

- Standard Operating Procedures
- Technical manuals
- Safety instructions
- Report templates
- Approval formats
- Historical correspondence
- Public sample documents for demonstration

Documents are embedded locally and stored in a local vector index. No document is uploaded to a hosted AI service.

### 4.4 Agentic task execution

The agent should:

1. Understand the user request.
2. Select an appropriate local model and tools.
3. Create a task plan.
4. Retrieve relevant local knowledge.
5. Process the input documents.
6. Validate intermediate results.
7. Generate the requested deliverable.
8. Present sources, actions, warnings, and logs.

### 4.5 Deliverable generation

The MVP should generate:

- Approval notes in DOCX
- Findings and action lists in XLSX
- Final reports in PDF
- JSON summaries
- Code files and test files for coding tasks

### 4.6 Sovereignty dashboard

The dashboard should display:

- Current network mode
- Allowed local endpoints
- Blocked outbound requests
- Model and tool calls
- File access history
- Task execution timeline
- Exportable audit logs

---

## 5. Demonstration Scenario

### Scenario A: Inspection report to approval note

**Input:** A scanned inspection report containing typed text, a table, and handwritten remarks.

**Task:**

- Read and OCR the report.
- Extract equipment name, inspection date, findings, severity, and recommendations.
- Search the local SOP repository.
- Compare the findings with the applicable procedure.
- Create an approval note in DOCX.
- Create an action tracker in XLSX.
- Produce a final PDF report.

**Expected result:** The evaluator can see the input, agent plan, source references, generated files, and complete audit log.

### Scenario B: Multimodal coding task

**Input:** A technical specification or diagram.

**Task:**

- Read the specification locally.
- Extract requirements.
- Generate a code skeleton.
- Generate unit tests.
- Run the code in a restricted sandbox.
- Return the files and execution result.

**Expected result:** Code is generated, tested locally, and no external service is contacted.

---

## 6. System Architecture

```text
┌────────────────────────────────────────────────────────────┐
│                    Web User Interface                       │
│ Upload • Task Builder • Progress • Outputs • Audit Logs    │
└──────────────────────────┬─────────────────────────────────┘
                           │ HTTP/WebSocket
┌──────────────────────────▼─────────────────────────────────┐
│                    FastAPI Backend                          │
│ Auth • Jobs • Files • Agent API • Network Status            │
└───────────────┬───────────────────┬────────────────────────┘
                │                   │
┌───────────────▼────────┐  ┌──────▼─────────────────────────┐
│ Agent Orchestrator      │  │ Document Processing Pipeline    │
│ Planner • Tools • State │  │ OCR • Vision • Parsing • Tables │
└───────────────┬────────┘  └──────┬─────────────────────────┘
                │                   │
┌───────────────▼───────────────────▼─────────────────────────┐
│                    Local AI Services                         │
│ Open-weight LLM • Vision Model • Embedding Model • Reranker │
└───────────────┬───────────────────┬─────────────────────────┘
                │                   │
┌───────────────▼────────┐  ┌──────▼─────────────────────────┐
│ Local Knowledge Base    │  │ Local Storage and Audit Logs    │
│ Vector Index • Metadata │  │ Inputs • Outputs • Events       │
└────────────────────────┘  └──────────────────────────────────┘
```

### Design principles

- Local-first and offline-capable.
- Least-privilege tool access.
- Human approval before sensitive actions.
- Explainable execution with source references.
- Reproducible model and prompt configuration.
- No unrestricted code execution.

---

## 7. Technology Stack

| Layer | Recommended technology | Purpose |
|---|---|---|
| Frontend | React, Vite, TypeScript | Dashboard and task interface |
| Backend | Python, FastAPI | REST API and orchestration |
| LLM serving | Ollama or llama.cpp | Local open-weight inference |
| Language model | A suitable local instruct model | Text reasoning and generation |
| Vision model | Local vision-language model | Images and scanned documents |
| OCR | Tesseract or PaddleOCR | Text extraction |
| Embeddings | Sentence Transformers | Local semantic embeddings |
| Vector store | FAISS or Chroma | Local knowledge retrieval |
| Document parsing | PyMuPDF, python-docx, openpyxl | File processing |
| Output generation | python-docx, openpyxl, ReportLab | Deliverables |
| Database | SQLite for MVP, PostgreSQL later | Metadata and task state |
| Sandbox | Docker or restricted subprocess | Safe code execution |
| Deployment | Docker Compose | Reproducible local deployment |
| Monitoring | Structured logs and network monitor | Sovereignty evidence |

Model selection must depend on available hardware. Do not assume that a particular model or GPU is available at the venue.

---

## 8. Project Structure

```text
.
├── README.md
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── api/
│   │   ├── agents/
│   │   ├── documents/
│   │   ├── knowledge_base/
│   │   ├── models/
│   │   ├── outputs/
│   │   ├── security/
│   │   └── audit/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── types/
│   ├── package.json
│   └── Dockerfile
├── knowledge_base/
│   ├── manuals/
│   ├── sops/
│   ├── templates/
│   └── sample_documents/
├── outputs/
├── data/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── scripts/
│   ├── ingest_knowledge.py
│   ├── run_demo.py
│   └── verify_offline_mode.sh
├── deployment/
│   └── docker-compose.yml
└── docs/
    ├── ARCHITECTURE.md
    ├── API.md
    ├── SECURITY.md
    └── DEMO_SCRIPT.md
```

Never commit confidential organizational documents, credentials, model weights, generated outputs containing sensitive data, or private correspondence.

---

## 9. Local Setup

### Requirements

- Python 3.10 or newer
- Node.js 20 or newer
- Docker and Docker Compose
- At least 16 GB RAM for a basic demonstration
- Additional RAM/VRAM according to the selected local model
- Linux recommended; Windows users may use WSL2

### Clone the repository

```bash
git clone https://github.com/jeevanhs06/SIH2026-MRPL-SovereignAI-Workbench.git
cd SIH2026-MRPL-SovereignAI-Workbench
```

### Backend

```bash
cd backend
python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows PowerShell
# .venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

### Frontend

```bash
cd frontend
npm install
```

### Local model service

Install and configure the selected local model runtime according to the project setup guide. Models must be downloaded before the offline demonstration and loaded from local storage.

### Environment variables

Create a local `.env` file from `.env.example`. Do not commit it.

```env
APP_ENV=development
API_HOST=127.0.0.1
API_PORT=8000
DATABASE_URL=sqlite:///./data/workbench.db
MODEL_BASE_URL=http://127.0.0.1:11434
VECTOR_STORE_PATH=./data/vector_store
INPUT_DIR=./data/inputs
OUTPUT_DIR=./data/outputs
AUDIT_LOG_PATH=./data/audit.log
OFFLINE_MODE=true
ALLOW_EXTERNAL_NETWORK=false
```

### Start the development services

```bash
# Terminal 1
cd backend
source .venv/bin/activate
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

# Terminal 2
cd frontend
npm run dev
```

The exact commands may change as implementation files are added. Keep `docs/SETUP.md` updated whenever setup changes.

---

## 10. Usage Workflow

1. Open the local dashboard.
2. Upload a public sample document.
3. Select a task template.
4. Review the generated plan.
5. Start the task.
6. Watch OCR, retrieval, model, and file-generation steps.
7. Review cited source documents and extracted data.
8. Download the generated deliverables.
9. Open the sovereignty dashboard.
10. Export the audit log for the demo.

### Sample task definition

```json
{
  "name": "Inspection report to approval note",
  "input_files": ["inspection_report.pdf"],
  "steps": [
    "extract_text_and_tables",
    "analyze_findings",
    "retrieve_relevant_sops",
    "validate_against_sop",
    "generate_docx_approval_note",
    "generate_xlsx_action_tracker",
    "generate_pdf_summary"
  ],
  "require_human_review": true
}
```

---

## 11. API Plan

Planned endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/health` | Service health |
| `POST` | `/api/documents` | Upload a document |
| `GET` | `/api/documents/{id}` | Document metadata and extracted text |
| `POST` | `/api/knowledge/index` | Index local knowledge files |
| `POST` | `/api/tasks` | Create an agentic task |
| `GET` | `/api/tasks/{id}` | Get task status |
| `GET` | `/api/tasks/{id}/events` | Get task events |
| `GET` | `/api/tasks/{id}/outputs` | List generated files |
| `GET` | `/api/audit` | Query audit events |
| `GET` | `/api/security/network-status` | Show network status |

API contracts should be documented in `docs/API.md` and tested using automated integration tests.

---

## 12. Security and Sovereignty

### Required controls

- Bind development services to localhost by default.
- Deny outbound traffic in the demonstration environment.
- Use only local model endpoints.
- Disable telemetry in dependencies where possible.
- Store credentials outside the repository.
- Validate file type and size before processing.
- Scan uploads before parsing.
- Restrict generated code execution inside a sandbox.
- Apply role-based access for sensitive operations.
- Log every model, tool, file, and network event.
- Require human confirmation before final approval or external action.

### Demonstrating no external calls

The demo must show more than a written claim. Prepare:

- Firewall rules blocking outbound traffic.
- A network monitor showing only loopback/local connections.
- Application logs containing model and tool endpoints.
- A failed external-request test demonstrating that outbound traffic is blocked.
- A repeatable verification script.

Example checks:

```bash
# Inspect listening services
ss -tulpn

# Inspect active connections during a task
ss -tpn

# Run the project-specific verification script
bash scripts/verify_offline_mode.sh
```

Use a controlled test environment and obtain team approval before changing firewall rules.

---

## 13. Team Responsibilities

| Role | Responsibilities |
|---|---|
| Team lead | Scope, integration, presentation, submission |
| Backend engineer | APIs, task state, orchestration, storage |
| AI/ML engineer | Model serving, prompts, OCR, vision, retrieval |
| Frontend engineer | Dashboard, upload flow, progress, outputs |
| Security/DevOps engineer | Docker, offline mode, sandbox, network evidence |
| Documentation/demo owner | Test data, scripts, screenshots, pitch, README |

Each teammate should create a feature branch and open a pull request for review. Avoid directly pushing unfinished changes to `main`.

### Suggested branch names

```text
feature/document-ingestion
feature/agent-orchestrator
feature/knowledge-retrieval
feature/frontend-dashboard
feature/security-monitor
feature/demo-workflow
```

---

## 14. Development Roadmap

### Phase 1 — Foundation

- [ ] Repository and development conventions
- [ ] FastAPI health endpoint
- [ ] React dashboard shell
- [ ] Local file storage
- [ ] Basic logging

### Phase 2 — Document pipeline

- [ ] PDF and image upload
- [ ] OCR extraction
- [ ] Page and source tracking
- [ ] Text and table extraction
- [ ] Document preview

### Phase 3 — Local AI and knowledge base

- [ ] Local model adapter
- [ ] Embedding generation
- [ ] Vector retrieval
- [ ] SOP/manual ingestion
- [ ] Citation display

### Phase 4 — Agent and deliverables

- [ ] Task planning
- [ ] Tool execution
- [ ] Human approval checkpoint
- [ ] DOCX generation
- [ ] XLSX and PDF generation
- [ ] Coding-task sandbox

### Phase 5 — Sovereignty proof and polish

- [ ] Outbound traffic block
- [ ] Network monitor
- [ ] Complete audit trail
- [ ] End-to-end tests
- [ ] Demo script
- [ ] Final presentation

---

## 15. Evaluation and Demo Checklist

Before presenting, verify:

- [ ] The application runs without internet access.
- [ ] At least one scanned or image-based document is processed.
- [ ] At least two task types are demonstrated.
- [ ] A local knowledge-base document is retrieved.
- [ ] The agent shows an intermediate plan and progress.
- [ ] At least one DOCX, XLSX, or PDF deliverable is generated.
- [ ] Generated output includes source references or evidence.
- [ ] A coding task runs inside a restricted sandbox, if implemented.
- [ ] Network logs visibly prove local-only operation.
- [ ] No real confidential data is included in the public repository.
- [ ] The system can recover from OCR, model, and file errors.
- [ ] Team members can explain their components.

### Five-minute demo flow

1. Explain the confidentiality problem.
2. Show the local-only architecture.
3. Upload a sample scanned inspection report.
4. Start the agentic workflow.
5. Show OCR and source retrieval.
6. Show the generated approval note and action tracker.
7. Open audit and network logs.
8. Explain how the same workbench supports a second task type.

---

## 16. Contribution Guidelines

1. Create a branch from `main`.
2. Make one focused change at a time.
3. Add or update tests.
4. Run formatting and tests locally.
5. Update documentation when behavior changes.
6. Do not commit secrets or confidential files.
7. Open a pull request with screenshots for UI changes.
8. Ask at least one teammate to review before merging.

### Commit message examples

```text
feat: add scanned PDF ingestion
feat: add local knowledge retrieval
fix: preserve page numbers in OCR output
test: add task orchestration tests
docs: update offline deployment guide
```

### Local quality checks

```bash
# Backend tests
pytest

# Frontend checks
npm run lint
npm run test

# Build the frontend
npm run build
```

Use the commands that exist in the current implementation and keep this section synchronized with the project scripts.

---

## 17. License

This repository is intended for the SIH 2026 project team. Add the final license only after the team agrees on the permitted use and ownership terms. Do not publish confidential MRPL data, proprietary documents, or restricted model files.

---

## Official Problem Statement Reference

- Official portal: `https://sih.gov.in/sih2026PS`
- Organization: Mangalore Refinery and Petrochemicals Limited (MRPL)
- Title: Sovereign On-Premise Agentic AI Workbench using Open-Weight Multimodal LLMs for Confidential Industrial Work
- Category: Software
- Theme: Smart Automation
- Screenshot-reported ID: 26117

The team should confirm the final official problem statement ID and wording directly on the SIH portal before preparing the final submission.

---

**Status:** Planning and active development  
**Repository:** `jeevanhs06/SIH2026-MRPL-SovereignAI-Workbench`  
**Last updated:** September 18, 2026
