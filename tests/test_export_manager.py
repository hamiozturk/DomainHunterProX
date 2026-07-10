import json
import os

from src.exporter import ExportManager
from src.models.domain import Domain


def create_domains():

    d1 = Domain("google.com")
    d1.score = 100
    d1.available = False
    d1.check_status = "registered"
    d1.check_method = "rdap"

    d2 = Domain("myuniquedomain123456.com")
    d2.score = 95
    d2.available = True
    d2.check_status = "available"
    d2.check_method = "rdap"

    return [d1, d2]


def test_csv_export():

    filename = "output/export_manager_test.csv"

    exporter = ExportManager("csv")

    exporter.export(create_domains(), filename)

    assert os.path.exists(filename)

    os.remove(filename)


def test_json_export():

    filename = "output/export_manager_test.json"

    exporter = ExportManager("json")

    exporter.export(create_domains(), filename)

    assert os.path.exists(filename)

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 2
    assert data[0]["domain"] == "google.com"
    assert data[1]["available"] is True

    os.remove(filename)


def test_invalid_exporter():

    try:
        ExportManager("xml")
    except ValueError:
        return

    raise AssertionError("ValueError was expected.")


if __name__ == "__main__":

    test_csv_export()

    test_json_export()

    test_invalid_exporter()

    print("ExportManager tests passed.")