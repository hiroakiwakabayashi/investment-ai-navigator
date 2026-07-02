from models.news import News


def collect_news() -> list[News]:
    news_list = []

    # ここに各スクレイパーを追加
    # news_list.extend(ReutersScraper().fetch())

    return news_list