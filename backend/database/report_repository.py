from database.client import supabase


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
        "bearish_score": report.bearish_score

    }).execute()