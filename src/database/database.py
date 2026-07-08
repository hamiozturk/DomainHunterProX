"""
DomainHunter Pro X

Database Manager
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

from src.logger import logger


class Database:
    """SQLite database manager."""

    def __init__(self) -> None:

        self.base_dir = Path(__file__).resolve().parents[2]
        self.database_dir = self.base_dir / "database"
        self.database_dir.mkdir(exist_ok=True)

        self.database_file = self.database_dir / "domainhunter.db"

        self.connection = sqlite3.connect(self.database_file)
        self.connection.row_factory = sqlite3.Row

        logger.success("Database connected.")

        self.create_tables()

    def create_tables(self) -> None:

        cursor = self.connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings(
            key TEXT PRIMARY KEY,
            value TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS favorites(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain TEXT NOT NULL,
            tld TEXT NOT NULL,
            score INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.connection.commit()

        logger.success("Database tables checked.")

    def execute(self, query: str, params: tuple = ()):

        cursor = self.connection.cursor()

        cursor.execute(query, params)

        self.connection.commit()

        return cursor

    def fetchone(self, query: str, params: tuple = ()):

        cursor = self.connection.cursor()

        cursor.execute(query, params)

        return cursor.fetchone()

    def fetchall(self, query: str, params: tuple = ()):

        cursor = self.connection.cursor()

        cursor.execute(query, params)

        return cursor.fetchall()

    def close(self):

        self.connection.close()

        logger.info("Database closed.")