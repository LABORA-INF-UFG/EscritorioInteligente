from datetime import datetime, date, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from MQTT.connection import Connection
from Scheduler.scheduling_simulator import SchedulingSimulator
from requests.auth import HTTPBasicAuth
import time, yaml
import os

try:
    import asyncio
except ImportError:
    import trollius as asyncio

class Scheduler():
    def __init__(self):
        self.__msg = None
        self.__connection = Connection()
        config = yaml.load(open('./Scripts/config.yaml', 'r'))
        self.__topic = confif['Topics']['topic_scheduler']
        self.scheduler()
    
    def get_scheduling(self):
        sch = SchedulingSimulator()
        results = sch.get_times()
        now = datetime.now()
        after = now + timedelta(seconds=60)
        for row in results:
            row_date_i = datetime.strptime(row['i'], '%Y-%m-%d %H:%M:%S.%f')
            row_date_f = datetime.strptime(row['f'], '%Y-%m-%d %H:%M:%S.%f')
            if row_date_i >= now and row_date_i <= after:
                return [row_date_i, row_date_f]
        return 0

    def configure(self, time):
        #print(time.date())
        #print(time.time())
        time_i = time[0]
        time_f = time[1]
        print("publishing %r" % time_i)
        msg = 'i|'+ str(time_i)+'|f|'+str(time_f)+'|s|Ativo'
        self.__connection.publish(self.__topic, msg)
        
    def trigger_event(self):
        results = self.get_scheduling()
        if results != 0:
            try:
                self.configure(results)
            except:
                pass

        else:
            print("Unreserved room")

    
    def scheduler(self):
        scheduler = AsyncIOScheduler()
        scheduler.add_job(self.trigger_event, 'interval', seconds=58, id='temporal_event')
        
        scheduler.start()
        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
        try:
            asyncio.get_event_loop().run_forever()
        except (KeyboardInterrupt, SystemExit):
            pass 

    

        