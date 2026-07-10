from .csv_exporter import CSVExporter
from .json_exporter import JSONExporter


class ExportManager:

    def __init__(self, exporter: str = "csv"):

        self._exporters = {
            "csv": CSVExporter(),
            "json": JSONExporter(),
        }

        if exporter not in self._exporters:
            raise ValueError(f"Unsupported exporter: {exporter}")

        self.exporter = self._exporters[exporter]

    def export(self, domains, filename):
        return self.exporter.export(domains, filename)