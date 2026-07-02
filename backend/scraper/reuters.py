import feedparser

from models.news import News
from scraper.base import BaseScraper


class ReutersScraper(BaseScraper):

    RSS_URL = "https://feeds.reuters.com/reuters/businessNews"

    def fetch(self) -> list[News]:

        feed = feedparser.parse(self.RSS_URL)

        news_list = []

        for entry in feed.entries:

            news = News(
                id=entry.get("id", entry.link),
                title=entry.title,
                url=entry.link,
                source="Reuters",
                published_at=None,
                content=None,
                summary=None,
            )

            news_list.append(news)

        return news_list