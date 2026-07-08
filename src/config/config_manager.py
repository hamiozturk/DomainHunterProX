"""
DomainHunter Pro X

Configuration Manager
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import orjson

from src.logger import logger


class ConfigManager:
    """
    Application configuration manager.
    """

    DEFAULT_CONFIG = {
        "app": {
            "name": "DomainHunter Pro X",
            "version": "0.1.0-alpha",
            "theme": "dark",
            "language": "en"
        },
        "scanner": {
            "timeout": 5,
            "workers": 100
        },
        "generator": {
            "default_length": 5,
            "default_tld": ".com"
        },
        "window": {
            "width": 1400,
            "height": 900
        }
    }

    def __init__(self) -> None:

        self.base_dir = Path(__file__).resolve().parents[2]
        self.config_dir = self.base_dir / "config"
        self.config_file = self.config_dir / "config.json"

        self.config_dir.mkdir(exist_ok=True)

        self.data: dict[str, Any] = {}

        self.load()

    def load(self) -> None:

        if not self.config_file.exists():
            self.data = self.DEFAULT_CONFIG
            self.save()
            logger.success("Default configuration created.")
            return

        with open(self.config_file, "rb") as f:
            self.data = orjson.loads(f.read())

        logger.info("Configuration loaded.")

    def save(self) -> None:

        with open(self.config_file, "wb") as f:
            f.write(
                orjson.dumps(
                    self.data,
                    option=orjson.OPT_INDENT_2
                )
            )

        logger.info("Configuration saved.")

    def get(self, *keys, default=None):

        value = self.data

        for key in keys:

            if isinstance(value, dict):

                value = value.get(key)

            else:

                return default

        if value is None:

            return default

        return value

    def set(self, *keys, value):

        data = self.data

        for key in keys[:-1]:

            data = data.setdefault(key, {})

        data[keys[-1]] = value

        self.save()