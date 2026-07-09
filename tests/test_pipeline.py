from src.generator import GeneratorEngine
from src.pipeline import DomainPipeline


generator = GeneratorEngine(
    length=2,
    tlds=[".com"]
)

pipeline = DomainPipeline(
    min_score=0,
    check_availability=False,
    checker="rdap",
)

count = 0

for candidate in generator.generate():

    domain = pipeline.process(candidate)

    if domain is None:
        continue

    print(
        f"{domain.name} | "
        f"Score={domain.score} | "
        f"Available={domain.available} | "
        f"Status={domain.check_status}"
    )

    count += 1

    if count == 10:
        break