from ai.analyzer import analyze
from database.analysis_repository import save_analysis
from database.news_repository import (
    get_waiting_news,
    complete_analysis
)


def analyze_news():

    waiting_news = get_waiting_news()

    print(f"分析対象：{len(waiting_news)}件")

    for news in waiting_news:

        result = analyze(news)

        save_analysis(result)

        complete_analysis(news["id"])

    print("分析完了")