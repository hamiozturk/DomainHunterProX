from src.services.domain_factory import DomainFactory
from src.scorer import DomainScorer
from src.checker.rdap import RDAPChecker


class DomainPipeline:

    def __init__(self):

        self.factory = DomainFactory()
        self.scorer = DomainScorer()
        self.checker = RDAPChecker()

    def process(self, candidate):

        domain = self.factory.from_candidate(candidate)

        self.scorer.calculate(domain)

        self.checker.check(domain)

        return domain