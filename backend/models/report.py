from dataclasses import dataclass

@dataclass
class Report:

    report_date: str
    market: str
    report_type: str

    title: str
    summary: str
    outlook: str

    market_sentiment: str
    risk_level: str

    bullish_score: int
    bearish_score: int

    investment_score: int
    investment_level: str