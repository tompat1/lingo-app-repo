from __future__ import annotations

from .contracts import DailySession

SAMPLE_CAFE_FORMAL = DailySession.model_validate({
    "mission": "Beställa på café med rätt artighet",
    "scene": "cafe",
    "tone": "formal",
    "sentences": [
        {
            "pl": "Dzień dobry, poproszę kawę z mlekiem.",
            "sv": "God dag, jag vill ha kaffe med mjölk.",
            "checks": [
                {"q": "Vad beställer du?", "a": "kawę z mlekiem"},
                {"q": "Är tonen formell?", "a": "ja"}
            ]
        }
    ],
    "dialog_seed": {"role": "barista", "opening": "Dzień dobry! Co podać?"},
    "patterns": [
        {"template": "Poproszę + [sak].", "examples": ["Poproszę wodę.", "Poproszę rachunek."]}
    ]
})
