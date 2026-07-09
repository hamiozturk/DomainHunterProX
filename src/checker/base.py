from abc import ABC, abstractmethod

from src.models.domain import Domain


class BaseChecker(ABC):

    name = "base"

    @abstractmethod
    def check(self, domain: Domain) -> None:
        """
        Domain nesnesini kontrol eder ve sonucu nesneye yazar.
        """
        raise NotImplementedError