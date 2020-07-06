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
        self.__config = yaml.load(open('../Scripts/config.yaml', 'r'))

        self.__client = mqtt.Client()
        self.__client.connect(host=self.__config['mqtt_broker']['host'], port=self.__config['mqtt_broker']['port'])
        self.__client.loop_start()
        self.__office = Office(self.__config)
    
    def get_office(self):
        return self.__office
    
    def publish(self, topic, msg): #publica mensagem mqtt
        try:
            response = self.__client.publish(topic, json.dumps(msg))
            time.sleep(2)
            response.wait_for_publish()
            if not response.is_published():
                print(response)
        except:
            pass
        
    def loop_stop(self): #encerra conexao com o broker mosquitto
        try:
            self.__client.loop_stop()
        except:
            logs.log('ERROR - Não foi possível encerrar a conexão com o broker MQTT!')

    def on_message_schedule(self, client, userdata, message): #recebe horario de reserva e inicia monitoramento
        try:
            end = datetime.strptime(json.loads(message.payload)['fim'], '%Y-%m-%d %H:%M:%S.%f')
            self.__office.set_stop(end)
            self.__office.set_allNodes()
            _thread.start_new_thread(self.monitoring(), ())
        except Exception as e:
            print(e)
    
    def subscribe_schedule(self): 
        logs.log("INFO - Subscrevendo no tópico {}...".format(self.__config['topics']['subscribe']['topic_scheduler']))
        try:

            subscribe.callback(self.on_message_schedule, self.__config['topics']['subscribe']['topic_scheduler'])
        except (KeyboardInterrupt, SystemExit):
            pass

    def monitoring(self):
        try:
            response = self.__office.check_availability() #inicia monitoramento da sala 
            if response == 1:
                msg = {"termino_monitoramento": True}
                logs.log('INFO - Publicando: {}'.format(json.dumps(msg)))
                response = self.__client.publish(self.__config['topics']['publish']['topic_scheduler'], json.dumps(msg)) #encerra monitoramento nos sensores
                time.sleep(2)
                response.wait_for_publish()
            #logs_scheduler.log('Message is published = {}'.format(response.is_published()))
                if not response.is_published():
                    print(response)
        except:
            pass
        finally:
            logs.log("INFO - Monitoramento encerrado.")    

    def callback(self, client, userdata, message):
        topic = message.topic
        payload = json.loads(message.payload)
        print(payload)
        time_msg = payload['time']
        if topic == self.__config['topics']['subscribe']['topic_heartbeat']:
            raspberry_id = payload['id']
            #logs.log("INFO - Nó {} está ativo.".format(raspberry_id))
            for node in self.__office.get_nodes():
                if(int(node['ID'])==int(raspberry_id)):
                    self.__office.set_heartbeat(self.__office.get_nodes().index(node), time_msg)
        elif topic == self.__config['topics']['subscribe']['topic_raspberry']:
            raspberry_id = payload['id_rasp']
            #logs.log("INFO - Resposta de: nó {}".format(raspberry_id))
            for node in self.__office.get_nodes():
                if(int(node['ID'])==int(raspberry_id)):
                    self.__office.set_node(True, self.__office.get_nodes().index(node), time_msg)
        #print(self.__office.get_nodes())

    def subscribe_raspberry(self):
        logs.log("INFO - Subscrevendo nos tópicos {} e {}...".format(self.__config['topics']['subscribe']['topic_heartbeat'], self.__config['topics']['subscribe']['topic_raspberry']))
        try:
            subscribe.callback(self.callback, [self.__config['topics']['subscribe']['topic_heartbeat'], self.__config['topics']['subscribe']['topic_raspberry']])
        except:
            pass