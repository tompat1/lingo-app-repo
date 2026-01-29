# Codex workflow (Lingo)

## 1) Cloud (Codex web)
- Gå till Codex och koppla repo via GitHub-integration.
- Låt Codex arbeta i PR:er (skapa PR per task), så du kan granska diffar.

## 2) GitHub PR review
- När Code review är aktiverat för repot kan du kommentera i en PR med:
  - `@codex review`

## 3) CLI
- Kör Codex CLI i repo-root och ge den en task, t.ex.
  - “Implementera /v1/daily-session enligt kontraktet och lägg till Zod+Pydantic validering.”

## 4) Våra regler (för att hålla flow)
- Håll ändringar små: 1 feature per PR.
- Uppdatera kontrakt först (`packages/contracts`), sedan API, sedan app.
