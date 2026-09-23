# Architecture

## 1. Purpose

SovereignAI Workbench is a local-first, multimodal, agentic AI platform for confidential industrial document workflows. The architecture separates user interaction, orchestration, document processing, local AI services, knowledge retrieval, output generation, and security controls.

## 2. Architectural principles

- **Local first:** documents, prompts, embeddings, inference, and outputs remain local.
- **Model replaceability:** application code uses a model gateway rather than a model-specific API.
- **Traceability:** every important action has an event, source reference, or audit record.
- **Human review:** high-impact deliverables are not automatically treated as approved.
- **Least privilege:** tools access only approved directories and operations.
- **Safe degradation:** the system can run in mock mode when OCR, vector search, or model services are unavailable.
- **Composable services:** the MVP is simple enough for local development and can evolve toward production deployment.

## 3. Logical architecture

```text
+----------------------+       +-----------------------------+
| React/TypeScript UI  | <---> | FastAPI API and Auth Layer  |
+----------+-----------+       +---------------+-------------+
           |                                   |
           |                           +-------+--------+
           |                           | Task/Agent     |
           |                           | Orchestrator   |
           |                           +---+--------+---+
           |                               |        |
           |                    +----------+        +-----------+
           |                    |                               |
+----------v-----------+  +-----v----------------+  +-----------v----------+
| Task progress,       |  | Document pipeline    |  | Local model gateway  |
| evidence, outputs,   |  | PDF, OCR, vision,   |  | text, vision,        |
| audit and security   |  | tables and parsing  |  | embeddings           |
+----------------------+  +----------+----------+  +-----------+----------+
                                      |                         |
                              +-------v-------------------------v-----+
                              | Local knowledge, storage and audit   |
                              | files, metadata, vectors, events    |
                              +------------------+--------------------+
                                                 |
                              +------------------v--------------------+
                              | Offline controls and sandbox        |
                              | network policy, code execution      |
                              +---------------------------------------+
```

## 4. Main components

### Frontend

The frontend provides:

- Health and service status.
- Document upload.
- Task creation.
- Task progress and event timeline.
- Evidence and citation display.
- Generated output downloads.
- Offline/security status.

It communicates only with the configured local backend API. It must not include external CDNs, analytics, remote fonts, or hosted AI calls.

### API layer

The FastAPI service owns:

- Request validation.
- Authentication and role checks.
- Document and task endpoints.
- Health checks.
- Security status.
- WebSocket or polling support for progress.

Route handlers should remain thin. Business logic belongs in services and domain modules.

### Document pipeline

The document pipeline selects an extraction path based on file type:

```text
Input file
   ├── TXT/Markdown -> direct text extraction
   ├── text PDF     -> PDF text extraction
   ├── scanned PDF  -> page rendering -> OCR
   ├── image        -> preprocessing -> OCR/vision
   ├── DOCX         -> paragraphs/tables extraction
   └── XLSX         -> workbook/sheet extraction
```

Every extracted fact should retain source filename and page or sheet information when available.

### Model gateway

The model gateway hides runtime-specific details behind stable interfaces:

- `generate_text(prompt, context)`
- `analyze_image(image, prompt)`
- `create_embedding(text)`
- `select_model(task_type, hardware_profile)`

The gateway supports mock mode for development and local model runtimes for demonstrations. It must reject unapproved remote endpoints.

### Agent orchestrator

The orchestrator manages:

1. Task validation.
2. Plan creation.
3. Tool selection.
4. Step execution.
5. Intermediate state.
6. Retry and timeout policy.
7. Human review checkpoints.
8. Output generation.
9. Audit events.

The agent must not have unrestricted shell or filesystem access.

### Knowledge base

The knowledge base contains approved local manuals, SOPs, templates, and sample correspondence. The indexing interface should be replaceable:

```text
Source files -> parsing -> chunks + metadata -> local embeddings -> vector index
User task -> retrieval query -> ranked chunks + citations
```

### Output generation

Output adapters convert structured results into:

- DOCX approval notes.
- XLSX action trackers.
- PDF summaries.
- JSON records.
- Sandboxed source code and tests.

Output generation must validate required fields and report incomplete or uncertain data.

### Storage and audit

The MVP may use SQLite and local directories. Production evolution may use PostgreSQL and managed on-premise storage. Inputs, outputs, temporary files, vector indexes, and audit logs must be separated.

## 5. Task lifecycle

```text
CREATED -> QUEUED -> RUNNING -> WAITING_FOR_REVIEW -> COMPLETED
                         |                    |
                         +-> FAILED           +-> REJECTED
                         +-> CANCELLED
```

Every transition should have an event with task ID, timestamp, actor, previous state, new state, and reason.

## 6. Data flow

```text
User -> API -> validated local file
     -> extraction/OCR/vision
     -> structured document representation
     -> local knowledge retrieval
     -> agent plan and tool calls
     -> structured result
     -> human review
     -> generated deliverables
     -> local audit log
```

No step in this data flow should require the public internet.

## 7. Deployment topology

### Development

- Frontend container or Vite process.
- Backend container or local Python process.
- Local database/file volumes.
- Mock model provider.

### Demonstration

- Preloaded model files.
- Pre-indexed sample knowledge base.
- Outbound traffic blocked.
- Local network monitor enabled.
- Synthetic documents only.

### Future production

- Separate services with restricted service accounts.
- On-premise PostgreSQL and vector store.
- Centralized local identity provider.
- Container image signing and vulnerability scanning.
- High-availability storage and backups.

## 8. Key design decisions

- **FastAPI:** simple typed HTTP API and automatic OpenAPI documentation.
- **React/TypeScript:** maintainable dashboard with explicit API types.
- **Mock mode:** allows development and evaluation without pretending advanced AI services are complete.
- **Local file storage for MVP:** reduces deployment complexity while interfaces remain ready for a database/object-store evolution.
- **JSONL audit logs:** easy to inspect, stream, archive, and export during the SIH demonstration.

## 9. Extension points

Future modules may add:

- FAISS, Chroma, or Qdrant retrieval.
- Multiple model profiles and hardware-aware routing.
- Multilingual OCR.
- Human correction interfaces.
- Role-based enterprise identity.
- Approval workflow integration.
- Local notification services.

All extensions must preserve local-only processing and auditability.
