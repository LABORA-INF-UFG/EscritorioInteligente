import paho.mqtt.client as mqtt
import json

class Connection:

    def __init__(self):
        self.__client = mqtt.Client()
        self.__client.connect(host='127.0.0.1', port=1883)
        self.__client.loop_start()

    def on_message(client, userdata, message):
        # print(message.payload())
        decoded_message = json.loads(message.payload.decode())
        message = decoded_message['attrs']['ativo']
        #message = (int(decoded_message.find('OFF')))
        #    print(message)
        print("message")
    
    def publish(self, topic, msg):
        print(msg)
        self.__client.publish(topic, json.dumps(msg))

    def subscribe(self, topic):
        print(msg)
        self.__client.subscribe(topic)
        client.on_message = on_message