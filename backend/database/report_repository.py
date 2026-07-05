from backend.database.client import supabase


def save_report(report):

    supabase.table("reports").insert({
        "report_date": report.report_date,
        "market": report.market,
        "report_type": report.report_type,
        "title": report.title,
        "summary": report.summary,
        "outlook": report.outlook,
        "market_sentiment": report.market_sentiment,
        "risk_level": report.risk_level,
        "bullish_score": report.bullish_score,
        "bearish_score": report.bearish_score,
        "investment_score": report.investment_score,
        "investment_level": report.investment_level,
    }).execute()


def get_latest_report():

    response = (
        supabase.table("reports")
        .select("*")
        .order("created_at", desc=True)
        .limit(1)
        .execute()
    )

    return response.data[0] if response.data else None
def get_report_history(limit: int = 20):

    response = (
        supabase.table("reports")
        .select("*")
        .order("created_at", desc=True)
        .limit(limit)
        .execute()
    )

    return response.data