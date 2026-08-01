def calculate_ratios(financials):

    revenue = float(financials["revenue"])
    net_income = float(financials["net_income"])
    total_assets = float(financials["total_assets"])
    total_liabilities = float(financials["total_liabilities"])
    total_equity = float(financials["total_equity"])
    current_assets = float(financials["current_assets"])
    current_liabilities = float(financials["current_liabilities"])

    ratios = {

        "profit_margin": round((net_income / revenue) * 100, 2),

        "current_ratio": round(current_assets / current_liabilities, 2),

        "debt_to_equity": round(total_liabilities / total_equity, 2),

        "roa": round((net_income / total_assets) * 100, 2),

        "roe": round((net_income / total_equity) * 100, 2)

    }

    return ratios