import csv
from pathlib import Path

from src.models import Domain


class CsvExporter:

    def __init__(self, filename: str):

        self.filename = Path(filename)

        self._initialized = False

    def _initialize(self):

        if self._initialized:
            return

        file_exists = self.filename.exists()

        self.file = open(
            self.filename,
            "a",
            newline="",
            encoding="utf-8"
        )

        self.writer = csv.DictWriter(
            self.file,
            fieldnames=[
                "domain",
                "extension",
                "length",
                "pattern",
                "score",
                "available",
                "status",
                "method",
                "checked_at",
                "rdap_url"
            ]
        )

        if not file_exists:
            self.writer.writeheader()

        self._initialized = True

    def write(self, domain: Domain):

        self._initialize()

        data = domain.to_dict()

        # CSV'de sld istemiyoruz
        data.pop("sld", None)

        self.writer.writerow(data)

        self.file.flush()

    def close(self):

        if self._initialized:
            self.file.close()