from abc import ABC, abstractmethod
from models.news import News


class BaseScraper(ABC):

    @abstractmethod
    def fetch(self) -> list[News]:
        pass