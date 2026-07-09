from src.generator import GeneratorEngine
from src.pipeline import DomainPipeline
from src.exporter import CsvExporter


generator = GeneratorEngine(
    length=2,
    tlds=[".com"]
)

pipeline = DomainPipeline()

exporter = CsvExporter("results.csv")

count = 0

for candidate in generator.generate():

    domain = pipeline.process(candidate)

    if domain is None:
        continue

    exporter.write(domain)

    count += 1

    if count == 10:
        break

exporter.close()

print("10 domains exported.")