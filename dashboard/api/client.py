import requests

BASE_URL = "http://localhost:8000"


def get_report_history():
    response = requests.get(f"{BASE_URL}/reports/history", timeout=10)
    response.raise_for_status()
    return response.json()