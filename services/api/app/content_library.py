from __future__ import annotations

from datetime import date
from typing import Dict, List, Tuple

from .contracts import DailySession

PolishPackKey = Tuple[str, str]

POLISH_PACK_V1: Dict[PolishPackKey, List[dict]] = {
    ("cafe", "formal"): [
        {
            "mission": "Café dag 1: beställa artigt och tydligt",
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
                {
                    "pl": "Poproszę cappuccino.",
                    "sv": "Jag vill ha en cappuccino.",
                    "checks": [{"q": "Vad beställer du?", "a": "cappuccino"}],
                },
                {
                    "pl": "Chciałbym małą kawę na miejscu.",
                    "sv": "Jag skulle vilja ha en liten kaffe här.",
                },
                {
                    "pl": "Czy macie ciasto marchewkowe?",
                    "sv": "Har ni morotskaka?",
                },
                {
                    "pl": "Poproszę szklankę wody.",
                    "sv": "Jag vill ha ett glas vatten.",
                },
                {
                    "pl": "Czy mogę zapłacić kartą?",
                    "sv": "Kan jag betala med kort?",
                },
                {
                    "pl": "Dziękuję bardzo.",
                    "sv": "Tack så mycket.",
                },
                {
                    "pl": "Przepraszam, gdzie jest toaleta?",
                    "sv": "Ursäkta, var är toaletten?",
                },
                {
                    "pl": "Czy to jest świeże?",
                    "sv": "Är det här färskt?",
                },
                {
                    "pl": "Poproszę herbatę z cytryną.",
                    "sv": "Jag vill ha te med citron.",
                },
                {
                    "pl": "Czy mogę dostać cukier?",
                    "sv": "Kan jag få socker?",
                },
                {
                    "pl": "Bez cukru, proszę.",
                    "sv": "Utan socker, tack.",
                },
                {
                    "pl": "Wezmę kanapkę z serem.",
                    "sv": "Jag tar en smörgås med ost.",
                },
                {
                    "pl": "Czy macie mleko roślinne?",
                    "sv": "Har ni växtmjölk?",
                },
                {
                    "pl": "Poproszę jedno espresso.",
                    "sv": "Jag vill ha en espresso.",
                },
                {
                    "pl": "Czy to jest na wynos?",
                    "sv": "Är det här för avhämtning?",
                },
                {
                    "pl": "Poproszę dwie kawy.",
                    "sv": "Jag vill ha två kaffe.",
                },
                {
                    "pl": "Ile to kosztuje?",
                    "sv": "Hur mycket kostar det?",
                },
                {
                    "pl": "Czy mogę prosić o paragon?",
                    "sv": "Kan jag få kvittot?",
                },
                {
                    "pl": "Dzień dobry, poproszę stolik przy oknie.",
                    "sv": "God dag, jag vill ha ett bord vid fönstret.",
                },
                {
                    "pl": "Czy jest wolne miejsce?",
                    "sv": "Finns det en ledig plats?",
                },
                {
                    "pl": "Poproszę menu, proszę.",
                    "sv": "Jag vill ha menyn, tack.",
                },
                {
                    "pl": "Chciałbym zapłacić osobno.",
                    "sv": "Jag skulle vilja betala separat.",
                },
                {
                    "pl": "Proszę o podgrzanie tej kanapki.",
                    "sv": "Kan ni värma den här smörgåsen?",
                },
                {
                    "pl": "Czy macie coś bezglutenowego?",
                    "sv": "Har ni något glutenfritt?",
                },
                {
                    "pl": "Poproszę lód do napoju.",
                    "sv": "Jag vill ha is till drycken.",
                },
                {
                    "pl": "To wszystko, dziękuję.",
                    "sv": "Det var allt, tack.",
                },
                {
                    "pl": "Czy mogę prosić o chwilę?",
                    "sv": "Kan jag få en liten stund?",
                },
                {
                    "pl": "Smakuje bardzo dobrze.",
                    "sv": "Det smakar väldigt gott.",
                },
            ],
            "dialog_seed": {"role": "barista", "opening": "Dzień dobry! Co podać?"},
            "patterns": [
                {
                    "template": "Poproszę + [sak].",
                    "examples": ["Poproszę wodę.", "Poproszę rachunek."],
                }
            ],
            "start_srs": [
                {
                    "front": "kawa z mlekiem",
                    "back": "kaffe med mjölk",
                    "tags": ["starter-pack", "cafe", "day-1"],
                },
                {
                    "front": "rachunek",
                    "back": "nota",
                    "tags": ["starter-pack", "cafe", "day-1"],
                },
                {
                    "front": "płacić kartą",
                    "back": "betala med kort",
                    "tags": ["starter-pack", "cafe", "day-1"],
                },
                {
                    "front": "na wynos",
                    "back": "för avhämtning",
                    "tags": ["starter-pack", "cafe", "day-1"],
                },
                {
                    "front": "cukier",
                    "back": "socker",
                    "tags": ["starter-pack", "cafe", "day-1"],
                },
                {
                    "front": "mleko roślinne",
                    "back": "växtmjölk",
                    "tags": ["starter-pack", "cafe", "day-1"],
                },
                {
                    "front": "paragon",
                    "back": "kvitto",
                    "tags": ["starter-pack", "cafe", "day-1"],
                },
                {
                    "front": "stolik przy oknie",
                    "back": "bord vid fönstret",
                    "tags": ["starter-pack", "cafe", "day-1"],
                },
                {
                    "front": "bezglutenowy",
                    "back": "glutenfri",
                    "tags": ["starter-pack", "cafe", "day-1"],
                },
                {
                    "front": "menu",
                    "back": "meny",
                    "tags": ["starter-pack", "cafe", "day-1"],
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
