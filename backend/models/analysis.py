from dataclasses import dataclass


@dataclass
class Analysis:

    summary: str

    importance: int

    risk: int

    sentiment: str

    sectors: list[str]

    companies: list[str]

    countries: list[str]