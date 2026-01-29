from __future__ import annotations

from datetime import date, timedelta
from uuid import uuid4

from fastapi import FastAPI, HTTPException, Query

from .contracts import (
    AttemptIn,
    DailySessionRecord,
    ReviewGradeIn,
    Scenario,
    ScenePack,
    SRSCard,
    WeeklyReport,
    WeeklyTestItem,
    WeeklyTestStartResponse,
    WeeklyTestSubmitIn,
)
from .sample_content import SAMPLE_SCENARIOS, SAMPLE_SCENES
from .sample_sessions import SAMPLE_CAFE_FORMAL
from .store import InMemoryStore

app = FastAPI(title="Lingo API", version="0.0.1")
store = InMemoryStore()
for scenario in SAMPLE_SCENARIOS:
    store.add_scenario(scenario)
for scene_pack in SAMPLE_SCENES.values():
    store.add_scene_pack(scene_pack)

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/v1/daily-session", response_model=DailySessionRecord)
def get_daily_session(session_date: date | None = Query(None, alias="date")):
    resolved_date = session_date or date.today()
    existing = store.get_session(resolved_date)
    if existing:
        return existing

    # MVP: return sample. Next: generate from content + user profile.
    session = DailySessionRecord(
        id=str(uuid4()),
        session_date=resolved_date,
        session_json=SAMPLE_CAFE_FORMAL,
    )
    store.save_session(resolved_date, session)
    return session

@app.post("/v1/attempts")
def post_attempt(attempt: AttemptIn):
    # MVP: store attempt. Next: detect mistakes -> generate SRS cards.
    store.add_attempt(attempt.model_dump())
    created_card_id = None
    if attempt.target_text:
        created_card_id = str(uuid4())
        card = SRSCard(
            id=created_card_id,
            front=attempt.target_text,
            back=attempt.stt_text or attempt.target_text,
            due_date=date.today(),
            ease=2.5,
            tags=["daily-session"],
            source="mistake",
            source_id=None,
        )
        store.add_card(card)
    return {"ok": True, "created_card_id": created_card_id}


@app.get("/v1/review/due", response_model=list[SRSCard])
def get_review_due(session_date: date | None = Query(None, alias="date")):
    resolved_date = session_date or date.today()
    return store.list_due_cards(resolved_date)


@app.post("/v1/review/grade")
def post_review_grade(grade: ReviewGradeIn):
    card = store.get_card(grade.card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")

    new_ease = max(1.3, card.ease + (grade.grade - 1.5) * 0.1)
    if grade.grade == 0:
        next_due = date.today()
    elif grade.grade == 1:
        next_due = date.today() + timedelta(days=1)
    elif grade.grade == 2:
        next_due = date.today() + timedelta(days=3)
    else:
        next_due = date.today() + timedelta(days=7)

    updated = card.model_copy(update={"ease": new_ease, "due_date": next_due})
    store.save_card(updated)
    return {"ok": True, "due_date": updated.due_date.isoformat(), "ease": updated.ease}


@app.get("/v1/scenarios", response_model=list[Scenario])
def get_scenarios():
    return store.scenarios


@app.get("/v1/scenes/{scenario_id}", response_model=ScenePack)
def get_scene_pack(scenario_id: str):
    scene_pack = store.get_scene_pack(scenario_id)
    if not scene_pack:
        raise HTTPException(status_code=404, detail="Scenario not found")
    return scene_pack


@app.post("/v1/weekly/test/start", response_model=WeeklyTestStartResponse)
def start_weekly_test():
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    test = WeeklyTestStartResponse(
        test_id=str(uuid4()),
        week_start=week_start,
        items=[
            WeeklyTestItem(prompt="Beställ en kaffe.", expected="Poproszę kawę."),
            WeeklyTestItem(prompt="Tacka artigt.", expected="Dziękuję uprzejmie."),
        ],
    )
    store.save_weekly_test(test)
    return test


@app.post("/v1/weekly/test/submit")
def submit_weekly_test(payload: WeeklyTestSubmitIn):
    test = store.get_weekly_test(payload.test_id)
    if not test:
        raise HTTPException(status_code=404, detail="Weekly test not found")
    report = WeeklyReport(
        id=str(uuid4()),
        week_start=test.week_start,
        metrics={"submitted_answers": len(payload.answers)},
        weaknesses={"top": ["politeness", "case endings"]},
        next_week_plan={"focus": ["beställa mat", "fråga om vägen"]},
    )
    store.save_weekly_report(report)
    return {"ok": True, "report_id": report.id}


@app.get("/v1/weekly/report", response_model=WeeklyReport)
def get_weekly_report(week_start: date = Query(..., alias="week_start")):
    report = store.get_weekly_report(week_start)
    if not report:
        raise HTTPException(status_code=404, detail="Weekly report not found")
    return report
