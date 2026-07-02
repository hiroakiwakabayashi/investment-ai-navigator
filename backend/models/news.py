from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4


@dataclass
class News:
    id: str
    title: str
    url: str
    source: str
    published_at: datetime | None = None
    content: str | None = None
    summary: str | None = None