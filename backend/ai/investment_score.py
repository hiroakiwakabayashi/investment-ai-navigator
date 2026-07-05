def calculate_score(news_list):

    score = 50

    bullish = 0
    bearish = 0

    total_importance = 0
    total_risk = 0
    emergency = 0

    for n in news_list:

        sentiment = str(n.get("sentiment", "")).lower()

        if sentiment == "bullish":
            bullish += 1
        elif sentiment == "bearish":
            bearish += 1

        total_importance += int(n.get("importance", 50))
        total_risk += int(n.get("risk", 50))

        if n.get("emergency"):
            emergency += 1

    count = max(len(news_list), 1)

    avg_importance = total_importance / count
    avg_risk = total_risk / count

    # 市場センチメント
    score += (bullish - bearish) * 3

    # 重要ニュース
    score += (avg_importance - 50) * 0.2

    # リスク
    score -= (avg_risk - 50) * 0.3

    # 緊急ニュース
    score -= emergency * 5

    score = max(0, min(100, round(score)))

    if score >= 90:
        level = "Strong Buy"
    elif score >= 75:
        level = "Buy"
    elif score >= 60:
        level = "Watch"
    elif score >= 40:
        level = "Caution"
    else:
        level = "Sell"

    return score, level