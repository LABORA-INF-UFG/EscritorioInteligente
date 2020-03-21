from datetime import datetime, date, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from MQTT.connection import Connection
from Scheduler.scheduling_simulator import SchedulingSimulator
import time, yaml
import os

try:
    import asyncio
except ImportError:
    import trollius as asyncio

class Scheduler():
    def __init__(self):
        self.__config = yaml.load(open('./Scripts/config.yaml', 'r'))
        self.__msg = None
        self.__connection = Connection()
        self.__topic_scheduler = self.__config['Topics']['Publish']['topic_scheduler']
        self.__list = []
        self.scheduler()
    
    def get_scheduling(self):
        self.__list.clear()
        #print(self.__list)
        sch = SchedulingSimulator()
        results = sch.get_times()
        row_date_i = row_date_f = r = None
        for row in results:
            r = {"i": row['i'], "f": row['f']}
            self.__list.append(r)
        #print(self.__list)

    def consumer(self):
        if len(self.__list) > 0:
            for row in self.__list:
                if row["i"] >= datetime.now() and row["i"] <= (datetime.now() + timedelta(seconds=5)):
                    msg = {'inicio_reserva': str(row["i"]),'fim_reserva': str(row["f"])}
                    self.__connection.publish(self.__topic_scheduler, msg)
                    self.__list.remove(row)

    def scheduler(self):
        scheduler = AsyncIOScheduler()
        scheduler.add_job(self.get_scheduling, 'interval', seconds=10, id='search')
        scheduler.add_job(self.consumer, 'interval', seconds=2, id='temporal_event')
        #print(scheduler.get_jobs())
        scheduler.start()
        
        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
        try:
            asyncio.get_event_loop().run_forever()
        except (KeyboardInterrupt, SystemExit):
            pass 

    

        