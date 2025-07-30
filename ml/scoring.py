def ai_score_loan(phone_number, amount):
    # Simulated scoring: smaller amounts = higher chance
    score = 100 - (amount / 100)  # e.g. 500 ETB = score 95
    score = max(30, min(score, 95))  # Clamp score
    return score
