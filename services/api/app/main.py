from __future__ import annotations

from datetime import date
from fastapi import FastAPI
from pydantic import BaseModel, Field

from .contracts import DailySession
from .sample_sessions import SAMPLE_CAFE_FORMAL
from .store import InMemoryStore

app = FastAPI(title="Lingo API", version="0.0.1")
store = InMemoryStore()

class AttemptIn(BaseModel):
    input_type: str = Field(description="audio|text")
    stt_text: str | None = None
    target_text: str | None = None
    score: dict | None = None

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/v1/daily-session", response_model=DailySession)
def get_daily_session():
    today = date.today()
    existing = store.get_session(today)
    if existing:
        return existing

    # MVP: return sample. Next: generate from content + user profile.
    store.save_session(today, SAMPLE_CAFE_FORMAL)
    return SAMPLE_CAFE_FORMAL

@app.post("/v1/attempts")
def post_attempt(attempt: AttemptIn):
    # MVP: store attempt. Next: detect mistakes -> generate SRS cards.
    store.add_attempt(attempt.model_dump())
    return {"ok": True}
