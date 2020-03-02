from MQTT.connection import Connection
import time

if __name__ == "__main__":
    connection = Connection()
    print("Subscribing to topic /4jggokgpepnvsb2uv4s40d59ov/Motion001/attrs...")
    connection.subscribe(topic='/4jggokgpepnvsb2uv4s40d59ov/Motion001/attrs')
    time.sleep(50000)