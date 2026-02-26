def calculate_ratios(data):
    return {
        "profit_margin": round(data["net_income"] / data["revenue"], 4),
        "current_ratio": round(data["current_assets"] / data["current_liabilities"], 4),
        "debt_to_equity": round(data["total_liabilities"] / data["equity"], 4),
        "roa": round(data["net_income"] / data["total_assets"], 4),
        "roe": round(data["net_income"] / data["equity"], 4),
        "asset_turnover": round(data["revenue"] / data["total_assets"], 4),
        "equity_ratio": round(data["equity"] / data["total_assets"], 4)
    }

def yoy_growth(current, previous):
    return {
        "revenue_growth_%": round(((current["revenue"] - previous["revenue"]) / previous["revenue"]) * 100, 2),
        "net_income_growth_%": round(((current["net_income"] - previous["net_income"]) / previous["net_income"]) * 100, 2),
        "asset_growth_%": round(((current["total_assets"] - previous["total_assets"]) / previous["total_assets"]) * 100, 2)
    }

def calculate_financial_health_score(current_ratios, growth):

    roe = current_ratios["roe"]
    profit_margin = current_ratios["profit_margin"]
    current_ratio = current_ratios["current_ratio"]
    de_ratio = current_ratios["debt_to_equity"]
    revenue_growth = growth["revenue_growth_%"] / 100  # convert to decimal

    # Weighted composite scoring
    score = (
        roe * 25 +
        profit_margin * 20 +
        (1 / de_ratio) * 15 +
        revenue_growth * 20 +
        current_ratio * 20
    )

    final_score = round(min(score, 100), 2)

    if final_score >= 75:
        rating = "Strong"
    elif final_score >= 50:
        rating = "Moderate"
    else:
        rating = "Weak"

    return {
        "financial_health_score": final_score,
        "rating": rating
    }