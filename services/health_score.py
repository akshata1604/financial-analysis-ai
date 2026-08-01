def calculate_health_score(ratios):

    score = 0

    # Profit Margin
    if ratios["profit_margin"] >= 10:
        score += 20

    # Current Ratio
    if ratios["current_ratio"] >= 1.5:
        score += 20

    # Debt to Equity
    if ratios["debt_to_equity"] <= 1:
        score += 20

    # ROA
    if ratios["roa"] >= 5:
        score += 20

    # ROE
    if ratios["roe"] >= 15:
        score += 20

    if score >= 80:
        rating = "Excellent"

    elif score >= 60:
        rating = "Good"

    elif score >= 40:
        rating = "Average"

    else:
        rating = "Poor"

    return {
        "score": score,
        "rating": rating
    }