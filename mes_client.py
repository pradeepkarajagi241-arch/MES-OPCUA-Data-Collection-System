from opcua import Client
import sqlite3
import time

# Connect OPC UA Server
client = Client("opc.tcp://127.0.0.1:4840")
client.connect()

# Connect Database
conn = sqlite3.connect("mes.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS production (
    timestamp TEXT,
    production_count INTEGER,
    machine_status TEXT
)
""")

prod_node = client.get_node("ns=2;i=2")
status_node = client.get_node("ns=2;i=3")

print("MES Started...")

while True:
    production_count = prod_node.get_value()
    machine_status = status_node.get_value()

    cursor.execute(
        "INSERT INTO production VALUES(datetime('now'), ?, ?)",
        (production_count, machine_status)
    )

    conn.commit()

    print(
        production_count,
        machine_status
    )

    time.sleep(5)