import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scoring import score_lead


def test_high_priority():
    result = score_lead(
        "Renovation",
        "$50k–$150k",
        "Ready now",
        "Any notes here"
    )
    assert result["priority"] == "high"


def test_medium_priority():
    result = score_lead(
        "Extension",
        "$20k–$50k",
        "Within 1 month",
        ""
    )
    assert result["priority"] == "medium"


def test_low_priority():
    result = score_lead(
        "Consultation",
        "Under $20k",
        "Just exploring",
        ""
    )
    assert result["priority"] == "low"


def test_notes_do_not_affect_scoring():
    a = score_lead(
        "Renovation",
        "$20k–$50k",
        "Within 1 month",
        ""
    )
    b = score_lead(
        "Renovation",
        "$20k–$50k",
        "Within 1 month",
        "heritage developer family very detailed notes"
    )
    assert a == b


if __name__ == "__main__":
    test_high_priority()
    print("high OK")

    test_medium_priority()
    print("medium OK")

    test_low_priority()
    print("low OK")

    test_notes_do_not_affect_scoring()
    print("notes independence OK")

    print("All tests passed.")
