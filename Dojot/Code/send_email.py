from MQTT.connection import Connection
import time

if __name__ == "__main__":
    connection = Connection()
    print("Subscribing to topic /admin/20270c/config...")
    connection.subscribe(topic='/admin/20270c/config')
    time.sleep(50000)