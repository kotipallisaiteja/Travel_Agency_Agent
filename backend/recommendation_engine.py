# backend/recommendation_engine.py

def generate_recommendations(insights):

    recommendations = []

    # Occupancy

    avg_occupancy = insights.get("avg_occupancy", 0)

    if avg_occupancy < 70:
        recommendations.append(
            "Launch route-specific promotions to improve seat occupancy."
        )

    # Delays

    avg_delay = insights.get("avg_delay", 0)

    if avg_delay > 20:
        recommendations.append(
            "Optimize route scheduling and investigate major delay hotspots."
        )

    # Customer Ratings

    avg_rating = insights.get("avg_rating", 0)

    if avg_rating < 4:
        recommendations.append(
            "Improve customer experience through better service quality and punctuality."
        )

    # Profit Margin

    avg_profit_margin = insights.get("avg_profit_margin", 0)

    if avg_profit_margin < 15:
        recommendations.append(
            "Reduce operational costs and improve route profitability."
        )

    # Fuel Cost

    fuel_cost_pct = insights.get("fuel_cost_pct", 0)

    if fuel_cost_pct > 40:
        recommendations.append(
            "Review fuel consumption patterns and optimize route efficiency."
        )

    # Revenue

    total_revenue = insights.get("total_revenue", 0)

    if total_revenue > 0:
        recommendations.append(
            "Focus marketing efforts on high-performing routes and customer segments."
        )

    if not recommendations:
        recommendations.append(
            "Business performance is healthy. Continue monitoring key operational metrics."
        )

    return recommendations