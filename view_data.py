import sqlite3

conn = sqlite3.connect("mes.db")

rows = conn.execute(
    "SELECT * FROM production"
).fetchall()

for row in rows:
    print(row)