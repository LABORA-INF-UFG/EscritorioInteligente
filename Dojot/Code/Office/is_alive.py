from apscheduler.schedulers.asyncio import AsyncIOScheduler
import os
from datetime import datetime, date, timedelta
from Office import logs


try:
    import asyncio
except ImportError:
    import trollius as asyncio
class Is_Alive(object):

    def __init__(self):
        pass

    def is_alive(self, office):
        now = datetime.now()
        for node in office.get_nodes():
            if node['Is_alive'] < now - timedelta(minutes=10):
                msg = 'WARNING - Nó com ID = {} não responde desde {}!'.format(node['ID'], node['Is_alive'])
                logs.log(msg)

    def scheduler(self, office):
        scheduler = AsyncIOScheduler()
        scheduler.add_job(self.is_alive, 'interval', minutes=5, id='is_alive', args=[office])
        #print(scheduler.get_jobs())
        scheduler.start()
        
        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
        try:
            asyncio.get_event_loop().run_forever()
        except (KeyboardInterrupt, SystemExit):
            pass 
    