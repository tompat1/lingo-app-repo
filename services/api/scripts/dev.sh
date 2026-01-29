#!/usr/bin/env bash

set -euo pipefail

unset http_proxy https_proxy HTTP_PROXY HTTPS_PROXY

if command -v python3 >/dev/null 2>&1; then
  PYTHON=python3
elif command -v python >/dev/null 2>&1; then
  PYTHON=python
else
  echo "Error: python or python3 is required but was not found in PATH." >&2
  exit 1
fi

${PYTHON} -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
