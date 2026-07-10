from src.generator import GeneratorEngine
from src.pipeline import DomainPipeline
from src.exporter import CSVExporter


def test_csv_exporter():

    generator = GeneratorEngine(
        length=2,
        tlds=[".com"]
    )

    pipeline = DomainPipeline(
        min_score=90,
        check_availability=True,
        checker="rdap"
    )

    candidates = []

    for i, candidate in enumerate(generator.generate()):

        candidates.append(candidate)

        if i == 19:
            break

    domains = pipeline.process_many(candidates)

    exporter = CSVExporter()

    filename = exporter.export(
        domains,
        "output/domains.csv"
    )

    print(f"\nCSV oluşturuldu: {filename}")

    print(f"Toplam kayıt: {len(domains)}")


if __name__ == "__main__":
    test_csv_exporter()