import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scoring import score_lead


def test_high_priority():
    result = score_lead(
        "Renovation",
        "$150k+",
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


def test_scoring_thresholds():
    # High = 5-6
    h = score_lead("X", "$150k+", "Ready now", "")
    assert h["priority"] == "high"
    # Medium = 3-4
    m = score_lead("X", "$20k–$50k", "Within 1 month", "")
    assert m["priority"] == "medium"
    # Low = 0-2
    l = score_lead("X", "Under $20k", "Just exploring", "")
    assert l["priority"] == "low"


def test_python_scoring_matches_intended_thresholds():
    # Ready now (3) + $150k+ (3) = 6 -> high
    assert score_lead("S", "$150k+", "Ready now", "")["priority"] == "high"
    # Within 1 month (2) + $50k-$150k (2) = 4 -> medium
    assert score_lead("S", "$50k–$150k", "Within 1 month", "")["priority"] == "medium"
    # Just exploring (0) + Under $20k (0) = 0 -> low
    assert score_lead("S", "Under $20k", "Just exploring", "")["priority"] == "low"


if __name__ == "__main__":
    test_high_priority()
    print("high OK")
    test_medium_priority()
    print("medium OK")
    test_low_priority()
    print("low OK")
    test_notes_do_not_affect_scoring()
    print("notes independence OK")
    test_scoring_thresholds()
    print("thresholds OK")
    test_python_scoring_matches_intended_thresholds()
    print("python thresholds match OK")
    print("All tests passed.")
