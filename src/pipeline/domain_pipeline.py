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

        domain = self.factory.from_candidate(candidate)

        self.scorer.calculate(domain)

        # Skoru düşükse devam etme
        if domain.score < self.min_score:
            return None

        # RDAP isteği opsiyonel
        if self.check_availability:
            self.checker.check(domain)

        return domain