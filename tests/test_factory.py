from src.generator import GeneratorEngine
from src.services.domain_factory import DomainFactory

generator = GeneratorEngine(
    length=2,
    tlds=[".com"]
)

candidate = next(generator.generate())

print("Candidate")
print(candidate)

print()

domain = DomainFactory.from_candidate(candidate)

print("Domain")
print(domain)

print()

print(domain.to_dict())