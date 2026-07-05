from models.report import Report
from datetime import date


def generate_report(news_list, report_type: str):

    bullish = 0
    bearish = 0

    sentiment_map = {
        "Positive": 1,
        "Neutral": 0,
        "Negative": -1
    }

    for n in news_list:

        raw = n.get("sentiment", "Neutral")
        sentiment = sentiment_map.get(raw, 0)

        if sentiment > 0:
            bullish += 1
        else:
            bearish += 1

    total = len(news_list)

    market_sentiment = (
        "bullish" if bullish > bearish
        else "bearish" if bearish > bullish
        else "neutral"
    )

    return Report(

        report_date=str(date.today()),
        market="US",
        report_type=report_type,

        title=f"{report_type.upper()} MARKET REPORT",

        summary=f"{total} news analyzed",

        outlook="Market outlook based on sentiment analysis",

        market_sentiment=market_sentiment,
        risk_level="medium",

        bullish_score=bullish,
        bearish_score=bearish
    )