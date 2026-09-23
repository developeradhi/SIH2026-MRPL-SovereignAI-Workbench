#!/usr/bin/env bash
set -euo pipefail

API_BASE_URL="${API_BASE_URL:-http://127.0.0.1:8000}"
response="$(curl -fsS "$API_BASE_URL/security/network-status")"

echo "$response" | python -m json.tool

if RESPONSE_JSON="$response" python - <<'PY'
import json
import os
import sys

payload = json.loads(os.environ["RESPONSE_JSON"])
if payload.get("offline_mode") and payload.get("model_endpoint_local"):
    sys.exit(0)
sys.exit(1)
PY
then
  echo "[offline-check] offline_mode is enabled"
else
  echo "[offline-check] offline_mode/model_endpoint_local requirements not met"
  exit 1
fi
