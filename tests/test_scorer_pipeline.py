from src.generator import GeneratorEngine
from src.services.domain_factory import DomainFactory
from src.scorer import DomainScorer

generator = GeneratorEngine(
    length=2,
    tlds=[".com"]
)

candidate = next(generator.generate())

domain = DomainFactory.from_candidate(candidate)

scorer = DomainScorer()

scorer.calculate(domain)

print(domain)

print(domain.to_dict())