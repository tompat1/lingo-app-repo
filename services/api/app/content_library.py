from __future__ import annotations

from datetime import date
from typing import Dict, List, Tuple

from .contracts import DailySession

PolishPackKey = Tuple[str, str]

POLISH_PACK_V1: Dict[PolishPackKey, List[dict]] = {
    ("cafe", "formal"): [
        {
            "mission": "Vecka 1: överlevnad & artighet (startpaket)",
            "scene": "cafe",
            "tone": "formal",
            "sentences": [
                {
                    "pl": "Przepraszam, gdzie jest najbliższy sklep?",
                    "sv": "Ursäkta, var är närmaste butik?",
                    "checks": [
                        {"q": "Vad frågar du efter?", "a": "najbliższy sklep"},
                        {"q": "Vad betyder \"najbliższy\"?", "a": "närmast"},
                    ],
                },
                {
                    "pl": "Poproszę kawę z mlekiem i wodę niegazowaną.",
                    "sv": "Jag vill ha kaffe med mjölk och stilla vatten.",
                    "checks": [
                        {"q": "Vad beställer du?", "a": "kawę z mlekiem i wodę niegazowaną"},
                        {"q": "Vad betyder \"niegazowaną\"?", "a": "utan kolsyra"},
                    ],
                },
                {
                    "pl": "Czy mogę zapłacić kartą?",
                    "sv": "Kan jag betala med kort?",
                    "checks": [
                        {"q": "Vad vill du göra?", "a": "zapłacić kartą"},
                        {"q": "Vilket ord betyder kort?", "a": "kartą"},
                    ],
                },
                {
                    "pl": "Nie rozumiem. Może Pan/Pani powtórzyć?",
                    "sv": "Jag förstår inte. Kan ni upprepa?",
                    "checks": [
                        {"q": "Vad ber du om?", "a": "powtórzyć"},
                        {"q": "Varför två varianter?", "a": "pan/pani = artigt tilltal"},
                    ],
                },
                {
                    "pl": "Szukam przystanku do Gdańska.",
                    "sv": "Jag letar efter hållplatsen till Gdańsk.",
                    "checks": [
                        {"q": "Vad letar du efter?", "a": "przystanku"},
                        {"q": "Till vilken plats?", "a": "Gdańska"},
                    ],
                },
                {
                    "pl": "O której godzinie jest spotkanie?",
                    "sv": "Vilken tid är mötet?",
                    "checks": [
                        {"q": "Vad handlar det om?", "a": "spotkanie"},
                        {"q": "Vilket ord signalerar klockslag?", "a": "godzinie"},
                    ],
                },
                {
                    "pl": "Dzisiaj nie mam czasu, ale jutro mogę.",
                    "sv": "Idag har jag inte tid, men imorgon kan jag.",
                    "checks": [
                        {"q": "När kan du?", "a": "jutro"},
                        {"q": "Vad säger du om idag?", "a": "nie mam czasu"},
                    ],
                },
                {
                    "pl": "Proszę mówić wolniej, uczę się polskiego.",
                    "sv": "Snälla prata långsammare, jag lär mig polska.",
                    "checks": [
                        {"q": "Vad ber du personen göra?", "a": "mówić wolniej"},
                        {"q": "Varför fungerar meningen?", "a": "du säger att du lär dig polska"},
                    ],
                },
                {
                    "pl": "To jest dla mnie za drogie.",
                    "sv": "Det är för dyrt för mig.",
                    "checks": [
                        {"q": "Vad betyder \"za drogie\"?", "a": "för dyrt"},
                        {"q": "När används det?", "a": "när något är för dyrt"},
                    ],
                },
                {
                    "pl": "Wezmę to. Poproszę paragon.",
                    "sv": "Jag tar det. Jag vill ha kvitto.",
                    "checks": [
                        {"q": "Vad bestämmer du?", "a": "wezmę to"},
                        {"q": "Vad vill du ha efteråt?", "a": "paragon"},
                    ],
                },
            ],
            "dialog_seed": {"role": "barista", "opening": "Dzień dobry! Co podać?"},
            "patterns": [
                {
                    "template": "Proszę + [sak].",
                    "examples": ["Proszę kawę.", "Proszę pomoc.", "Proszę rachunek."],
                },
                {
                    "template": "Czy mogę + [verb]...?",
                    "examples": [
                        "Czy mogę wejść?",
                        "Czy mogę zapłacić?",
                        "Czy mogę prosić o paragon?",
                    ],
                },
                {
                    "template": "Nie rozumiem / Nie wiem + [fortsättning].",
                    "examples": [
                        "Nie rozumiem.",
                        "Nie wiem, może później.",
                        "Nie rozumiem, proszę powtórzyć.",
                    ],
                }
            ],
            "start_srs": [
                {
                    "front": "najbliższy sklep",
                    "back": "närmaste butik",
                    "tags": ["starter-pack", "week-1", "day-1"],
                },
                {
                    "front": "woda niegazowana",
                    "back": "stilla vatten",
                    "tags": ["starter-pack", "week-1", "day-1"],
                },
                {
                    "front": "zapłacić kartą",
                    "back": "betala med kort",
                    "tags": ["starter-pack", "week-1", "day-1"],
                },
                {
                    "front": "powtórzyć",
                    "back": "upprepa",
                    "tags": ["starter-pack", "week-1", "day-1"],
                },
                {
                    "front": "przystanek",
                    "back": "hållplats",
                    "tags": ["starter-pack", "week-1", "day-1"],
                },
                {
                    "front": "spotkanie",
                    "back": "möte",
                    "tags": ["starter-pack", "week-1", "day-1"],
                },
                {
                    "front": "jutro",
                    "back": "imorgon",
                    "tags": ["starter-pack", "week-1", "day-1"],
                },
                {
                    "front": "wolniej",
                    "back": "långsammare",
                    "tags": ["starter-pack", "week-1", "day-1"],
                },
                {
                    "front": "za drogie",
                    "back": "för dyrt",
                    "tags": ["starter-pack", "week-1", "day-1"],
                },
                {
                    "front": "paragon",
                    "back": "kvitto",
                    "tags": ["starter-pack", "week-1", "day-1"],
                },
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
