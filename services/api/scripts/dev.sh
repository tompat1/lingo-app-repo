#!/usr/bin/env bash

set -euo pipefail

unset http_proxy https_proxy HTTP_PROXY HTTPS_PROXY

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
