from src.generator import GeneratorEngine
from src.pipeline import DomainPipeline
from src.exporter import CsvExporter


def main():

    generator = GeneratorEngine(
        length=2,
        tlds=[".com"]
    )

    pipeline = DomainPipeline(
        min_score=90,
        check_availability=False

    )

 

    exporter = CsvExporter("available_domains.csv")

    processed = 0
    exported = 0

    try:

        for candidate in generator.generate():

            processed += 1

            domain = pipeline.process(candidate)

            if domain is None:
                continue

            if domain.available:

                exporter.write(domain)
                exported += 1

                print(
                    f"[+] {domain.name:<20} "
                    f"Score:{domain.score:<3} "
                    f"AVAILABLE"
                )

    finally:

        exporter.close()

        print()
        print(f"Processed : {processed}")
        print(f"Exported  : {exported}")


if __name__ == "__main__":
    main()