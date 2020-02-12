import paho.mqtt.client as mqtt

class Connection:

    def __init__(self):
        self.__client = mqtt.Client()
        self.__client.connect(host='127.0.0.1', port=1883)
        self.__client.loop_start()

    def publish(self, topic, msg):
        self.__client.publish(topic, str(msg))