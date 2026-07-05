from backend.database.report_repository import get_report_history


def execute(limit: int = 20):
    return get_report_history(limit)