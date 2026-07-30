from rubric import MAX_SCORE

def score_lead(lead):
    message = lead["message"].lower()

    score = 0

    # Budget
    if "budget approved" in message or "500" in message:
        score += 20
    elif "budget" in message:
        score += 10

    # Urgency
    if "urgent" in message or "immediately" in message or "two weeks" in message:
        score += 15

    # Industry Fit
    score += 15

    # Company Size
    if any(word in message for word in ["enterprise", "500", "100"]):
        score += 15
    else:
        score += 8

    # Purchase Intent
    if any(word in message for word in ["need", "looking", "interested"]):
        score += 15

    # Decision Maker
    if "manager" in message or "procurement" in message:
        score += 10

    # Message Quality
    if len(message) > 40:
        score += 10
    else:
        score += 5

    score = min(score, MAX_SCORE)

    # Recommended Action
    if score >= 85:
        action = "Contact immediately"
    elif score >= 70:
        action = "Schedule product demo"
    elif score >= 50:
        action = "Follow up by email"
    else:
        action = "Keep in nurture campaign"

    return score, action