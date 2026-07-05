from usecases.collect_news import collect_news
from usecases.analyze_news import analyze_news
from jobs.report_job import generate_report

def run():

    print("=== Hourly Job Start ===")

    collect_news()

    analyze_news()

    generate_report("night")

    print("=== Hourly Job End ===")