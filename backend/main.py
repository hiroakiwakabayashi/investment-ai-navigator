from usecases.collect_news import collect_news
from usecases.analyze_news import analyze_news
from jobs.hourly_job import run


def main():

    run()


if __name__ == "__main__":
    main()

# def main():

#     print("=" * 50)
#     print("Investment AI Navigator")
#     print("=" * 50)

#     collect_news()
#     analyze_news()


# if __name__ == "__main__":
#     main()

