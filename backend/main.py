from collector.marketaux import fetch_news


def main():

    news = fetch_news()

    print("=" * 50)

    print(f"取得件数：{len(news['data'])}")

    print("=" * 50)

    for article in news["data"]:

        print(article["title"])
        print(article["source"])
        print(article["published_at"])

        print("-" * 50)


if __name__ == "__main__":
    main()