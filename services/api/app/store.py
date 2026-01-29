from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Dict, List, Optional

from .contracts import DailySessionRecord, Mistake, Scenario, ScenePack, SRSCard, WeeklyReport, WeeklyTestStartResponse

@dataclass
class InMemoryStore:
    sessions_by_date: Dict[str, DailySessionRecord] = field(default_factory=dict)
    attempts: List[dict] = field(default_factory=list)
    mistakes: Dict[str, Mistake] = field(default_factory=dict)
    srs_cards: Dict[str, SRSCard] = field(default_factory=dict)
    scenarios: List[Scenario] = field(default_factory=list)
    scenes_by_scenario: Dict[str, ScenePack] = field(default_factory=dict)
    weekly_tests: Dict[str, WeeklyTestStartResponse] = field(default_factory=dict)
    weekly_reports: Dict[str, WeeklyReport] = field(default_factory=dict)

    def get_session(
        self,
        session_date: date,
        scenario: str | None = None,
        tone: str | None = None,
    ) -> DailySessionRecord | None:
        return self.sessions_by_date.get(self._session_key(session_date, scenario, tone))

    def save_session(
        self,
        session_date: date,
        session: DailySessionRecord,
        scenario: str | None = None,
        tone: str | None = None,
    ) -> None:
        self.sessions_by_date[self._session_key(session_date, scenario, tone)] = session

    @staticmethod
    def _session_key(session_date: date, scenario: str | None, tone: str | None) -> str:
        return f"{session_date.isoformat()}::{scenario or 'default'}::{tone or 'default'}"

    def add_attempt(self, attempt: dict) -> None:
        self.attempts.append(attempt)

    def add_mistake(self, mistake: Mistake) -> None:
        self.mistakes[mistake.id] = mistake

    def add_card(self, card: SRSCard) -> None:
        self.srs_cards[card.id] = card

    def list_due_cards(self, session_date: date) -> List[SRSCard]:
        return [
            card
            for card in self.srs_cards.values()
            if card.due_date <= session_date
        ]

    def get_card(self, card_id: str) -> Optional[SRSCard]:
        return self.srs_cards.get(card_id)

    def save_card(self, card: SRSCard) -> None:
        self.srs_cards[card.id] = card

    def add_scenario(self, scenario: Scenario) -> None:
        self.scenarios.append(scenario)

    def add_scene_pack(self, scene_pack: ScenePack) -> None:
        self.scenes_by_scenario[scene_pack.scenario_id] = scene_pack

    def get_scene_pack(self, scenario_id: str) -> Optional[ScenePack]:
        return self.scenes_by_scenario.get(scenario_id)

    def save_weekly_test(self, test: WeeklyTestStartResponse) -> None:
        self.weekly_tests[test.test_id] = test

    def get_weekly_test(self, test_id: str) -> Optional[WeeklyTestStartResponse]:
        return self.weekly_tests.get(test_id)

    def save_weekly_report(self, report: WeeklyReport) -> None:
        self.weekly_reports[report.week_start.isoformat()] = report

    def get_weekly_report(self, week_start: date) -> Optional[WeeklyReport]:
        return self.weekly_reports.get(week_start.isoformat())
