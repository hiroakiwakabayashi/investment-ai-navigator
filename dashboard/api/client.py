import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("API_URL")


def _get(endpoint: str):
    """
    共通GET処理
    """

    response = requests.get(
        f"{BASE_URL}{endpoint}",
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def get_latest_report():
    return _get("/reports/latest")


def get_report_history():
    return _get("/reports/history")