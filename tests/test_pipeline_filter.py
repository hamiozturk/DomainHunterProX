from src.generator import GeneratorEngine
from src.pipeline import DomainPipeline


generator = GeneratorEngine(
    length=2,
    tlds=[".com"]
)

pipeline = DomainPipeline(
    min_score=95
)

count = 0

for candidate in generator.generate():

    domain = pipeline.process(candidate)

    if domain is None:
        continue

    print(domain.name, domain.score)

    count += 1

    if count == 10:
        break