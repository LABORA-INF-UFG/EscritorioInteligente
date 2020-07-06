from Email.email import Email
from Office import logs
from datetime import datetime, date, timedelta
import yaml, time, os
from apscheduler.schedulers.asyncio import AsyncIOScheduler

try:
    import asyncio
except ImportError:
    import trollius as asyncio

class Office(object):
    def __init__(self, config):
        self.__msg = None
        self.__id = None
        self.__config = config
        self.__tenant = None
        self.__start = None
        self.__stop = None
        self.__nodes = []
        for x in range(1, config['room']['nodes']+1):
            node = {'ID': x, 'Status': False, 'Last_Update': datetime.now(), 'Heartbeat': datetime.now()}
            self.__nodes.append(node)
        #self.scheduler()
        

    def get_start(self): #retorna o horario de inicio da reserva
        return self.__start
    
    def get_stop(self): # retorna o horario do fim da reserva
        return self.__stop

    def get_nodes(self): # retorna a lista de nós da sala
        return self.__nodes

    def get_allNodes(self): # retorna 1 se todos os nós estão detectando ausencia de pessoas
        for node in self.__nodes:
            if not node['Status']:
                return 0
        #print(self.__nodes)
        return 1

    def get_oneNode(self): # retorna 1 se ao menos um nó está detectando ausencia de pessoas
        for node in self.__nodes:
            if node['Status']:
                logs.log("INFO - Identificada a ausência de pessoas em regiões do ambiente.")
                return 1
        return 0

    def set_node(self, status, index, time_msg): # atualiza o dado de leitura do nó (ausencia/presenca e o horario de envio da mensagem)
        #print(index, time_msg)
        self.__nodes[index]['Status'] = status
        self.__nodes[index]['Last_Update'] = datetime.strptime(time_msg, '%Y-%m-%d %H:%M:%S.%f')

    def set_heartbeat(self, index, time_msg): # atualiza 
        self.__nodes[index]['Heartbeat'] = datetime.strptime(time_msg, '%Y-%m-%d %H:%M:%S.%f')

    def set_allNodes(self): # altera o status de todos os nós para falso (detectando presença)
        for x in range(len(self.__nodes)):
            self.__nodes[x]['Status'] = False
            self.__nodes[index]['Last_Update'] = datetime.now()
        #print(self.__nodes)

    def set_start(self, start):
        self.__start = start

    def set_stop(self, stop):
        self.__stop = stop

    def last_update(self): #verifca se a ultima atualização de cada nó foi há mais de 30 seg atrás
        now = datetime.now()
        for node in self.__nodes:
            if node['Last_Update'] < now - timedelta(seconds=35):
                
                return 0
        return 1

    def check_availability(self): #verifica se a sala está disponível
        logs.log("INFO - Monitoramento iniciado.")
        while self.__stop >= datetime.now()+timedelta(minutes=5): #monitora até 5min antes do fim da reuniao
            if self.get_oneNode() == 1: #recebe resposta de pelo menos um sensor"
                time.sleep(30)# aguarda 30 segundos
                if self.get_allNodes() == 1: #verifica se os outros sensores enviam resposta"
                    logs.log("INFO - Nenhuma pessoa identificada no ambiente. Temporizador iniciado.")
                    start = datetime.now() #momento em que todos os nós detectaram ausencia na sala
                    while self.last_update() == 1: # enquanto todos os sensores ainda estão detectando ausencia
                        if datetime.now() >= start + timedelta(minutes=self.__config['set_times']['cancel_booking']): # verifica se já se passaram 15 min sem presença
                            logs.log("INFO - Ambiente disponível!") 
                            if self.__stop >= datetime.now()+timedelta(minutes=self.__config['set_times']['cancel_booking']): # verifica se resta mais de 15 min para o fim da reserva
                                subject = self.__config['email']['availability']['subject'] # assunto do email
                                msg = self.__config['email']['availability']['message'] # texto do email
                                email = Email()
                                email.send_email(subject, msg) # envia email
                            return 1
                        elif ((datetime.now() - start).seconds % 300) == 0: #alerta se a sala está vazia a cada 5 min
                            minutes = (datetime.now() - start).seconds//60
                            if (minutes != 0):
                                logs.log("INFO - Ambiente vazio há {} minutos.".format(minutes))
                        time.sleep(1)
                    if self.__stop >= datetime.now()+timedelta(minutes=5): # algum sensor detectou presença
                        logs.log("INFO - Identificada a presença de pessoas no ambiente!")
                else: # se os outros sensores nao enviam          
                    pass
                self.set_allNodes()  # False
            time.sleep(1)
        return 0

    