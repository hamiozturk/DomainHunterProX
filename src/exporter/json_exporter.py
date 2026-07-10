import json
import os
from datetime import datetime

from .base import BaseExporter


class JSONExporter(BaseExporter):

    def export(self, domains, filename):

        folder = os.path.dirname(filename)

        if folder:
            os.makedirs(folder, exist_ok=True)

        data = []

        for domain in domains:

            item = {
                "domain": domain.name,
                "score": domain.score,
                "available": domain.available,
                "status": domain.check_status,
                "method": domain.check_method,
                "checked_at": (
                    domain.checked_at.isoformat()
                    if isinstance(domain.checked_at, datetime)
                    else None
                ),
            }

            data.append(item)

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

        return filename