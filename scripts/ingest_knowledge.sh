#!/usr/bin/env bash
set -euo pipefail

API_BASE_URL="${API_BASE_URL:-http://127.0.0.1:8000}"
SOURCE_DIR="${1:-/workspace/knowledge_base}"

curl -fsS -X POST "$API_BASE_URL/knowledge/ingest" \
  -H "Content-Type: application/json" \
  -d "{\"source_dir\": \"$SOURCE_DIR\"}" | python -m json.tool
