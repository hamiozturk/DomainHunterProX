from src.generator import GeneratorEngine
from src.services.domain_factory import DomainFactory
from src.scorer import DomainScorer
from src.checker.rdap import RDAPChecker


generator = GeneratorEngine(
    length=2,
    tlds=[".com"]
)

candidate = next(generator.generate())

domain = DomainFactory.from_candidate(candidate)

scorer = DomainScorer()
checker = RDAPChecker()

scorer.calculate(domain)
checker.check(domain)

print(domain)
print()
print(domain.to_dict())