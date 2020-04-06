import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
from datetime import datetime, date, timedelta
from Office.office import Office
from Office import logs
import json, yaml
import time, _thread

try:
    import asyncio
except ImportError:
    import trollius as asyncio

class Connection(object):

    def __init__(self):
        self.__config = yaml.load(open('./Scripts/config.yaml', 'r'))

        self.__client = mqtt.Client()
        self.__client.connect(host='127.0.0.1', port=1883)
        self.__client.loop_start()
        self.__office = Office(self.__config)
    
    def get_office(self):
        return self.__office
    
    def publish(self, topic, msg):
        try:
            response = self.__client.publish(topic, json.dumps(msg))
            #logs_scheduler.log('Message is published = {}'.format(response.is_published()))
            time.sleep(2)
            response.wait_for_publish()
            #logs_scheduler.log('Message is published = {}'.format(response.is_published()))
            if not response.is_published():
                print(response)
        except:
            pass
        
    def loop_stop(self):
        try:
            self.__client.loop_stop()
        except:
            logs.log('ERROR - Não foi possível encerrar a conexão com o broker MQTT!')

    def on_message_schedule(self, client, userdata, message):
        end = datetime.strptime(json.loads(message.payload)['fim'], '%Y-%m-%d %H:%M:%S.%f')
        self.__office.set_stop(end)
        self.__office.set_allNodes()
        _thread.start_new_thread(self.monitoring(), )

        #self.__mail.send_email('escritoriointeligente123@gmail.com', 'franciellysouza552@gmail.com', 'teste ', 'oi')
    
    def subscribe_schedule(self):
        logs.log("INFO - Subscrevendo no tópico {}...".format(self.__config['Topics']['Subscribe']['topic_scheduler']))
        try:

            subscribe.callback(self.on_message_schedule, self.__config['Topics']['Subscribe']['topic_scheduler'])
        except (KeyboardInterrupt, SystemExit):
            pass

    def monitoring(self):
        try:
            logs.log("INFO - Iniciando monitoramento...")
            response = self.__office.check_availability()
            if response == 1:
                msg = {"termino_monitoramento": True}
                logs.log('INFO - Publicando: {}'.format(json.dumps(msg)))
                self.__client.publish(self.__config['Topics']['Publish']['topic_scheduler'], json.dumps(msg))
        except:
            pass
        finally:
            logs.log("INFO - Monitoramento encerrado.")    

    def callback(self, client, userdata, message):
        topic = message.topic
        if topic == self.__config['Topics']['Subscribe']['topic_is_alive']:
            raspberry_id = json.loads(message.payload)['id']
            logs.log("INFO - Resposta de: nó {}".format(raspberry_id))
            for node in self.__office.get_nodes():
                if(int(node['ID'])==int(raspberry_id)):
                    self.__office.set_last_update(self.__office.get_nodes().index(node))
        elif topic == self.__config['Topics']['Subscribe']['topic_raspberry']:
            raspberry_id = json.loads(message.payload)['id_rasp']
            logs.log("INFO - Resposta de: nó {}".format(raspberry_id))
            for node in self.__office.get_nodes():
                if(int(node['ID'])==int(raspberry_id)):
                    self.__office.set_node(True, self.__office.get_nodes().index(node))

    def subscribe_raspberry(self):
        logs.log("INFO - Subscrevendo nos tópicos {} e {}...".format(self.__config['Topics']['Subscribe']['topic_is_alive'], self.__config['Topics']['Subscribe']['topic_raspberry']))
        try:
            subscribe.callback(self.callback, [self.__config['Topics']['Subscribe']['topic_is_alive'], self.__config['Topics']['Subscribe']['topic_raspberry']])
        except:
            pass