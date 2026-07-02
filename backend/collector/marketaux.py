import os

import requests
from dotenv import load_dotenv

from models.news import News

load_dotenv()

API_KEY = os.getenv("MARKETAUX_API_KEY")

BASE_URL = "https://api.marketaux.com/v1/news/all"


def fetch_news() -> list[News]:

    params = {
        "api_token": API_KEY,
        "language": "en",
        "limit": 10,
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    news_list = []

    for article in response.json()["data"]:

        news = News(
            id=article.get("uuid", article["url"]),
            title=article["title"],
            url=article["url"],
            source=article["source"],
            published_at=article["published_at"],
            content=article.get("description"),
            summary=None,
        )

        news_list.append(news)

    return news_list
