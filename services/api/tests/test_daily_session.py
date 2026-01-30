from datetime import date

from app.content_library import generate_daily_session


def test_generate_daily_session_week1_starter_pack() -> None:
    session = generate_daily_session("cafe", "formal", date(2024, 1, 1))

    assert session.mission.startswith("Vecka 1: överlevnad")
    assert session.scene == "cafe"
    assert session.tone == "formal"
    assert len(session.sentences) == 10
    assert any(pattern.template.startswith("Proszę") for pattern in session.patterns or [])
