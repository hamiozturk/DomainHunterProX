import csv
import os

from .base import BaseExporter


class CSVExporter(BaseExporter):

    def export(self, domains, filename):

        folder = os.path.dirname(filename)

        if folder:
            os.makedirs(folder, exist_ok=True)

        with open(
            filename,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "domain",
                "score",
                "available",
                "status",
                "method",
                "checked_at"
            ])

            for domain in domains:

                writer.writerow([

                    domain.name,

                    domain.score,

                    domain.available,

                    domain.check_status,

                    domain.check_method,

                    domain.checked_at

                ])

        return filename