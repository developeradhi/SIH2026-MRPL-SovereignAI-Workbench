# SIH Demonstration Script

## Project

**SovereignAI Workbench**  
SIH 2026 | MRPL | Smart Automation  
Problem title: Sovereign On-Premise Agentic AI Workbench using Open-Weight Multimodal LLMs for Confidential Industrial Work

Use only synthetic or publicly shareable demonstration files.

## 1. Demonstration objective

Show that the workbench can process a multimodal industrial document, retrieve local knowledge, complete a multi-step task, generate real deliverables, and prove that processing remains local with no external calls.

## 2. Preparation checklist

### One day before

- [ ] Build the backend and frontend.
- [ ] Prepare local model files or enable mock mode.
- [ ] Index the sample knowledge base.
- [ ] Prepare a synthetic scanned inspection report.
- [ ] Prepare a sample SOP and document template.
- [ ] Test DOCX, XLSX and PDF generation.
- [ ] Run unit, integration and end-to-end tests.
- [ ] Test the offline verification script.
- [ ] Record a backup screen capture.

### Before evaluators arrive

```bash
docker compose up -d
curl http://127.0.0.1:8000/health
bash scripts/verify_offline_mode.sh
```

Open the frontend and keep these views ready:

1. Dashboard.
2. Document upload.
3. Task progress.
4. Evidence/citations.
5. Generated outputs.
6. Security/network status.
7. Audit logs.

## 3. Five-minute presentation

### 0:00–0:30 — Problem

Say:

> Industrial teams work with confidential inspection reports, SOPs, manuals, drawings and correspondence. Cloud chatbots create a confidentiality risk and usually stop at a text answer. Our platform performs the complete task locally and produces an auditable business deliverable.

### 0:30–1:00 — Solution

Show the architecture and explain:

- Local document processing.
- Local OCR and vision.
- Local model gateway.
- Knowledge-base retrieval.
- Agentic task execution.
- Human review and audit.
- Network isolation.

### 1:00–1:30 — Upload

Upload `sample_inspection_report.pdf`.

Point out:

- The document is stored locally.
- The checksum is generated.
- The system identifies scanned pages.
- OCR or the mock extraction path starts.

### 1:30–2:15 — Task creation

Select or create:

```text
Task: Convert inspection report into an approval note and action tracker.
Inputs: sample_inspection_report.pdf
Knowledge: sample_inspection_sop.pdf
Outputs: DOCX approval note, XLSX action tracker, PDF summary
Review: required
```

Show the generated plan:

1. Extract text and tables.
2. Run OCR or multimodal analysis.
3. Retrieve relevant SOP sections.
4. Identify findings and uncertainty.
5. Create structured results.
6. Generate deliverables.
7. Request human review.

### 2:15–3:00 — Evidence and retrieval

Open the event timeline and evidence panel.

Explain:

- Which pages were read.
- Which local SOP sections were retrieved.
- Which facts were extracted.
- Which fields have warnings or low confidence.
- How citations connect the result to source material.

### 3:00–3:45 — Outputs

Open the generated files:

- DOCX approval note.
- XLSX action tracker.
- PDF summary.

Show that the outputs contain source references, warnings, reviewer status and generated metadata.

### 3:45–4:20 — Sovereignty proof

Open the security panel and show:

- `OFFLINE_MODE=true`.
- `ALLOW_EXTERNAL_NETWORK=false`.
- Local model endpoint.
- Active local connections.
- Blocked or absent external connections.
- Audit events for the task.

Run:

```bash
bash scripts/verify_offline_mode.sh
```

Say:

> Sovereignty is demonstrated by configuration, network policy, local endpoints, application events and repeatable verification—not by a claim in the interface.

### 4:20–5:00 — Second task and conclusion

Demonstrate a second task, such as:

- Engineering drawing/specification discrepancy report.
- Local coding assistant with sandboxed tests.
- Compliance checklist generation.

Conclude:

> The same local workbench can process different industrial tasks while keeping documents, inference, retrieval and outputs inside the controlled environment. It is designed to scale from a working prototype to a hardened on-premise system.

## 4. Backup demo

If the model service fails:

1. Switch to mock mode.
2. Use pre-indexed sample files.
3. Demonstrate the same task lifecycle, evidence, output generation and security logs.
4. Explain clearly that mock mode is a deterministic demonstration adapter, not the final AI capability.

If the UI fails:

```bash
curl http://127.0.0.1:8000/health
curl -X POST http://127.0.0.1:8000/api/tasks \
  -H 'Content-Type: application/json' \
  -d '{"name":"Inspection demo","require_human_review":true}'
```

Use the API documentation at `/docs` for the exact current request schema.

## 5. Questions evaluators may ask

### Why on-premise?

Industrial documents may contain confidential operational information. Local processing reduces exposure and supports controlled deployment.

### Is this only a chatbot?

No. The system plans and executes multi-step workflows, calls controlled tools, retrieves local evidence, generates files, pauses for review, and records an audit trail.

### How is multimodality handled?

The document pipeline routes text documents, scanned pages, images, tables and drawings to the appropriate local parser, OCR engine or vision model.

### What happens without a GPU?

The model router can select a smaller quantized model, use CPU inference, or use OCR plus text processing. The demo is prepared with a CPU/mock fallback.

### How do you prove no data leaves?

The system uses local endpoints, outbound network restrictions, security configuration, connection inspection, application logs and a repeatable verification script.

### Can the AI approve a safety decision?

No. High-impact outputs require human review. The system is an assistant and evidence organizer.

### What remains for production?

Enterprise identity, hardened sandboxing, production-grade vector storage, model evaluation, deployment hardening, backup strategy, and integration with approved internal systems.

## 6. Final checklist

- [ ] Demo data is not confidential.
- [ ] App starts without internet.
- [ ] Health endpoint works.
- [ ] Knowledge base is indexed.
- [ ] At least one scanned/image document is ready.
- [ ] At least two task types are prepared.
- [ ] Deliverables open correctly.
- [ ] Audit logs are visible.
- [ ] Offline verification passes.
- [ ] Backup demo is available.
- [ ] Every teammate understands their component.
- [ ] Final SIH problem statement ID and wording are confirmed on the official portal.
