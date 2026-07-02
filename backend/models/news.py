from dataclasses import dataclass
from datetime import datetime


@dataclass
class News:
    title: str
    url: str
    source: str
    published_at: datetime | None = None
    content: str | None = None
    summary: str | None = None