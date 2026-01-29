from __future__ import annotations

from datetime import date, timedelta
from uuid import uuid4

from fastapi import FastAPI, HTTPException, Query

from .contracts import (
    AttemptIn,
    DailySessionRecord,
    Mistake,
    ReviewGradeIn,
    Scenario,
    ScenePack,
    SRSCard,
    WeeklyReport,
    WeeklyTestItem,
    WeeklyTestStartResponse,
    WeeklyTestSubmitIn,
)
from .content_library import generate_daily_session
from .sample_content import SAMPLE_SCENARIOS, SAMPLE_SCENES
from .store import InMemoryStore

app = FastAPI(title="Lingo API", version="0.0.1")
store = InMemoryStore()
for scenario in SAMPLE_SCENARIOS:
    store.add_scenario(scenario)
for scene_pack in SAMPLE_SCENES.values():
    store.add_scene_pack(scene_pack)

def seed_start_srs(session: DailySessionRecord) -> None:
    if not session.session_json.start_srs:
        return
    if any("starter-pack" in card.tags for card in store.srs_cards.values()):
        return
    for seed in session.session_json.start_srs:
        card = SRSCard(
            id=str(uuid4()),
            front=seed.front,
            back=seed.back,
            due_date=session.session_date,
            ease=2.5,
            interval_days=0,
            repetitions=0,
            last_reviewed=None,
            tags=seed.tags,
            source="highfreq",
            source_id=session.id,
        )
        store.add_card(card)

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/v1/daily-session", response_model=DailySessionRecord)
def get_daily_session(
    session_date: date | None = Query(None, alias="date"),
    scenario: str | None = Query(None),
    tone: str | None = Query(None),
):
    resolved_date = session_date or date.today()
    existing = store.get_session(resolved_date, scenario, tone)
    if existing:
        return existing

    try:
        daily_session = generate_daily_session(scenario, tone, resolved_date)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

    session = DailySessionRecord(
        id=str(uuid4()),
        session_date=resolved_date,
        session_json=daily_session,
    )
    store.save_session(resolved_date, session, scenario, tone)
    seed_start_srs(session)
    return session

@app.post("/v1/attempts")
def post_attempt(attempt: AttemptIn):
    store.add_attempt(attempt.model_dump())
    created_card_id = None
    created_mistake_id = None
    if attempt.target_text and attempt.stt_text and attempt.stt_text != attempt.target_text:
        created_mistake_id = str(uuid4())
        mistake = Mistake(
            id=created_mistake_id,
            daily_session_id=attempt.daily_session_id,
            target_text=attempt.target_text,
            input_text=attempt.stt_text,
            detected_at=date.today(),
        )
        store.add_mistake(mistake)

        created_card_id = str(uuid4())
        card = SRSCard(
            id=created_card_id,
            front=attempt.target_text,
            back=attempt.target_text,
            due_date=date.today(),
            ease=2.5,
            interval_days=0,
            repetitions=0,
            last_reviewed=None,
            tags=["mistake", "daily-session"],
            source="mistake",
            source_id=created_mistake_id,
        )
        store.add_card(card)
    return {
        "ok": True,
        "created_mistake_id": created_mistake_id,
        "created_card_id": created_card_id,
    }


@app.get("/v1/review/due", response_model=list[SRSCard])
def get_review_due(session_date: date | None = Query(None, alias="date")):
    resolved_date = session_date or date.today()
    return store.list_due_cards(resolved_date)


@app.post("/v1/review/grade")
def post_review_grade(grade: ReviewGradeIn):
    card = store.get_card(grade.card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")

    quality = grade.grade
    new_ease = max(
        1.3,
        card.ease + (0.1 - (3 - quality) * (0.08 + (3 - quality) * 0.02)),
    )
    if quality < 2:
        repetitions = 0
        interval_days = 1
    else:
        repetitions = card.repetitions + 1
        if repetitions == 1:
            interval_days = 1
        elif repetitions == 2:
            interval_days = 3
        else:
            interval_days = max(1, round(card.interval_days * new_ease))

    next_due = date.today() + timedelta(days=interval_days)
    updated = card.model_copy(
        update={
            "ease": new_ease,
            "due_date": next_due,
            "interval_days": interval_days,
            "repetitions": repetitions,
            "last_reviewed": date.today(),
        }
    )
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
