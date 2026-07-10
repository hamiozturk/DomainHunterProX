from src.generator import GeneratorEngine
from src.pipeline import DomainPipeline


def test_pipeline_many():

    generator = GeneratorEngine(
        length=2,
        tlds=[".com"]
    )

    pipeline = DomainPipeline(
        min_score=90,
        check_availability=True,
        checker="rdap",
    )

    candidates = []

    for i, candidate in enumerate(generator.generate()):

        candidates.append(candidate)

        if i == 49:
            break

    domains = pipeline.process_many(candidates)

    for domain in domains:

        print(
            f"{domain.name} | "
            f"Score={domain.score} | "
            f"Available={domain.available} | "
            f"Status={domain.check_status}"
        )

    print("\nToplam:", len(domains))

    print("\nRDAP Statistics:")

    print(
        pipeline.checker.checker.engine.stats.report()
    )


if __name__ == "__main__":
    test_pipeline_many()