import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
from Email.email import Email
import json
import time

class Connection():

    def __init__(self):
        self.__client = mqtt.Client('admin')
        self.__client.connect(host='127.0.0.1', port=1883)
        self.__client.loop_start()
        self.__mail = Email()
    
    def publish(self, topic, msg):
        print(msg)
        self.__client.publish(topic, msg)

    def on_message_email(self, client, userdata, message):
        print("Send Email")
        self.__mail.send_email('escritoriointeligente123@gmail.com', 'franciellysouza552@gmail.com', 'teste ', 'oi')
    
    def subscribe(self, topic):

        subscribe.callback(self.on_message_email, topic)