from Email.email import Email
from datetime import datetime, date, timedelta
import yaml, time

class Office():
    def __init__(self, config):
        self.__msg = None
        self.__id = None
        self.__email = Email()
        self.__tenant = None
        self.__start = None
        self.__stop = None
        self.__nodes = []
        print(config['Nodes'])
        for x in config['Nodes']:
            node = {'ID': x['ID'], 'Status': False, 'Last_Update': datetime.now()}
            self.__nodes.append(node)

    def get_start(self):
        return self.__start
    
    def get_stop(self):
        return self.__stop

    def get_nodes(self):
        return self.__nodes

    def get_allNodes(self):
        for node in self.__nodes:
            if not node['Status']:
                return 0
        #print(self.__nodes)
        return 1

    def get_oneNode(self):
        for node in self.__nodes:
            if node['Status']:
                return 1
        return 0

    def set_node(self, status, index):
        self.__nodes[index]['Status'] = status
        self.__nodes[index]['Last_Update'] = datetime.now()

    def set_allNodes(self):
        for x in range(len(self.__nodes)):
            self.__nodes[x]['Status'] = False
            self.__nodes[x]['Last_Update'] = datetime.now()
        #print(self.__nodes)

    def set_start(self, start):
        self.__start = start

    def set_stop(self, stop):
        self.__stop = stop

    def last_update(self): #verifca se a ultima atualização de cada nó foi há mais de 30 seg atrás
        now = datetime.now()
        for node in self.__nodes:
            if node['Last_Update'] < now - timedelta(seconds=30):
                return 0
        
        return 1

    def check_availability(self):
        while self.__stop >= datetime.now()+timedelta(seconds=60): #monitora até 15min antes do stop da reuniao
            if self.get_oneNode() == 1: #recebe resposta de pelo menos um sensor"
                print("Aguardando resposta de todos os nós...")
                time.sleep(30)# aguarda 30 segundos
                if(self.get_allNodes() == 1): #verifica se os outros sensores enviam resposta"
                    print("Iniciando temporizador...")
                    start = datetime.now()
                    while self.last_update() == 1: # verifica se todos os sensores ainda estão detectando ausencia
                        if datetime.now() >= start + timedelta(seconds=60) and self.__stop >= datetime.now()+timedelta(seconds=60): # verifica se já se passaram 15 min sem presença e se falta mais de 15 min pro stop da reserva
                            print("Office Disponível!") 
                            self.__email.send_email()
                            return 1
                            #self.set_allNodes()
                        time.sleep(1)
                    print("Algum sensor detectou presença.")
                else: # se os outros sensores nao enviam          
                    print("Algum sensor está detectando presença.")
            self.set_allNodes()  # False
            time.sleep(5)
        return 0