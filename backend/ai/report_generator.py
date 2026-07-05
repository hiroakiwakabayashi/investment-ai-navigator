from datetime import date

from backend.models.report import Report
from backend.ai.investment_score import calculate_score


def generate_report(news_list, report_type: str):

    bullish = 0
    bearish = 0
    neutral = 0

    risk_total = 0
    importance_total = 0

    sector_map = {}
    top_news = []

    for n in news_list:

        sentiment = n.get("sentiment", "Neutral")
        importance = float(n.get("importance", 0))
        risk = float(n.get("risk", 0))

        # sentiment集計
        if sentiment == "Positive":
            bullish += 1
        elif sentiment == "Negative":
            bearish += 1
        else:
            neutral += 1

        # risk / importance
        risk_total += risk
        importance_total += importance

        # sectors集計
        sectors = n.get("sectors") or []

        # DBに文字列で保存されている場合の対応
        if isinstance(sectors, str):
            sectors = [s.strip() for s in sectors.split(",") if s.strip()]

        for s in sectors:
            sector_map[s] = sector_map.get(s, 0) + 1

        # 重要ニュース抽出
        if importance >= 70:
            top_news.append(n.get("summary", ""))

    total = len(news_list)

    # -----------------------------
    # 市場センチメント
    # -----------------------------
    if bullish > bearish:
        market_sentiment = "bullish"
    elif bearish > bullish:
        market_sentiment = "bearish"
    else:
        market_sentiment = "neutral"

    # -----------------------------
    # リスクレベル
    # -----------------------------
    avg_risk = risk_total / total if total else 0

    if avg_risk >= 70:
        risk_level = "high"
    elif avg_risk >= 40:
        risk_level = "medium"
    else:
        risk_level = "low"

    # -----------------------------
    # セクターTop3
    # -----------------------------
    top_sectors = sorted(
        sector_map.items(),
        key=lambda x: x[1],
        reverse=True
    )[:3]

    # -----------------------------
    # Summary
    # -----------------------------
    summary = f"""
Analyzed {total} news items.

Bullish : {bullish}
Bearish : {bearish}
Neutral : {neutral}

Top sectors:
{top_sectors}
"""

    # -----------------------------
    # Outlook
    # -----------------------------
    outlook = f"""
Market sentiment : {market_sentiment}

Risk level : {risk_level}

Average risk score : {avg_risk:.1f}

Focus sectors :
{top_sectors}
"""

    # -----------------------------
    # Investment Score
    # -----------------------------
    investment_score, investment_level = calculate_score(news_list)

    # -----------------------------
    # Report生成
    # -----------------------------
    return Report(

        report_date=str(date.today()),
        market="US",
        report_type=report_type,

        title=f"{report_type.upper()} MARKET REPORT",

        summary=summary,
        outlook=outlook,

        market_sentiment=market_sentiment,
        risk_level=risk_level,

        bullish_score=bullish,
        bearish_score=bearish,

        investment_score=investment_score,
        investment_level=investment_level,
    )