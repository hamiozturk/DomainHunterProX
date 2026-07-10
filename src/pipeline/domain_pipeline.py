from src.services.domain_factory import DomainFactory
from src.scorer import DomainScorer
from src.checker import CheckerManager


class DomainPipeline:

    def __init__(
        self,
        min_score: int = 0,
        check_availability: bool = True,
        checker: str = "rdap",
    ):

        self.min_score = min_score
        self.check_availability = check_availability

        self.factory = DomainFactory()
        self.scorer = DomainScorer()
        self.checker = CheckerManager(checker)

    def process(self, candidate):
        """
        Tek bir domain işler.
        Geriye dönük uyumluluk korunur.
        """

        domain = self.factory.from_candidate(candidate)

        self.scorer.calculate(domain)

        if domain.score < self.min_score:
            return None

        if self.check_availability:
            self.checker.check(domain)

        return domain

    def process_many(self, candidates):
        """
        Çoklu domain işleme.
        RDAP ThreadPool'u burada kullanılır.
        """

        domains = []

        # Domain oluştur + skorla
        for candidate in candidates:

            domain = self.factory.from_candidate(candidate)

            self.scorer.calculate(domain)

            if domain.score < self.min_score:
                continue

            domains.append(domain)

        if not domains:
            return []

        # Toplu RDAP kontrolü
        if self.check_availability:

            if hasattr(self.checker.checker, "check_many"):

                self.checker.checker.check_many(domains)

            else:
                # Eski checker'lar için fallback
                for domain in domains:
                    self.checker.check(domain)

        return domains