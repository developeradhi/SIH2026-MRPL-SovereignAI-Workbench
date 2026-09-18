# SovereignAI Workbench

## SIH 2026 | MRPL | Smart Automation

> **Problem Statement:** Sovereign On-Premise Agentic AI Workbench using Open-Weight Multimodal LLMs for Confidential Industrial Work  
> **Organization:** Mangalore Refinery and Petrochemicals Limited (MRPL)  
> **Category:** Software  
> **Theme:** Smart Automation  
> **Problem Statement ID shown in the provided SIH screenshot:** `26117`  
> **Official reference:** https://sih.gov.in/sih2026PS

SovereignAI Workbench is an on-premise, local-first, multimodal and agentic AI platform for processing confidential industrial documents. It can read scanned PDFs, handwritten notes, photographs, engineering drawings and office documents; search a local knowledge base; execute multi-step tasks; and generate useful deliverables such as approval notes, reports, spreadsheets and code without sending data to external services.

> **Submission note:** Verify the final problem statement ID and exact wording on the SIH portal before submitting. Never place confidential MRPL documents, proprietary data, credentials or private correspondence in this public repository.

---

## Contents

- [1. Project Vision](#1-project-vision)
- [2. Problem Understanding](#2-problem-understanding)
- [3. Proposed Solution](#3-proposed-solution)
- [4. Goals and Non-Goals](#4-goals-and-non-goals)
- [5. Complete Requirements](#5-complete-requirements)
- [6. Functional Requirements](#6-functional-requirements)
- [7. Non-Functional Requirements](#7-non-functional-requirements)
- [8. User Roles](#8-user-roles)
- [9. End-to-End Workflow](#9-end-to-end-workflow)
- [10. Demonstration Use Cases](#10-demonstration-use-cases)
- [11. System Architecture](#11-system-architecture)
- [12. Technology Stack](#12-technology-stack)
- [13. Repository Structure](#13-repository-structure)
- [14. Hardware and Software Requirements](#14-hardware-and-software-requirements)
- [15. Installation Guide](#15-installation-guide)
- [16. Configuration](#16-configuration)
- [17. Development Guide](#17-development-guide)
- [18. Knowledge Base Setup](#18-knowledge-base-setup)
- [19. Agent and Tool Design](#19-agent-and-tool-design)
- [20. Deliverable Generation](#20-deliverable-generation)
- [21. Offline and Security Design](#21-offline-and-security-design)
- [22. API Specification](#22-api-specification)
- [23. Testing Strategy](#23-testing-strategy)
- [24. Demo Plan](#24-demo-plan)
- [25. Acceptance Criteria](#25-acceptance-criteria)
- [26. Team Plan](#26-team-plan)
- [27. Roadmap](#27-roadmap)
- [28. Troubleshooting](#28-troubleshooting)
- [29. Contribution Rules](#29-contribution-rules)
- [30. Responsible Use](#30-responsible-use)
- [31. License and Data Policy](#31-license-and-data-policy)

---

## 1. Project Vision

Industrial organizations have large collections of confidential documents and need reliable assistance with document-heavy work. Conventional chatbots usually answer a single question, have limited understanding of images and scans, depend on cloud APIs, and do not create complete business deliverables.

Our vision is to provide a **private digital workbench** where an authorized user can submit an industrial task and receive a traceable result:

```text
User request + local documents
          ↓
Task planning and model selection
          ↓
OCR, vision, parsing and local retrieval
          ↓
Agentic reasoning and tool execution
          ↓
Validation and human review
          ↓
DOCX / XLSX / PDF / code deliverable
          ↓
Audit trail and sovereignty proof
```

---

## 2. Problem Understanding

The system must satisfy the following challenge:

- Search and reason over internal documents.
- Handle more than plain text: scanned PDFs, handwritten notes, engineering drawings and photographs.
- Use OCR and vision models locally.
- Continue through a task instead of stopping after a single answer.
- Produce real files and outputs, not only chat messages.
- Ground its work in local manuals, SOPs and past correspondence.
- Run on a workstation or server without external calls.
- Demonstrate through logs or a visible network monitor that no data leaves the environment.
- Select appropriate local models for different task types and available hardware.

### Core example

A user uploads a scanned inspection report. The system reads the report, extracts findings, retrieves the relevant local SOP, compares the findings with the procedure, prepares an approval note, generates an action tracker, and records every step.

---

## 3. Proposed Solution

The platform consists of the following modules:

1. **Workbench UI** — document upload, task creation, progress, outputs and logs.
2. **API gateway** — authentication, validation, task APIs and file APIs.
3. **Document pipeline** — OCR, image preprocessing, table extraction and parsing.
4. **Local model gateway** — a consistent interface for local LLM, vision and embedding models.
5. **Agent orchestrator** — planning, tool selection, execution, retries and checkpoints.
6. **Knowledge base** — local indexing and retrieval of manuals, SOPs and templates.
7. **Output generator** — DOCX, XLSX, PDF, JSON and code generation.
8. **Sandbox** — restricted execution for generated code.
9. **Security layer** — offline enforcement, network monitoring, audit logs and access control.

The architecture is model-agnostic. The implementation must be able to use smaller models when GPU hardware is not available and larger models when additional resources are present.

---

## 4. Goals and Non-Goals

### Goals

- Deliver a working local prototype for SIH evaluation.
- Demonstrate at least two different task types.
- Process multimodal sample documents.
- Use open-weight models running locally.
- Retrieve information from a local knowledge base.
- Generate at least one useful business document.
- Show complete task and network logs.
- Provide reproducible setup and demo scripts.

### Non-goals for the first MVP

- Fully replacing a certified industrial approval system.
- Autonomous final approval of safety-critical decisions.
- Production-scale deployment across every MRPL site.
- Training a foundation model from scratch.
- Uploading real confidential documents to this repository.
- Allowing unrestricted shell access or unrestricted code execution.

---

## 5. Complete Requirements

### 5.1 Required MVP capabilities

- [ ] Upload PDF, image, DOCX, XLSX and text files.
- [ ] Detect whether a PDF contains selectable text or scanned pages.
- [ ] Run local OCR on scanned pages.
- [ ] Preserve page numbers and document references.
- [ ] Process images and photographs using a local vision model.
- [ ] Extract text, tables, metadata and basic structured fields.
- [ ] Index local manuals, SOPs and templates.
- [ ] Perform semantic retrieval from the local knowledge base.
- [ ] Create and display an agent plan before execution.
- [ ] Execute multi-step tasks with visible progress.
- [ ] Use local tools for calculations, file operations and retrieval.
- [ ] Generate DOCX approval notes.
- [ ] Generate XLSX action trackers.
- [ ] Generate PDF summaries.
- [ ] Generate JSON output for integrations.
- [ ] Support a restricted coding task if code generation is included.
- [ ] Require human review before finalizing sensitive deliverables.
- [ ] Record all task, model, tool, file and security events.
- [ ] Prove that external network access is disabled.
- [ ] Run using public sample data without proprietary documents.

### 5.2 Recommended enhanced capabilities

- [ ] Handwriting confidence scores.
- [ ] Table and diagram understanding.
- [ ] Multiple local model profiles.
- [ ] Model auto-selection based on task type and hardware.
- [ ] User and role management.
- [ ] Versioned prompts and templates.
- [ ] Document-level access permissions.
- [ ] Human correction of OCR output.
- [ ] Citation and evidence panel.
- [ ] Replay of completed tasks.
- [ ] Exportable audit package.
- [ ] LoRA or organization-specific adapters in a controlled environment.
- [ ] Local multilingual support.

---

## 6. Functional Requirements

### FR-01: User authentication

The system shall authenticate users locally and enforce role-based permissions.

### FR-02: File upload

The system shall accept supported files, validate file type and size, calculate a checksum, store the original safely, and create metadata.

### FR-03: Document extraction

The system shall determine the correct extraction path: direct text extraction, OCR, image processing, table extraction or multimodal analysis.

### FR-04: Knowledge ingestion

An administrator shall be able to add local manuals, SOPs, templates and approved sample correspondence to the knowledge base.

### FR-05: Retrieval

The system shall return relevant chunks with source file, page number, score and text evidence.

### FR-06: Task planning

The agent shall convert a user request into a visible, ordered plan with tools and expected outputs.

### FR-07: Task execution

The agent shall execute steps, save intermediate results, retry safe failures and stop for human review when required.

### FR-08: Model selection

The platform shall support configurable local models for text, vision and embeddings and select a suitable profile for a task.

### FR-09: Deliverable generation

The platform shall create files from structured results and templates while preserving traceability to the input documents.

### FR-10: Human review

Users shall be able to inspect extracted facts, citations, warnings and generated files before finalization.

### FR-11: Audit logging

The system shall log who performed an action, when it occurred, what input was used, what model/tool ran, what output was produced and whether an error occurred.

### FR-12: Sovereignty verification

The system shall display local network status and record blocked or attempted outbound connections.

### FR-13: Failure handling

The system shall show actionable errors for unsupported files, OCR failures, unavailable models, invalid outputs and tool timeouts.

---

## 7. Non-Functional Requirements

### Security

- No external AI APIs.
- No telemetry or analytics that transmit documents.
- Secrets supplied through environment variables or a secret manager.
- Encryption at rest and in transit where appropriate.
- Least-privilege service accounts.
- Sandboxed generated code.
- Complete audit trail.

### Privacy

- Process data locally.
- Support retention and deletion policies.
- Avoid copying sensitive content into application logs.
- Mask secrets and personal data in error messages.

### Reliability

- Recoverable task state.
- Idempotent ingestion and task operations.
- Retry policies for safe operations.
- Health endpoints for all services.

### Performance targets for the MVP

- Upload acknowledgement: under 2 seconds for normal files.
- Text extraction: visible progress and no silent blocking.
- First task update: under 10 seconds after task start.
- The interface must remain responsive during processing.
- Exact inference time depends on hardware and model size.

### Usability

- Clear task status: queued, running, waiting for review, completed or failed.
- Source citations next to extracted facts.
- Downloadable outputs.
- Useful error messages.
- Demo operation possible by a non-developer.

### Maintainability

- Modular services.
- Typed API schemas.
- Automated tests.
- Configuration through environment variables.
- Documentation for every public module.

---

## 8. User Roles

| Role | Permissions |
|---|---|
| Viewer | View approved tasks and outputs |
| Operator | Upload documents and run approved task templates |
| Reviewer | Inspect evidence and approve or reject outputs |
| Knowledge Administrator | Add, remove and re-index local knowledge |
| System Administrator | Configure models, security and users |
| Auditor | View security and audit logs without changing data |

For the MVP, role handling may be simplified, but the permission boundaries must be documented.

---

## 9. End-to-End Workflow

### Document-to-deliverable workflow

1. User signs in.
2. User uploads a document.
3. Backend validates the file and calculates its checksum.
4. The document pipeline identifies the content type.
5. OCR, parser or vision processing extracts content.
6. User reviews extraction if confidence is low.
7. User chooses a task template or enters a task request.
8. Agent planner creates an execution plan.
9. Retrieval tool searches local manuals and SOPs.
10. Agent analyzes the input and evidence.
11. Agent creates a structured result.
12. Output generator creates DOCX, XLSX or PDF.
13. Reviewer checks facts, evidence and warnings.
14. System finalizes the output.
15. Audit and sovereignty logs are exported.

### Task state machine

```text
CREATED → QUEUED → RUNNING → WAITING_FOR_REVIEW → COMPLETED
                         │                    │
                         ├→ FAILED            └→ REJECTED
                         └→ CANCELLED
```

---

## 10. Demonstration Use Cases

### Use Case A: Inspection report to approval note

**Input:** Scanned inspection report with typed text, tables and handwritten annotations.

**Steps:**

1. OCR the report.
2. Extract equipment, date, findings, severity and recommendations.
3. Retrieve relevant SOP sections.
4. Compare findings with the SOP.
5. Highlight missing or uncertain information.
6. Generate a DOCX approval note.
7. Generate an XLSX action tracker.
8. Generate a PDF summary.
9. Show source pages and audit logs.

### Use Case B: Engineering drawing and specification analysis

**Input:** Public sample drawing and technical specification.

**Steps:**

1. Render drawing pages locally.
2. Use a local vision model to identify labels and relevant regions.
3. Extract requirements from the specification.
4. Compare drawing information with the requirements.
5. Produce a structured discrepancy report.

### Use Case C: Local coding assistant

**Input:** Public sample specification or scanned requirement document.

**Steps:**

1. Extract requirements.
2. Generate a Python code skeleton.
3. Generate tests.
4. Run inside a restricted sandbox.
5. Display test results and generated files.
6. Block network access during execution.

### Use Case D: Compliance review

**Input:** Local policy, checklist and sample audit evidence.

**Output:** Compliance matrix, missing evidence list and draft report with citations.

---

## 11. System Architecture

```text
┌──────────────────────────────────────────────────────────────┐
│                         Web Workbench                         │
│ Upload │ Task Builder │ Progress │ Evidence │ Outputs │ Logs │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│                      API and Auth Layer                       │
│ FastAPI │ Validation │ RBAC │ File API │ Task API │ WebSocket│
└─────────────┬────────────────────┬───────────────────────────┘
              │                    │
┌─────────────▼──────────┐ ┌───────▼──────────────────────────┐
│ Agent Orchestrator      │ │ Multimodal Document Pipeline      │
│ Planner │ State │ Tools │ │ OCR │ Vision │ PDF │ Tables │ Text │
└─────────────┬──────────┘ └───────┬──────────────────────────┘
              │                    │
┌─────────────▼────────────────────▼───────────────────────────┐
│                         Local Model Gateway                   │
│ Text LLM │ Vision LLM │ Embeddings │ Reranker │ Model Router │
└─────────────┬────────────────────┬──────────────────────────┘
              │                    │
┌─────────────▼──────────┐ ┌───────▼──────────────────────────┐
│ Local Knowledge Base    │ │ Storage, Outputs and Audit        │
│ Files │ Chunks │ Vector │ │ SQLite/Postgres │ Files │ Events   │
└────────────────────────┘ └───────────────────────────────────┘
              │
┌─────────────▼────────────────────────────────────────────────┐
│                 Offline Security and Monitoring               │
│ Firewall │ Network Monitor │ Sandboxed Code │ Integrity Logs │
└──────────────────────────────────────────────────────────────┘
```

### Architecture rules

- The model gateway is the only component that can call model services.
- Model services must be local addresses or Unix sockets.
- The knowledge base must never require a cloud endpoint.
- The code runner must run with network access disabled.
- All important state transitions must be auditable.

---

## 12. Technology Stack

| Layer | MVP choice | Alternatives |
|---|---|---|
| Frontend | React + TypeScript + Vite | Vue, Svelte |
| API | Python + FastAPI | Flask |
| Database | SQLite | PostgreSQL |
| Local LLM runtime | Ollama or llama.cpp | vLLM in an isolated environment |
| Text model | Locally available open-weight instruct model | Another compatible model |
| Vision | Local vision-language model | Local OCR plus image model |
| OCR | Tesseract or PaddleOCR | EasyOCR |
| PDF | PyMuPDF | pypdf, pdfplumber |
| DOCX | python-docx | LibreOffice headless |
| XLSX | openpyxl | pandas plus xlsxwriter |
| PDF output | ReportLab | LibreOffice headless |
| Embeddings | Sentence Transformers | Local embedding runtime |
| Vector store | FAISS or Chroma | Qdrant on-premise |
| Queue | FastAPI background tasks for MVP | Celery + Redis/RabbitMQ |
| Sandbox | Docker with no network | gVisor or restricted subprocess |
| Deployment | Docker Compose | Kubernetes |
| Testing | Pytest, Vitest/Playwright | Jest |

### Model policy

The exact model is configurable. Select based on:

- Available CPU, RAM, GPU and VRAM.
- Required context length.
- OCR and vision capability.
- Inference speed.
- License suitability.
- Offline availability.
- Quality on the project sample set.

Do not download models during the final offline demo.

---

## 13. Repository Structure

```text
.
├── README.md
├── .env.example
├── .gitignore
├── LICENSE
├── docker-compose.yml
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── api/
│   │   │   ├── auth.py
│   │   │   ├── documents.py
│   │   │   ├── tasks.py
│   │   │   ├── knowledge.py
│   │   │   └── security.py
│   │   ├── agents/
│   │   │   ├── planner.py
│   │   │   ├── executor.py
│   │   │   ├── state.py
│   │   │   └── tools.py
│   │   ├── documents/
│   │   │   ├── ingestion.py
│   │   │   ├── ocr.py
│   │   │   ├── vision.py
│   │   │   ├── tables.py
│   │   │   └── parsers.py
│   │   ├── models/
│   │   │   ├── gateway.py
│   │   │   ├── profiles.py
│   │   │   └── prompts.py
│   │   ├── knowledge_base/
│   │   │   ├── indexer.py
│   │   │   ├── retriever.py
│   │   │   └── citations.py
│   │   ├── outputs/
│   │   │   ├── docx.py
│   │   │   ├── xlsx.py
│   │   │   ├── pdf.py
│   │   │   └── json.py
│   │   ├── security/
│   │   │   ├── audit.py
│   │   │   ├── network.py
│   │   │   ├── sandbox.py
│   │   │   └── integrity.py
│   │   └── storage/
│   │       ├── database.py
│   │       ├── files.py
│   │       └── repositories.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── types/
│   │   └── App.tsx
│   ├── package.json
│   └── Dockerfile
├── knowledge_base/
│   ├── manuals/
│   ├── sops/
│   ├── templates/
│   └── sample_documents/
├── data/
│   ├── inputs/.gitkeep
│   ├── outputs/.gitkeep
│   ├── vector_store/.gitkeep
│   └── audit/.gitkeep
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── e2e/
│   └── fixtures/
├── scripts/
│   ├── bootstrap.sh
│   ├── ingest_knowledge.py
│   ├── run_demo.py
│   ├── run_tests.sh
│   └── verify_offline_mode.sh
├── deployment/
│   ├── docker-compose.dev.yml
│   ├── docker-compose.prod.yml
│   └── firewall/
└── docs/
    ├── ARCHITECTURE.md
    ├── API.md
    ├── SETUP.md
    ├── SECURITY.md
    ├── DEMO_SCRIPT.md
    └── TROUBLESHOOTING.md
```

The directories describe the target architecture. Add files incrementally and keep the structure synchronized with implementation.

---

## 14. Hardware and Software Requirements

### Minimum development machine

- 64-bit operating system.
- 4 CPU cores.
- 16 GB RAM.
- 50 GB free disk space, excluding model storage.
- Python 3.10+.
- Node.js 20+.
- Docker 24+ and Docker Compose.
- Internet access only during initial dependency and model preparation.

### Recommended demo machine

- 8 or more CPU cores.
- 32 GB RAM.
- NVIDIA GPU with adequate VRAM, if available.
- 100 GB or more free SSD space.
- Linux or a Linux virtual machine.
- Local network isolation or outbound firewall rules.

### CPU-only fallback

- Use a smaller quantized model.
- Use OCR plus text processing when vision inference is too slow.
- Reduce image resolution and document batch size.
- Use a smaller embedding model.
- Pre-index all demonstration knowledge before the event.

### Required software

- Git.
- Python and virtual environment support.
- Node.js and npm.
- Docker and Docker Compose.
- OCR engine.
- Local model runtime.
- A PDF viewer and office document viewer for checking outputs.

---

## 15. Installation Guide

### 15.1 Clone the repository

```bash
git clone https://github.com/jeevanhs06/SIH2026-MRPL-SovereignAI-Workbench.git
cd SIH2026-MRPL-SovereignAI-Workbench
```

### 15.2 Create local configuration

```bash
cp .env.example .env
```

Never commit `.env`.

### 15.3 Backend setup

```bash
cd backend
python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows PowerShell
# .venv\Scripts\Activate.ps1

pip install --upgrade pip
pip install -r requirements.txt
```

### 15.4 Frontend setup

```bash
cd frontend
npm install
```

### 15.5 Install local OCR

Install the selected OCR engine on the host or include it in the backend container. Verify it:

```bash
tesseract --version
```

### 15.6 Prepare the local model runtime

Install the selected local runtime and download compatible models while internet access is available. Record model names, checksums, versions and licenses in `docs/MODELS.md`. Test inference before going offline.

### 15.7 Start services locally

```bash
# Backend
cd backend
source .venv/bin/activate
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

# Frontend in another terminal
cd frontend
npm run dev
```

Expected local endpoints:

- Frontend: `http://127.0.0.1:5173`
- Backend: `http://127.0.0.1:8000`
- API documentation: `http://127.0.0.1:8000/docs`

### 15.8 Docker setup

```bash
docker compose up --build
```

The production-like compose file must use local volumes, health checks, restricted permissions and no unnecessary outbound network access.

---

## 16. Configuration

Create `.env` from `.env.example`:

```env
APP_ENV=development
APP_NAME=SovereignAI-Workbench
API_HOST=127.0.0.1
API_PORT=8000
FRONTEND_ORIGIN=http://127.0.0.1:5173

DATABASE_URL=sqlite:///./data/workbench.db
INPUT_DIR=./data/inputs
OUTPUT_DIR=./data/outputs
TEMP_DIR=./data/tmp
AUDIT_LOG_PATH=./data/audit/audit.jsonl

MODEL_RUNTIME=local
MODEL_BASE_URL=http://127.0.0.1:11434
TEXT_MODEL=local-text-model
VISION_MODEL=local-vision-model
EMBEDDING_MODEL=local-embedding-model
VECTOR_STORE_PATH=./data/vector_store

OFFLINE_MODE=true
ALLOW_EXTERNAL_NETWORK=false
MAX_UPLOAD_MB=100
CODE_EXECUTION_TIMEOUT_SECONDS=30
REQUIRE_HUMAN_REVIEW=true
LOG_LEVEL=INFO
```

### Configuration rules

- `ALLOW_EXTERNAL_NETWORK` must remain `false` for the demo.
- Bind services to localhost unless remote access is explicitly required.
- Do not hard-code passwords, API keys or tokens.
- Validate all model endpoints against an allowlist.
- Treat model files and prompts as versioned project assets.

---

## 17. Development Guide

### Branching

```bash
git checkout main
git pull origin main
git checkout -b feature/document-ingestion
```

Suggested branches:

```text
feature/document-ingestion
feature/ocr-pipeline
feature/local-model-gateway
feature/knowledge-retrieval
feature/agent-orchestrator
feature/output-generation
feature/frontend-dashboard
feature/security-monitor
feature/demo-workflow
```

### Development order

1. Health endpoint and configuration.
2. File upload and local storage.
3. Text extraction and OCR.
4. Local model adapter.
5. Knowledge indexing and retrieval.
6. Agent planning and task execution.
7. DOCX/XLSX/PDF generation.
8. Frontend progress and evidence views.
9. Offline controls and audit proof.
10. End-to-end demo and documentation.

### Coding standards

- Use type hints in Python.
- Use Pydantic schemas for API input and output.
- Keep business logic outside route handlers.
- Add tests for every new processing path.
- Avoid logging document contents by default.
- Use structured errors and stable error codes.
- Document assumptions and limitations.

### Useful commands

```bash
# Backend tests
pytest -q

# Backend formatting/linting, when configured
ruff check .

# Frontend lint and tests
npm run lint
npm run test

# Frontend production build
npm run build

# Docker status
docker compose ps
```

---

## 18. Knowledge Base Setup

### Supported knowledge sources

- Public sample SOPs.
- Public technical manuals.
- Public document templates.
- Synthetic inspection reports.
- Synthetic correspondence.
- Public engineering sample documents.

### Ingestion process

1. Copy approved documents into `knowledge_base/`.
2. Validate file type and checksum.
3. Extract text, tables and page metadata.
4. Split content into meaningful chunks.
5. Generate embeddings locally.
6. Store vectors and metadata locally.
7. Run retrieval quality tests.
8. Record source version and ingestion time.

### Chunk metadata

Each chunk should include:

```json
{
  "document_id": "doc-001",
  "filename": "sample_sop.pdf",
  "page": 4,
  "section": "Inspection frequency",
  "checksum": "sha256:...",
  "text": "...",
  "embedding_model": "local-embedding-model"
}
```

### Retrieval requirements

- Return source filename and page number.
- Return evidence text.
- Show retrieval score or rank.
- Never present retrieved text as an approved instruction without human review.
- Make it clear when the answer is based on general model knowledge rather than the knowledge base.

---

## 19. Agent and Tool Design

### Agent loop

```text
Receive task
   ↓
Validate input and permissions
   ↓
Create plan
   ↓
Select model and tools
   ↓
Execute one step
   ↓
Validate result
   ├── retry or ask for clarification
   └── continue
   ↓
Generate deliverable
   ↓
Request human review
   ↓
Finalize and audit
```

### Approved initial tools

- `extract_document_text`
- `run_ocr`
- `analyze_image`
- `retrieve_knowledge`
- `calculate`
- `create_docx`
- `create_xlsx`
- `create_pdf`
- `write_json`
- `run_sandboxed_code`
- `record_audit_event`

### Tool safety rules

- Validate tool arguments.
- Restrict file paths to approved directories.
- Reject path traversal.
- Apply timeouts and output-size limits.
- Do not allow unrestricted shell commands.
- Disable network access for code execution.
- Require review for high-impact outputs.
- Keep tool calls visible in the UI.

### Agent result format

```json
{
  "task_id": "task-001",
  "status": "waiting_for_review",
  "summary": "Inspection findings extracted and compared with the sample SOP.",
  "facts": [],
  "warnings": [],
  "citations": [],
  "outputs": [],
  "events": []
}
```

---

## 20. Deliverable Generation

### DOCX approval note

Must contain:

- Document title and generated date.
- Subject and reference document.
- Extracted findings.
- Relevant evidence and page references.
- Recommendations.
- Risks and uncertainties.
- Required approvals.
- Human-review status.
- System-generated disclaimer.

### XLSX action tracker

Suggested columns:

```text
Action ID | Finding | Severity | Responsible Role | Due Date | Evidence Page | Status | Reviewer
```

### PDF report

Must contain:

- Executive summary.
- Input document metadata.
- Processing steps.
- Findings.
- Evidence and citations.
- Warnings and confidence.
- Generated-by and model version.
- Audit reference.

### Generated code

Must contain:

- README with usage instructions.
- Source files.
- Tests.
- Dependency list.
- Execution result.
- Sandbox restrictions.
- No secret values.

---

## 21. Offline and Security Design

### Sovereignty definition

For this project, sovereignty means that confidential input data, model inference, embeddings, retrieval and output generation remain inside the controlled local environment. A statement in the README is not enough; the demo must provide evidence.

### Required controls

- Use local model endpoints only.
- Disable outbound network access at the host/container level.
- Use an allowlist for local services.
- Disable dependency telemetry where possible.
- Store all inputs and outputs on local volumes.
- Keep audit logs append-only for the demo.
- Hash important files.
- Prevent documents from appearing in exception traces.
- Restrict administrator operations.
- Use a separate synthetic dataset for public development.

### Network verification

Before the demo:

```bash
# Show listening services
ss -tulpn

# Show active TCP connections
ss -tpn

# Inspect container network configuration
docker network ls
docker inspect <container-name>

# Run the project verification script
bash scripts/verify_offline_mode.sh
```

The verification script should:

1. Check `OFFLINE_MODE=true`.
2. Check `ALLOW_EXTERNAL_NETWORK=false`.
3. Verify model endpoints resolve to local addresses.
4. Check firewall or container network rules.
5. Run a complete sample task.
6. Save network and application logs.
7. Fail if an unexpected external connection is detected.

### Security threat model

| Threat | Mitigation |
|---|---|
| Document exfiltration | No outbound network; local model gateway |
| Prompt injection | Treat documents as untrusted; tool allowlist; review gates |
| Malicious upload | File validation, size limits, malware scanning where available |
| Path traversal | Canonicalize and restrict paths |
| Unsafe generated code | Sandboxed execution with no network |
| Hallucinated facts | Citations, confidence, validation and human review |
| Unauthorized access | Local authentication and role permissions |
| Log leakage | Redaction and minimal content logging |
| Model supply-chain risk | Record source, checksum, version and license |

---

## 22. API Specification

### Health

```http
GET /health
```

### Upload document

```http
POST /api/documents
Content-Type: multipart/form-data
```

Response should include:

```json
{
  "document_id": "doc-001",
  "filename": "inspection_report.pdf",
  "status": "uploaded",
  "sha256": "..."
}
```

### Create task

```http
POST /api/tasks
Content-Type: application/json
```

```json
{
  "name": "Inspection report to approval note",
  "document_ids": ["doc-001"],
  "template": "inspection_to_approval",
  "require_human_review": true
}
```

### Task status

```http
GET /api/tasks/{task_id}
```

### Task events

```http
GET /api/tasks/{task_id}/events
```

### Generated outputs

```http
GET /api/tasks/{task_id}/outputs
```

### Knowledge indexing

```http
POST /api/knowledge/index
```

### Network status

```http
GET /api/security/network-status
```

### API rules

- Validate all request bodies.
- Return stable error schemas.
- Authenticate non-public endpoints.
- Add request IDs for tracing.
- Never return secrets.
- Never expose arbitrary filesystem paths.

---

## 23. Testing Strategy

### Unit tests

Test:

- File validation.
- Text extraction.
- OCR normalization.
- Chunking.
- Retrieval metadata.
- Agent state transitions.
- Prompt construction.
- Output generation.
- Path restrictions.
- Audit event creation.

### Integration tests

Test:

- Upload to extraction.
- Extraction to indexing.
- Retrieval to agent response.
- Agent to DOCX/XLSX/PDF generation.
- API authentication and permissions.
- Offline model gateway.

### End-to-end test

Run the complete inspection-report workflow with a synthetic document and verify:

- Expected extracted fields exist.
- Expected citations exist.
- Output files are created.
- Human review is required.
- Audit events are present.
- No external connections occur.

### Quality evaluation

Create a small evaluation set with expected answers for:

- OCR accuracy.
- Field extraction.
- Retrieval relevance.
- Citation correctness.
- Output completeness.
- Task completion success.
- Processing time.

Do not evaluate only on fluent responses. Evaluate evidence and deliverable correctness.

---

## 24. Demo Plan

### Five-minute presentation

1. Introduce the confidentiality and document-processing problem.
2. Show the architecture and local-only model gateway.
3. Upload a synthetic scanned inspection report.
4. Start the agentic workflow.
5. Show OCR, evidence and SOP retrieval.
6. Show generated DOCX and XLSX files.
7. Show task timeline and audit logs.
8. Show blocked outbound network evidence.
9. Demonstrate the second task type.
10. Explain scalability and limitations.

### Demo preparation checklist

- [ ] Models are downloaded and tested.
- [ ] No internet is needed during the demo.
- [ ] Sample files are synthetic or publicly shareable.
- [ ] Knowledge base is indexed.
- [ ] Output templates are tested.
- [ ] Firewall/network rules are tested.
- [ ] A backup recording or screenshots exist.
- [ ] The team has a CPU-only fallback.
- [ ] All services have health checks.
- [ ] The demo can be reset quickly.

---

## 25. Acceptance Criteria

The MVP is considered successful when:

1. It runs on a local workstation or server.
2. It accepts at least one scanned PDF and one image.
3. It performs OCR or local multimodal extraction.
4. It retrieves relevant content from a local knowledge base.
5. It executes a multi-step task.
6. It supports at least two task types.
7. It generates a real DOCX, XLSX or PDF deliverable.
8. It shows intermediate progress and final status.
9. It provides citations or evidence references.
10. It records audit events.
11. It demonstrates blocked or absent external calls.
12. It handles at least one failure safely.
13. It can be set up from the repository documentation.
14. It does not require proprietary confidential data for the demonstration.

---

## 26. Team Plan

| Role | Main responsibility | Deliverables |
|---|---|---|
| Project lead | Scope, integration and submission | Milestones, pitch and final integration |
| Backend lead | FastAPI, storage and APIs | Stable backend and API documentation |
| AI/ML lead | OCR, models, prompts and retrieval | Model gateway and evaluation set |
| Agent lead | Planning, tools and state machine | Agent workflow and task logs |
| Frontend lead | Workbench user interface | Upload, progress, evidence and outputs |
| Security/DevOps lead | Docker, network isolation and sandbox | Offline proof and deployment scripts |
| Documentation lead | README, demo and presentation | Setup, screenshots, demo script and pitch |

### Team working rules

- Use small pull requests.
- Review each other's code.
- Keep setup instructions current.
- Do not commit confidential documents.
- Keep a known-good demo branch or tag.
- Record model and dependency versions.
- Assign one person to run the final offline rehearsal.

---

## 27. Roadmap

### Phase 1: Foundation

- [ ] Repository conventions.
- [ ] Environment configuration.
- [ ] Backend health endpoint.
- [ ] Frontend shell.
- [ ] Local storage.

### Phase 2: Multimodal ingestion

- [ ] PDF parser.
- [ ] Image upload.
- [ ] OCR pipeline.
- [ ] Table extraction.
- [ ] Extraction review screen.

### Phase 3: Local intelligence

- [ ] Text model gateway.
- [ ] Vision model gateway.
- [ ] Embedding service.
- [ ] Vector retrieval.
- [ ] Citations.

### Phase 4: Agentic workflow

- [ ] Task planner.
- [ ] Tool registry.
- [ ] State machine.
- [ ] Retry and failure handling.
- [ ] Human approval gate.

### Phase 5: Deliverables

- [ ] DOCX generator.
- [ ] XLSX generator.
- [ ] PDF generator.
- [ ] Code generation and sandbox.
- [ ] Output preview.

### Phase 6: Security and final demo

- [ ] Offline firewall rules.
- [ ] Network monitor.
- [ ] Audit export.
- [ ] Security tests.
- [ ] Performance testing.
- [ ] Final rehearsal.

---

## 28. Troubleshooting

### Model service is unavailable

- Confirm the local model runtime is running.
- Check the configured local endpoint.
- Verify the model is already downloaded.
- Check RAM/VRAM and model compatibility.
- Use the CPU fallback profile.

### OCR output is poor

- Improve image resolution.
- Deskew and rotate pages.
- Apply contrast and denoising.
- Try a different OCR language configuration.
- Show low-confidence fields for manual correction.

### Retrieval returns irrelevant results

- Check chunk size and overlap.
- Verify embeddings were generated with the expected model.
- Add section and page metadata.
- Improve the retrieval query.
- Add a reranker or keyword filter.

### Output file is empty or corrupt

- Validate the structured intermediate result.
- Check template paths.
- Confirm write permissions.
- Test the output generator independently.
- Add a post-generation file validation step.

### External network appears in logs

- Stop the demo.
- Identify the process and destination.
- Disable the dependency's telemetry.
- Update the allowlist.
- Re-run offline verification before continuing.

### Docker service cannot access a model

- Confirm the model service is on the expected local Docker network.
- Use the service name inside Docker, not `localhost`.
- Confirm the model volume is mounted.
- Verify the container health check.

---

## 29. Contribution Rules

1. Create a feature branch.
2. Make a focused change.
3. Add tests and documentation.
4. Run local quality checks.
5. Do not commit `.env`, secrets, model weights or confidential documents.
6. Open a pull request with a clear description.
7. Request at least one review.
8. Update the demo if behavior changes.

### Commit examples

```text
feat: add scanned PDF ingestion
feat: add local knowledge retrieval
feat: generate approval note docx
fix: preserve page references in OCR output
test: add offline network verification
docs: expand deployment requirements
```

### Pull request checklist

- [ ] Tests pass.
- [ ] Documentation updated.
- [ ] No secrets or sensitive files included.
- [ ] API changes documented.
- [ ] Security impact considered.
- [ ] Demo path still works.

---

## 30. Responsible Use

This system assists authorized personnel; it does not replace qualified engineers, safety officers, reviewers or approval authorities. AI-generated results must be checked before being used for operational, safety, legal, financial or compliance decisions.

The system must clearly show:

- What was extracted directly from source documents.
- What was inferred by the model.
- What evidence supports the result.
- What information is missing or uncertain.
- What requires human approval.

Never use the public repository or public demo to process real confidential industrial documents.

---

## 31. License and Data Policy

The project team must decide the final license before publication. Until then:

- Do not include proprietary documents.
- Do not include restricted MRPL data.
- Do not include credentials or private keys.
- Do not commit model weights unless their license permits it.
- Record third-party licenses in `docs/THIRD_PARTY_NOTICES.md`.
- Use synthetic or publicly shareable documents for examples.

---

## Official Reference

- SIH portal: https://sih.gov.in/sih2026PS
- Repository: https://github.com/jeevanhs06/SIH2026-MRPL-SovereignAI-Workbench
- Organization: Mangalore Refinery and Petrochemicals Limited (MRPL)
- Category: Software
- Theme: Smart Automation
- Screenshot-reported problem statement ID: `26117`

**Status:** Active development  
**Last updated:** September 18, 2026
