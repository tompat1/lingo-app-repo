# Lingo App (Monorepo)

Språk-agnostisk, multimodal språkcoach (bild + tal + text) med fokus på speaking + listening.

## Repo-struktur
- `apps/mobile` – Expo React Native (iOS/Android)
- `services/api` – FastAPI (JSON-kontrakt, sessioner, SRS)
- `packages/contracts` – Delade kontrakt (Zod/TS) för renderbar AI-JSON

## Snabbstart (lokalt)

### 1) Mobile
```bash
cd apps/mobile
pnpm install
pnpm start
```

### 2) API
```bash
cd services/api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

API: `http://localhost:8000/docs`

## Viktigt
- Allt AI-genererat ska vara **renderbar JSON** (se `packages/contracts`).
- MVP kör in-memory storage först; byt till Supabase/Postgres när loop + kontrakt sitter.
