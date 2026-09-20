BUDGET_SCORES = {
    "Under $20k": 0,
    "$20k–$50k": 1,
    "$50k–$150k": 2,
    "$150k+": 3,
}

TIMELINE_SCORES = {
    "Just exploring": 0,
    "Within 3 months": 1,
    "Within 1 month": 2,
    "Ready now": 3,
}

BUDGET_REASONS = {
    "Under $20k": "Low budget",
    "$20k–$50k": "Lower budget",
    "$50k–$150k": "Medium budget",
    "$150k+": "High budget",
}

TIMELINE_REASONS = {
    "Just exploring": "Just exploring",
    "Within 3 months": "Within 3 months",
    "Within 1 month": "Within 1 month",
    "Ready now": "Ready now",
}


def score_lead(service, budget, timeline, notes=""):
    score = BUDGET_SCORES.get(budget, 0) + TIMELINE_SCORES.get(timeline, 0)

    reasons = [
        TIMELINE_REASONS.get(timeline, "Timeline not specified"),
        BUDGET_REASONS.get(budget, "Budget not specified"),
    ]

    if score >= 5:
        priority = "high"
    elif score >= 3:
        priority = "medium"
    else:
        priority = "low"

    return {
        "priority": priority,
        "reasons": reasons,
    }
