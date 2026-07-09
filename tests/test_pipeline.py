from src.generator import GeneratorEngine
from src.pipeline import DomainPipeline

generator = GeneratorEngine(
    length=2,
    tlds=[".com"]
)

pipeline = DomainPipeline()

candidate = next(generator.generate())

domain = pipeline.process(candidate)

print(domain)
print(domain.to_dict())