from __future__ import annotations

from typing import List, Literal, Optional
from pydantic import BaseModel, Field

Tone = Literal["formal", "casual"]

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
