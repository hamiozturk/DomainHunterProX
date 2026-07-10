import json
import os

from src.exporter.json_exporter import JSONExporter
from src.models.domain import Domain


def test_json_exporter():

    domains = []

    d1 = Domain("openai.com")
    d1.score = 100
    d1.available = False
    d1.check_status = "registered"
    d1.check_method = "rdap"

    d2 = Domain("mynewdomain999999.com")
    d2.score = 95
    d2.available = True
    d2.check_status = "available"
    d2.check_method = "rdap"

    domains.append(d1)
    domains.append(d2)

    filename = "output/test_domains.json"

    exporter = JSONExporter()

    result = exporter.export(domains, filename)

    assert result == filename
    assert os.path.exists(filename)

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 2

    assert data[0]["domain"] == "openai.com"
    assert data[0]["score"] == 100
    assert data[0]["available"] is False

    assert data[1]["domain"] == "mynewdomain999999.com"
    assert data[1]["available"] is True

    os.remove(filename)

    print("JSON Exporter test passed.")


if __name__ == "__main__":
    test_json_exporter()