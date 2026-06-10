from opcua import ua, Server
import time
import random

server = Server()
server.set_endpoint("opc.tcp://0.0.0.0:4840")

uri = "MES_Project"
idx = server.register_namespace(uri)

objects = server.get_objects_node()

machine = objects.add_object(idx, "Machine")

production_count = machine.add_variable(idx, "Production_Count", 0)
machine_status = machine.add_variable(idx, "Machine_Status", "STOP")

production_count.set_writable()
machine_status.set_writable()

server.start()

print("OPC UA Server Started")

count = 0

try:
    while True:
        count += 1

        production_count.set_value(count)
        machine_status.set_value(
            random.choice(["RUN", "STOP", "FAULT"])
        )

        time.sleep(2)

except KeyboardInterrupt:
    server.stop()