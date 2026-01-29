from __future__ import annotations

from .contracts import SceneImage, ScenePack, Scenario

SAMPLE_SCENARIOS = [
    Scenario(id="cafe", name_sv="Cafébesök", tags=["mat", "beställa"]),
    Scenario(id="pharmacy", name_sv="Apotek", tags=["hälsa", "inköp"]),
]

SAMPLE_SCENES = {
    "cafe": ScenePack(
        scenario_id="cafe",
        name_sv="Cafébesök",
        images=[
            SceneImage(
                url="https://images.example.com/scenes/cafe-1.jpg",
                alt="Ett café med disk och kaffemaskin",
            ),
            SceneImage(
                url="https://images.example.com/scenes/cafe-2.jpg",
                alt="En barista som serverar kaffe",
            ),
        ],
    ),
    "pharmacy": ScenePack(
        scenario_id="pharmacy",
        name_sv="Apotek",
        images=[
            SceneImage(
                url="https://images.example.com/scenes/pharmacy-1.jpg",
                alt="En apoteksdisk med hyllor",
            ),
            SceneImage(
                url="https://images.example.com/scenes/pharmacy-2.jpg",
                alt="En farmaceut som ger råd",
            ),
        ],
    ),
}
