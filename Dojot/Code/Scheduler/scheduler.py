from datetime import datetime, date, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from MQTT.connection import Connection
from Scheduler.scheduling_simulator import SchedulingSimulator
from Scheduler import logs
import time, yaml, os, requests, logging, json

from requests.auth import HTTPBasicAuth

try:
    import asyncio
except ImportError:
    import trollius as asyncio

class Scheduler(object):
    def __init__(self):
        self.__config = yaml.load(open('./Scripts/config.yaml', 'r'))
        self.__msg = None
        self.__connection = Connection()
        self.__topic_scheduler = self.__config['Topics']['Publish']['topic_scheduler']
        self.__username_auth = 'escritoriointeligenternp@gmail.com'
        self.__password_auth = 'c167f6e5'
        self.__list = []
        self.get_scheduling()
        self.consumer()
        self.scheduler()
    
    def get_scheduling(self):
        self.__list.clear()
        logs.log("INFO - Buscando reservas...")
        #print(self.__list)
        sch = SchedulingSimulator()
        results = sch.get_times()
        row_date_i = row_date_f = r = None
        for row in results:
            r = {"start": row['i'], "end": row['f']}
            self.__list.append(r)
        #print(self.__list)

    '''def get_scheduling(self):
        today = datetime.now().date().strftime("%d/%m/%Y")
        tomorrow = (datetime.now() + timedelta(days=1)).date().strftime("%d/%m/%Y")
        self.__list.clear()
        logs.log("INFO - Buscando reservas...")
        query = 'https://teste.agendamento.rnp.br/rnp-agendamento/api/reunioes/todas?dataInicial='+today+'&dataFinal='+tomorrow+'&sala=44'
        result = requests.get('https://teste.agendamento.rnp.br/rnp-agendamento/api/reunioes/todas?dataInicial=11/12/2019&dataFinal=12/12/2019&sala=44', auth=HTTPBasicAuth(self.__username_auth, self.__password_auth))
        for row in result.json():
            start = datetime.strptime(row['dataInicial'], '%d/%m/%Y %H:%M')
            end = datetime.strptime(row['dataFinal'], '%d/%m/%Y %H:%M')
            r = {'start': start, 'end': end}
            self.__list.append(r)
        print(self.__list)'''

    
    def consumer(self):
        logs.log("INFO - Verificando lista...")
        if len(self.__list) > 0:
            for row in self.__list:
                #print(row["end"] <= (datetime.now() + timedelta(seconds=5)))#and row["end"] <= (datetime.now() + timedelta(seconds=5)))
                if row["start"] >= datetime.now() and row["start"] <= (datetime.now() + timedelta(seconds=60)):
                    #print(datetime.now() + timedelta(seconds=5))
                    msg = {'inicio_reserva': str(row["start"]),'fim_reserva': str(row["end"])}
                    logs.log('INFO - Publicando: {}'.format(json.dumps(msg)))
                    self.__connection.publish(self.__topic_scheduler, msg)
                    self.__list.remove(row)

    def scheduler(self):
        scheduler = AsyncIOScheduler()
        scheduler.add_job(self.get_scheduling, 'interval', minutes=20, id='query')
        scheduler.add_job(self.consumer, 'interval', seconds=60, id='temporal_event')
        #print(scheduler.get_jobs())
        scheduler.start()
        
        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
        try:
            asyncio.get_event_loop().run_forever()
        except (KeyboardInterrupt, SystemExit):
            self.__connection.loop_stop()
            pass 

    

        