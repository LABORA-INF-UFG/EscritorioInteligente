import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import json
import time

class Connection():

    def __init__(self):
        self.__client = mqtt.Client('admin')
        self.__client.connect(host='127.0.0.1', port=1883)
        self.__client.loop_start()
    
    def publish(self, topic, msg):
        print(msg)
        self.__client.publish(topic, json.dumps(msg))
