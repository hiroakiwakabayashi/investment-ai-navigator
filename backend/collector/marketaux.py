import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MARKETAUX_API_KEY")

BASE_URL = "https://api.marketaux.com/v1/news/all"


def fetch_news():

    params = {
        "api_token": API_KEY,
        "language": "en",
        "limit": 10,
    }

    response = requests.get(BASE_URL, params=params)

    response.raise_for_status()

    return response.json()