# Lingo App (Monorepo)

Språk-agnostisk, multimodal språkcoach (bild + tal + text) med fokus på speaking + listening.

## Repo-struktur
- `apps/mobile` – Expo React Native (iOS/Android)
- `services/api` – FastAPI (JSON-kontrakt, sessioner, SRS)
- `packages/contracts` – Delade kontrakt (Zod/TS) för renderbar AI-JSON

## Snabbstart (lokalt)

### Monorepo (mobile + API)
```bash
pnpm install
pnpm dev
```

### 1) Mobile
```bash
cd apps/mobile
pnpm install
pnpm start
```

Om appen körs i emulator/enhet kommer `localhost` inte peka på API:t. Sätt då
`EXPO_PUBLIC_API_BASE` till din dator-IP (t.ex. `http://192.168.x.x:8000`), eller
använd Android-emulatorns standard `http://10.0.2.2:8000`.

Om `pnpm install` klagar på `@types/react-native@~0.76.0` finns den versionen inte publicerad. React Native inkluderar TypeScript-typer, så ta bort `@types/react-native` om den råkar finnas som dependency, eller pinna den till senaste publicerade version. Du kan kontrollera listan med:
```bash
pnpm view @types/react-native versions
```

Start-check för Expo-entry (valfritt men bra för CI/lokalt):
```bash
pnpm -C apps/mobile test:start-check
```

### 2) API
```bash
cd services/api
./scripts/dev.sh
```

Om du har proxy-variabler i miljön (t.ex. `HTTP_PROXY`), se till att de är avstängda
så att `pip install` kan nå PyPI. `scripts/dev.sh` gör detta automatiskt.

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

## Databasschema
Se `docs/db-schema.md` för Postgres/Supabase-tabellerna.
