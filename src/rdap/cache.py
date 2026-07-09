import sqlite3
import os
from datetime import datetime


class RDAPCache:


    def __init__(
        self,
        db_path="data/rdap_cache.db"
    ):

        self.db_path = db_path

        folder = os.path.dirname(db_path)

        if folder and not os.path.exists(folder):
            os.makedirs(folder)


        self.conn = sqlite3.connect(
            self.db_path,
            check_same_thread=False
        )

        self.create_table()



    def create_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS rdap_cache (

            domain TEXT PRIMARY KEY,

            available INTEGER,

            status TEXT,

            checked_at TEXT

        )
        """

        self.conn.execute(query)

        self.conn.commit()



    def get(self, domain):

        cursor = self.conn.cursor()


        cursor.execute(
            """
            SELECT domain, available, status, checked_at
            FROM rdap_cache
            WHERE domain=?
            """,
            (domain,)
        )


        row = cursor.fetchone()


        if not row:
            return None



        return {

            "domain": row[0],

            "available": bool(row[1]),

            "status": row[2],

            "checked_at": row[3]

        }




    def set(self, result):

        self.conn.execute(
            """
            INSERT OR REPLACE INTO rdap_cache
            VALUES (?, ?, ?, ?)
            """,
            (
                result["domain"],
                int(result["available"])
                if result["available"] is not None
                else -1,

                result["status"],

                datetime.utcnow().isoformat()

            )
        )


        self.conn.commit()