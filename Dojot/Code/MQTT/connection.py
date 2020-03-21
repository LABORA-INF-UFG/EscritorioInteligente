import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
from datetime import datetime, date, timedelta
from Office.office import Office
import json, yaml
import time, _thread

class Connection():

    def __init__(self):
        self.__config = yaml.load(open('./Scripts/config.yaml', 'r'))

        self.__client = mqtt.Client('admin')
        self.__client.connect(host='127.0.0.1', port=1883)
        self.__client.loop_start()
        self.__office = Office(self.__config)
    
    def get_office(self):
        return self.__office
    
    def publish(self, topic, msg):
        print(json.dumps(msg))
        self.__client.publish(topic, json.dumps(msg))
  
    def on_message_schedule(self, client, userdata, message):
        end = datetime.strptime(json.loads(message.payload)['fim'], '%Y-%m-%d %H:%M:%S.%f')
        self.__office.set_stop(end)
        self.__office.set_allNodes()
        print(self.__office.get_stop())
        _thread.start_new_thread(self.monitoring(), )

        #self.__mail.send_email('escritoriointeligente123@gmail.com', 'franciellysouza552@gmail.com', 'teste ', 'oi')
    
    def subscribe_schedule(self):
        subscribe.callback(self.on_message_schedule, self.__config['Topics']['Subscribe']['topic_scheduler'])

    def monitoring(self):
        response = self.__office.check_availability()
        if response == 1:
            msg = {"termino_monitoramento": True}
            self.__client.publish(self.__config['Topics']['Publish']['topic_scheduler'], json.dumps(msg))

    def on_message_raspberry(self, client, userdata, message):
        raspberry_id = json.loads(message.payload)['id_rasp']
        print("Response from: node "+raspberry_id)
        for node in self.__office.get_nodes():
            if(int(node['ID'])==int(raspberry_id)):
                self.__office.set_node(True, self.__office.get_nodes().index(node))
        #self.__mail.send_email('escritoriointeligente123@gmail.com', 'franciellysouza552@gmail.com', 'teste ', 'oi')
    
    def subscribe_raspberry(self):
        subscribe.callback(self.on_message_raspberry, self.__config['Topics']['Subscribe']['topic_raspberry'])