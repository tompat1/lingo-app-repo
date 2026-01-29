from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Dict, List

from .contracts import DailySession

@dataclass
class InMemoryStore:
    sessions_by_date: Dict[str, DailySession] = field(default_factory=dict)
    attempts: List[dict] = field(default_factory=list)

    def get_session(self, session_date: date) -> DailySession | None:
        return self.sessions_by_date.get(session_date.isoformat())

    def save_session(self, session_date: date, session: DailySession) -> None:
        self.sessions_by_date[session_date.isoformat()] = session

    def add_attempt(self, attempt: dict) -> None:
        self.attempts.append(attempt)
