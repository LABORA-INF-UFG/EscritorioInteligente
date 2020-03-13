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
    
    def get_mail(self):
        return self.__mail
    
    def publish(self, topic, msg):
        print(json.dumps(msg))
        self.__client.publish(topic, json.dumps(msg))
  
    def on_message_email(self, client, userdata, message):
        raspberry_id = str(message.payload)[4]
        print(raspberry_id)
        if(raspberry_id == '1'):
            self.__mail.set_rasp01(True)
        elif(raspberry_id == '2'):
            self.__mail.set_rasp02(True)
        elif(raspberry_id == '3'):
            self.__mail.set_rasp03(True)
        '''print(self.__mail.get_rasp01())
        print(self.__mail.get_rasp02())
        print(self.__mail.get_rasp03())'''

        #self.__mail.send_email('escritoriointeligente123@gmail.com', 'franciellysouza552@gmail.com', 'teste ', 'oi')
    
    def subscribe(self, topic):

        subscribe.callback(self.on_message_email, topic)