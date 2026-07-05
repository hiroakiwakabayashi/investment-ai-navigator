from backend.database.report_repository import get_latest_report


def execute():
    return get_latest_report()