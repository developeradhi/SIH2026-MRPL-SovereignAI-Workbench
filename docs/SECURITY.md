# Security and Offline Operation

## 1. Security objective

SovereignAI Workbench is designed to process confidential industrial work inside a controlled local environment. The system must not rely on external AI APIs, cloud storage, hosted vector databases, remote telemetry, or internet access during the demonstration.

A README statement is not proof of sovereignty. The team must demonstrate configuration, network restrictions, application logs, and repeatable verification.

## 2. Security boundaries

### Trusted components

- Controlled host operating system.
- Approved local model files.
- Application containers and source code.
- Approved synthetic/public demonstration data.
- Local database and storage volumes.

### Untrusted inputs

- Uploaded documents.
- OCR output.
- Text inside PDFs and images.
- Retrieved document content.
- Model-generated code.
- User-supplied prompts and filenames.

Documents must be treated as data, not instructions. A document must never be allowed to override system security rules.

## 3. Required controls

### Network isolation

- Set `OFFLINE_MODE=true`.
- Set `ALLOW_EXTERNAL_NETWORK=false`.
- Permit only approved loopback or local model endpoints.
- Block outbound traffic at the host, container, or network layer.
- Disable dependency telemetry where possible.
- Do not use external fonts, CDNs, analytics, hosted maps, or cloud APIs.

### File security

- Allowlist file extensions.
- Enforce maximum file size.
- Generate a checksum for each uploaded file.
- Store uploads beneath configured directories only.
- Resolve paths and reject traversal such as `../`.
- Use generated IDs instead of trusting filenames.
- Keep temporary files separate from final outputs.
- Do not log complete document contents by default.

### Secrets

- Store secrets in environment variables or an approved local secret manager.
- Never commit `.env`, API keys, passwords, certificates, tokens, or private keys.
- Redact secrets from errors and audit logs.
- Rotate credentials used during development if accidentally exposed.

### Model and dependency supply chain

Record for every model:

- Name and version.
- Source.
- License.
- File checksum.
- Runtime version.
- Required hardware.
- Known limitations.

Pin application dependencies where practical and record third-party notices.

### Generated code

Generated code is untrusted. Run it only in a restricted sandbox with:

- No network access.
- Read-only source inputs where possible.
- A temporary working directory.
- CPU, memory, process, disk, and time limits.
- No host socket or credential access.
- A restricted executable allowlist.

Do not implement unrestricted shell execution as an agent tool.

## 4. Audit requirements

Record the following without leaking document contents:

- Event ID.
- Timestamp.
- User or service identity.
- Task ID.
- Action type.
- Input/output file IDs and checksums.
- Model profile and version.
- Tool name and result status.
- Security warnings.
- State transitions.

Audit logs should be append-only for the demonstration and exportable with the final task results.

## 5. Sovereignty verification procedure

### Before the demo

1. Prepare dependencies and model files while internet access is available.
2. Record checksums and versions.
3. Stop unnecessary services.
4. Set offline configuration variables.
5. Apply host or container firewall rules.
6. Confirm the model endpoint is local.
7. Run the verification script.

```bash
bash scripts/verify_offline_mode.sh
```

### During the demo

Show:

- Application configuration.
- Local model endpoint.
- Active local connections.
- Blocked outbound policy.
- Task events.
- Audit logs.
- Generated outputs.

Useful diagnostic commands:

```bash
ss -tulpn
ss -tpn
docker compose ps
docker network ls
docker inspect <container-name>
```

### After the demo

- Export task and security logs.
- Remove sample outputs if they contain sensitive test content.
- Reset local credentials.
- Confirm no confidential data was committed or uploaded.

## 6. Threat model

| Threat | Mitigation |
|---|---|
| Document exfiltration | Offline network policy, local model gateway, no cloud APIs |
| Prompt injection | Treat documents as untrusted, fixed system policy, tool allowlist |
| Path traversal | Canonical path checks and approved storage roots |
| Malicious upload | Type/size checks, safe parsing, malware scanning where available |
| Unsafe generated code | Network-disabled sandbox and resource limits |
| Hallucinated output | Evidence, citations, confidence, validation and human review |
| Unauthorized access | Local authentication, roles and file permissions |
| Log leakage | Redaction and event metadata instead of raw document contents |
| Dependency compromise | Version pinning, checksums, offline preparation |
| Denial of service | Upload limits, task timeouts, queue limits and resource controls |

## 7. Human review policy

The system is an assistant, not an approval authority. Require human review before:

- Final approval notes.
- Safety, compliance, legal, financial, or operational decisions.
- Sending information to another system.
- Executing generated code outside the sandbox.
- Marking a task as approved.

The UI must distinguish extracted facts, model inferences, warnings, and reviewer decisions.

## 8. Known limitations

- Local model quality depends on hardware and selected model.
- OCR may be inaccurate for poor-quality handwriting.
- Network verification in application code cannot replace host firewall evidence.
- The starter mock provider does not represent production model quality.
- Authentication and enterprise identity require additional hardening before real deployment.

## 9. Security checklist

- [ ] No confidential data in Git.
- [ ] No secrets in source or logs.
- [ ] Offline mode enabled.
- [ ] External network disabled.
- [ ] Model endpoint is local.
- [ ] Upload extensions and sizes are limited.
- [ ] Paths are restricted.
- [ ] Generated code is sandboxed.
- [ ] Audit logs are created.
- [ ] Human review is enabled.
- [ ] Model versions and licenses are recorded.
- [ ] Security logs are included in the demo.
