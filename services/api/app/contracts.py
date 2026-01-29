from __future__ import annotations

from datetime import date
from typing import List, Literal, Optional
from pydantic import BaseModel, Field

Tone = Literal["formal", "casual"]
InputType = Literal["audio", "text"]
CardSource = Literal["mistake", "highfreq"]

class Check(BaseModel):
    q: str = Field(min_length=1)
    a: str = Field(min_length=1)

class Sentence(BaseModel):
    pl: str = Field(min_length=1)
    sv: str = Field(min_length=1)
    checks: Optional[List[Check]] = None

class DialogSeed(BaseModel):
    role: str = Field(min_length=1)
    opening: str = Field(min_length=1)

class Pattern(BaseModel):
    template: str = Field(min_length=1)
    examples: List[str] = Field(min_length=1)

class DailySession(BaseModel):
    mission: str = Field(min_length=1)
    scene: str = Field(min_length=1)
    tone: Tone
    sentences: List[Sentence] = Field(min_length=1)
    dialog_seed: DialogSeed
    patterns: Optional[List[Pattern]] = None


class DailySessionRecord(BaseModel):
    id: str = Field(min_length=1)
    session_date: date
    session_json: DailySession


class AttemptIn(BaseModel):
    daily_session_id: str = Field(min_length=1)
    input_type: InputType
    stt_text: Optional[str] = None
    target_text: Optional[str] = None
    score: Optional[dict] = None


class Scenario(BaseModel):
    id: str = Field(min_length=1)
    name_sv: str = Field(min_length=1)
    tags: List[str] = Field(default_factory=list)


class SceneImage(BaseModel):
    url: str = Field(min_length=1)
    alt: str = Field(min_length=1)


class ScenePack(BaseModel):
    scenario_id: str = Field(min_length=1)
    name_sv: str = Field(min_length=1)
    images: List[SceneImage] = Field(min_length=1)


class SRSCard(BaseModel):
    id: str = Field(min_length=1)
    front: str = Field(min_length=1)
    back: str = Field(min_length=1)
    due_date: date
    ease: float = Field(ge=1.0)
    interval_days: int = Field(ge=0)
    repetitions: int = Field(ge=0)
    last_reviewed: Optional[date] = None
    tags: List[str] = Field(default_factory=list)
    source: CardSource
    source_id: Optional[str] = None


class Mistake(BaseModel):
    id: str = Field(min_length=1)
    daily_session_id: str = Field(min_length=1)
    target_text: str = Field(min_length=1)
    input_text: str = Field(min_length=1)
    detected_at: date


class ReviewGradeIn(BaseModel):
    card_id: str = Field(min_length=1)
    grade: int = Field(ge=0, le=3)


class WeeklyTestItem(BaseModel):
    prompt: str = Field(min_length=1)
    expected: str = Field(min_length=1)


class WeeklyTestStartResponse(BaseModel):
    test_id: str = Field(min_length=1)
    week_start: date
    items: List[WeeklyTestItem] = Field(min_length=1)


class WeeklyTestSubmitIn(BaseModel):
    test_id: str = Field(min_length=1)
    answers: List[str] = Field(default_factory=list)


class WeeklyReport(BaseModel):
    id: str = Field(min_length=1)
    week_start: date
    metrics: dict
    weaknesses: dict
    next_week_plan: dict
