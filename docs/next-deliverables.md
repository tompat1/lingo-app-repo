# Next Deliverables (MVP)

Det här dokumentet sammanfattar “Next Deliverables” för Lingo App (direkt körbart som underlag för design/dev). Innehållet följer aktuell MVP-spec och fungerar som referens för UX/UI, produkt och implementation.

## 1) MVP-spec: user stories + acceptance criteria

### Epic A — Onboarding & Home
**US-A1: Sätta preferenser**  
Som användare vill jag välja mål (travel/work/daily), nivå (A0–B2), tone default (formal/casual) och tid per dag så att passen matchar mig.

**AC**
- Kan spara `UserProfile`.
- Home visar “Dagens pass” + streak + “Dagens svagaste område”.

**US-A2: Starta dagens pass**  
Som användare vill jag starta dagens pass med ett klick.

**AC**
- Skapar/hämtar `DailySession` för dagens datum.
- Offline-cache: kan öppna sessionen utan nät efter första hämtningen.

### Epic B — Scene Cards (bild + TTS + STT + feedback)
**US-B1: Spela upp target (TTS)**

**AC**
- “Play” spelar upp meningen.
- “Slower” spelar upp långsammare.
- “Replay” spelar upp igen.

**US-B2: Säg meningen (STT)**

**AC**
- “Say it” spelar in push-to-talk och transkriberar.
- App visar: (1) din STT-text, (2) target, (3) enkel score + 1–2 micro-corrections.

### Epic C — 10 meningar (comprehension drills)
**US-C1: 10 meningar med checks**

**AC**
- Visar 1 mening åt gången.
- Efter varje mening: 2–3 frågor med facit.
- Kontroller: replay / slower / show translation.

### Epic D — Dialog (chat + optional voice senare)
**US-D1: Textdialog med tone switch**

**AC**
- Dialog startar från `dialog_seed` (barista/expedient osv).
- Tone switch byter mellan formal/casual och påverkar öppningar + fraser.
- Micro-corrections max 1–2 saker per tur.

### Epic E — SRS & “mistake → card”
**US-E1: Auto-generera kort**

**AC**
- Varje `Mistake` kan skapa 1+ `SRSCard` med taggar (source: mistake/highfreq).
- Review visar dagens nya kort + nästa due.

**US-E2: Daglig review**

**AC**
- Visar due cards (begränsa till t.ex. 5–20).
- Uppdaterar ease + due_date.

### Epic F — Weekly recall + weakness report
**US-F1: Weekly test**

**AC**
- Timed test (t.ex. 3–5 min) med blandning: highfreq + mistake-cards.
- Skapar `WeeklyReport` med svagheter + `next_week_plan`.

## 2) Informationsarkitektur + microcopy (MVP)

### Global navigation (MVP)
- Home
- Review (SRS)
- Settings (profil/tone)

### Microcopy-kärna (kort, flow-vänligt)

**Home**
- CTA: “Starta dagens pass”
- Streak: “Streak: {n} dagar”
- Weak spot: “Fokus idag: {weak_area}”

**Scene Card**
- Play: “Lyssna”
- Say it: “Säg det”
- Feedback rubrik: “Snabb feedback”
- Controls: “Långsammare”, “Repetera”, “Visa översättning”

**10 meningar**
- “Frågor” / “Kolla svar”
- “Nästa mening”

**Dialog**
- Placeholder: “Svara som om du står i kön…”
- Tone: “Formell (Pan/Pani)” / “Casual (Cześć)”
- Correction chip: “Lite bättre: …” (inte “Fel: …”)

**Review**
- “Dagens 3 lärdomar”
- “Nya kort från dina misstag”
- “Imorgon: {tomorrow_focus}”

**Felmeddelanden (lugna)**
- STT misslyckas: “Jag hörde inte riktigt — testa igen lite närmare mikrofonen.”
- Nät offline: “Offline-läge: jag visar senaste cachade passet.”

## 3) UI-wireframes (Figma-ready struktur)

### Screen 1 — Home
- Header: “Lingo”
- Primary card: Dagens pass
- Scenario + tone badge
- CTA knapp
- Secondary: Streak, Weakest area, “Senaste report (kort)”

### Screen 2 — Scene Card
- Top: Scenario title + tone toggle
- Center: Image (scene)
- Under: Target sentence (PL) + optional SV
- Controls row: Play / Slower / Replay / Translation
- Record module: “Säg det” + waveform + transkript
- Feedback module: score + 1–2 corrections + “natural variant”

### Screen 3 — 10 meningar
- Stepper (1/10)
- Sentence block + Play controls
- Checks block (2–3 Q)
- CTA: Next

### Screen 4 — Dialog
- Chat stream
- Input: text + mic (voice senare)
- Tone toggle persistent
- Inline micro-correction chip under user bubble (max 1–2)

### Screen 5 — Review
- “3 lärdomar” bullets
- New cards list (front/back preview)
- “Tomorrow’s focus” card
