def analyze(news):

    return {
        "news_id": news["id"],
        "summary": f"Dummy Summary: {news['title']}",
        "importance": 50,
        "risk": 20,
        "sentiment": "Neutral",
        "companies": [],
        "countries": [],
        "sectors": [],
        "emergency": False
    }