import csv
from pathlib import Path


class CsvExporter:

    def __init__(self):
        Path("output").mkdir(exist_ok=True)

    def save(self, filename, rows):

        with open(
            f"output/{filename}",
            "w",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.writer(f)

            writer.writerow([
                "Domain",
                "Pattern",
                "Length",
                "Score"
            ])

            writer.writerows(rows)