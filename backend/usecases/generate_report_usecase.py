from ai.report_generator import generate_report
from database.analysis_repository import get_completed_analysis
from database.report_repository import save_report


def execute(report_type: str):

    news = get_completed_analysis()

    report = generate_report(news, report_type)

    save_report(report)