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

        self.__client = mqtt.Client("admin") #criando client mqtt
        self.__client.connect(host=self.__config['mqtt_broker']['host'], port=self.__config['mqtt_broker']['port'])
        self.__client.loop_start()
        self.__office = Office(self.__config) # criando sala
    
    def get_office(self):
        return self.__office
    
    def publish(self, topic, msg): #publica mensagem mqtt
        try:
            response = self.__client.publish(topic, msg)
            time.sleep(2)
            response.wait_for_publish()
            if not response.is_published():
                print(response)
        except:
            pass
        
    def loop_stop(self): #encerra conexao com o broker mqtt
        try:
            msg = 't|true'
            print(msg)
            response = self.__client.publish(self.__config['topics']['topic_scheduler'], msg)
            time.sleep(2)
            response.wait_for_publish()
            self.__client.loop_stop()
        except:
            logs.log('ERROR - Não foi possível encerrar a conexão com o broker MQTT!')

    def on_message_schedule(self, client, userdata, message): #recebe horario de um navo reserva
        try:
            decoded_message = str(message.payload)
            end = datetime.strptime(decoded_message[33:59], '%Y-%m-%d %H:%M:%S.%f')
            self.__office.set_stop(end)
            self.__office.set_allNodes()
            _thread.start_new_thread(self.monitoring(), ) #inicia monitoramento
        except:
            pass
    
    def subscribe_schedule(self):
        try:

            subscribe.callback(self.on_message_schedule, self.__config['topics']['topic_scheduler']) #se inscreve no topico de horarios
        except (KeyboardInterrupt, SystemExit):
            pass

    def monitoring(self): #chama função que monitora a sala
        try:
            response = self.__office.check_availability()
            if response == 1: #finaliza monitoramento nos sensores
                msg = 't|true'
                print(msg)
                response = self.__client.publish(self.__config['topics']['topic_scheduler'], msg)
                time.sleep(2)
                response.wait_for_publish()
                if not response.is_published():
                    print(response)
                
            logs.log("INFO - Monitoramento encerrado.\n-----------------------------------------------------------")
        except:
            pass 

    def callback(self, client, userdata, message): #recebe mensagens dos sensores
        topic = message.topic #verifica o topico da mensagem recebida
        payload = str(message.payload)
        time_msg = payload[8:-1]
        raspberry_id = payload[4:5]
        if topic == self.__config['topics']['topic_heartbeat']:
            #logs.log("INFO - Nó {} está ativo.".format(raspberry_id))
            for node in self.__office.get_nodes():
                if(int(node['ID'])==int(raspberry_id)):
                    self.__office.set_heartbeat(self.__office.get_nodes().index(node), time_msg)
        elif topic == self.__config['topics']['topic_raspberry']:
            #logs.log("INFO - Resposta de: nó {}".format(raspberry_id))
            for node in self.__office.get_nodes():
                if(int(node['ID'])==int(raspberry_id)):
                    self.__office.set_node(True, self.__office.get_nodes().index(node), time_msg)

    def subscribe_raspberry(self):
        logs.log("INFO - Aplicação em execução.\n-----------------------------------------------------------")
        try:
            subscribe.callback(self.callback, [self.__config['topics']['topic_raspberry'], self.__config['topics']['topic_heartbeat']])
        except:
            pass