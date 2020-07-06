from datetime import datetime, date, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from scheduling_simulator import SchedulingSimulator
import logs
import time, yaml, os, requests, logging, json
import paho.mqtt.client as mqtt

from requests.auth import HTTPBasicAuth

try:
    import asyncio
except ImportError:
    import trollius as asyncio

class Scheduler(object):
    def __init__(self):
        self.__config = yaml.load(open('../Scripts/config.yaml', 'r'))
        self.__msg = None
        self.__id = self.__config['room']['id']
        self.__client = mqtt.Client()
        self.__client.connect(host=self.__config['mqtt_broker']['host'], port=self.__config['mqtt_broker']['port'])
        self.__client.loop_start()
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
        query = 'https://teste.agendamento.rnp.br/rnp-agendamento/api/reunioes/todas?dataInicial='+today+'&dataFinal='+tomorrow+'&sala={}'.format(self.__id)
        result = requests.get(query, auth=HTTPBasicAuth(self.__config['scheduling_api']['user'], self.__config['scheduling_api']['password']))
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
                    msg = {'inicio': str(row["start"]),'fim_': str(row["end"])}
                    logs.log('INFO - Publicando: {}'.format(json.dumps(msg)))
                    try:
                        response = self.__client.publish(self.__config['topics']['topic_scheduler'], msg)
                        time.sleep(2)
                        response.wait_for_publish()
                        self.__list.remove(row)
                        if not response.is_published():
                            print(response)
                    except:
                        pass


    def scheduler(self):
        scheduler = AsyncIOScheduler()
        scheduler.add_job(self.get_scheduling, 'interval', minutes=self.__config['set_times']['query_database'], id='query')
        scheduler.add_job(self.consumer, 'interval', seconds=60, id='temporal_event')
        #print(scheduler.get_jobs())
        scheduler.start()
        
        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
        try:
            asyncio.get_event_loop().run_forever()
        except (KeyboardInterrupt, SystemExit):
            self.__client.loop_stop()
            pass 

    

        