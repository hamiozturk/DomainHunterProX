import os
import sqlite3
from datetime import datetime


class RDAPCache:

    def __init__(
        self,
        db_path="data/rdap_cache.db"
    ):

        self.db_path = db_path

        folder = os.path.dirname(db_path)

        if folder:
            os.makedirs(folder, exist_ok=True)

        self.create_table()

    def _connect(self):

        conn = sqlite3.connect(
            self.db_path,
            timeout=30
        )

        return conn

    def create_table(self):

        with self._connect() as conn:

            conn.execute("""
                CREATE TABLE IF NOT EXISTS rdap_cache (

                    domain TEXT PRIMARY KEY,

                    available INTEGER,

                    status TEXT,

                    checked_at TEXT

                )
            """)

            conn.commit()

    def get(self, domain):

        with self._connect() as conn:

            cursor = conn.execute(
                """
                SELECT
                    domain,
                    available,
                    status,
                    checked_at
                FROM rdap_cache
                WHERE domain = ?
                """,
                (domain,)
            )

            row = cursor.fetchone()

        if row is None:
            return None

        available = None

        if row[1] == 1:
            available = True
        elif row[1] == 0:
            available = False

        return {

            "domain": row[0],

            "available": available,

            "status": row[2],

            "checked_at": row[3]

        }

    def set(self, result):

        if result["available"] is True:
            available = 1

        elif result["available"] is False:
            available = 0

        else:
            available = -1

        with self._connect() as conn:

            conn.execute(
                """
                INSERT OR REPLACE INTO rdap_cache
                (
                    domain,
                    available,
                    status,
                    checked_at
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    result["domain"],
                    available,
                    result["status"],
                    datetime.utcnow().isoformat()
                )
            )

            conn.commit()