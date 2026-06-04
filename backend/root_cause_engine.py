def get_business_insights(df):

    top_route = (
        df.groupby("Route_Name")["Revenue"]
        .sum()
        .idxmax()
    )

    worst_route = (
        df.groupby("Route_Name")["Profit"]
        .sum()
        .idxmin()
    )

    best_booking_source = (
        df.groupby("Booking_Source")["Revenue"]
        .sum()
        .idxmax()
    )

    worst_booking_source = (
        df.groupby("Booking_Source")["Revenue"]
        .sum()
        .idxmin()
    )

    insights = {
        "total_revenue": df["Revenue"].sum(),
        "total_profit": df["Profit"].sum(),
        "avg_occupancy": df["Occupancy_Percentage"].mean(),
        "avg_delay": df["Delay_Minutes"].mean(),
        "avg_rating": df["Customer_Rating"].mean(),
        "avg_profit_margin": df["Profit_Margin_Percentage"].mean(),
        "fuel_cost_pct": (
            df["Fuel_Cost"].sum()
            / df["Revenue"].sum()
        ) * 100,
        "top_route": top_route,
        "worst_route": worst_route,
        "best_booking_source": best_booking_source,
        "worst_booking_source": worst_booking_source
    }

    return insights