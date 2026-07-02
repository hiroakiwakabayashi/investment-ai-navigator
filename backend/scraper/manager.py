from scraper.reuters import ReutersScraper
from models.news import News


def collect_news() -> list[News]:

    news = []

    news.extend(
        ReutersScraper().fetch()
    )

    return news