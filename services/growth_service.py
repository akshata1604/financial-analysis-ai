def calculate_growth(current, previous):

    growth = {}

    metrics = [
        "revenue",
        "net_income",
        "total_assets",
        "total_liabilities",
        "total_equity"
    ]

    for metric in metrics:

        current_value = float(current[metric])
        previous_value = float(previous[metric])

        if previous_value == 0:
            growth[metric] = None
        else:
            growth[metric] = round(
                ((current_value - previous_value) / previous_value) * 100,
                2
            )

    return growth