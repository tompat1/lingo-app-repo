from __future__ import annotations

from datetime import date
from typing import Dict, List, Tuple

from .contracts import DailySession

PolishPackKey = Tuple[str, str]

POLISH_PACK_V1: Dict[PolishPackKey, List[dict]] = {
    ("cafe", "formal"): [
        {
            "mission": "Beställa på café med rätt artighet",
            "scene": "cafe",
            "tone": "formal",
            "sentences": [
                {
                    "pl": "Dzień dobry, poproszę kawę z mlekiem.",
                    "sv": "God dag, jag vill ha kaffe med mjölk.",
                    "checks": [
                        {"q": "Vad beställer du?", "a": "kawę z mlekiem"},
                        {"q": "Är tonen formell?", "a": "ja"},
                    ],
                },
                {
                    "pl": "Czy mogę dostać rachunek, proszę?",
                    "sv": "Kan jag få notan, tack?",
                    "checks": [{"q": "Vad frågar du efter?", "a": "rachunek"}],
                },
            ],
            "dialog_seed": {"role": "barista", "opening": "Dzień dobry! Co podać?"},
            "patterns": [
                {
                    "template": "Poproszę + [sak].",
                    "examples": ["Poproszę wodę.", "Poproszę rachunek."],
                }
            ],
        }
    ],
    ("cafe", "casual"): [
        {
            "mission": "Snacka ledigt på café",
            "scene": "cafe",
            "tone": "casual",
            "sentences": [
                {
                    "pl": "Hej! Poproszę latte na wynos.",
                    "sv": "Hej! Jag tar en latte to-go.",
                    "checks": [
                        {"q": "Vad vill du ha?", "a": "latte na wynos"},
                        {"q": "Är tonen ledig?", "a": "ja"},
                    ],
                },
                {
                    "pl": "Masz może ciastko?",
                    "sv": "Har du möjligtvis en kaka?",
                    "checks": [{"q": "Vad frågar du efter?", "a": "ciastko"}],
                },
            ],
            "dialog_seed": {"role": "barista", "opening": "Cześć! Co dla ciebie?"},
            "patterns": [
                {
                    "template": "Masz może + [sak]?",
                    "examples": ["Masz może cukier?", "Masz może sernik?"],
                }
            ],
        }
    ],
}


def generate_daily_session(
    scenario: str | None,
    tone: str | None,
    session_date: date,
) -> DailySession:
    resolved_scenario = scenario or "cafe"
    resolved_tone = tone or "formal"
    key = (resolved_scenario, resolved_tone)
    entries = POLISH_PACK_V1.get(key)
    if not entries:
        raise ValueError(f"No content for scenario={resolved_scenario} tone={resolved_tone}")
    index = session_date.toordinal() % len(entries)
    payload = entries[index]
    return DailySession.model_validate(payload)
