from datetime import datetime, date, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import time
import os
import _thread
from MQTT.connection import Connection
from Scheduler.scheduling_simulator import SchedulingSimulator

try:
    import asyncio
except ImportError:
    import trollius as asyncio

class Scheduler():
    def __init__(self):
        self.__msg = None
        self.__connection = Connection()
        self.scheduler()
    
    def get_scheduling(self):
        sch = SchedulingSimulator()
        results = sch.get_times()
        now = datetime.now()
        after = now + timedelta(seconds=60)
        for row in results:
            row_date = datetime.strptime(row, '%Y-%m-%d %H:%M:%S.%f')
            if row_date >= now and row_date <= after:
                return row_date
        return 0

    def configure(self, time):
        #print(time.date())
        #print(time.time())
        print("publishing %r" % time)
        msg = {'horario': str(time.time()), 'ativo': True}
        self.__connection.publish('/admin/a124c1/attrs', msg)
        
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
        scheduler.add_job(self.trigger_event, 'interval', seconds=2, id='temporal_event')
        
        scheduler.start()
        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
        try:
            asyncio.get_event_loop().run_forever()
        except (KeyboardInterrupt, SystemExit):
            pass 
