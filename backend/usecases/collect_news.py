from collector.marketaux import fetch_news
from backend.database.news_repository import save_news


def collect_news():

    news_list = fetch_news()

    print("=" * 50)
    print(f"取得件数：{len(news_list)}")

    save_news(news_list)

    print("ニュース保存完了")
    print("=" * 50)