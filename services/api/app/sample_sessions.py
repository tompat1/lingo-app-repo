from __future__ import annotations

from .contracts import DailySession

SAMPLE_CAFE_FORMAL = DailySession.model_validate({
    "mission": "Vecka 1: överlevnad & artighet (startpaket)",
    "scene": "cafe",
    "tone": "formal",
    "sentences": [
        {
            "pl": "Przepraszam, gdzie jest najbliższy sklep?",
            "sv": "Ursäkta, var är närmaste butik?",
            "checks": [
                {"q": "Vad frågar du efter?", "a": "najbliższy sklep"},
                {"q": "Vad betyder \"najbliższy\"?", "a": "närmast"}
            ]
        }
    ],
    "dialog_seed": {"role": "barista", "opening": "Dzień dobry! Co podać?"},
    "patterns": [
        {"template": "Proszę + [sak].", "examples": ["Proszę kawę.", "Proszę pomoc.", "Proszę rachunek."]},
        {
            "template": "Czy mogę + [verb]...?",
            "examples": ["Czy mogę wejść?", "Czy mogę zapłacić?", "Czy mogę prosić o paragon?"]
        }
    ]
})
