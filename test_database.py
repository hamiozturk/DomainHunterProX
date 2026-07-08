from src.database import Database

db = Database()

db.execute(
    "INSERT INTO history(action) VALUES(?)",
    ("Application Started",)
)

rows = db.fetchall("SELECT * FROM history")

for row in rows:
    print(dict(row))

db.close()