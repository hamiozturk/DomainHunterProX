import os

from .csv_exporter import CSVExporter
from .json_exporter import JSONExporter


class ExportManager:

    def __init__(self):

        self._exporters = {
            ".csv": CSVExporter(),
            ".json": JSONExporter(),
        }

    def export(self, domains, filename):

        extension = os.path.splitext(filename)[1].lower()

        exporter = self._exporters.get(extension)

        if exporter is None:
            raise ValueError(
                f"Unsupported export format: {extension}"
            )

        return exporter.export(domains, filename)