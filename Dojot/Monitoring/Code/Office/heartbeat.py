from apscheduler.schedulers.asyncio import AsyncIOScheduler
import os, yaml
from Email.email import Email
from datetime import datetime, date, timedelta
from Office import logs
from pymongo import MongoClient

try:
    import asyncio
except ImportError:
    import trollius as asyncio
class Heartbeat(object):

    def __init__(self, config):
        self.__config = config
        self.__id_office = self.__config['room']['id']
 
    def heartbeat(self, office):
        now = datetime.now()
        for node in office.get_nodes():
            if node['Heartbeat'] < now - timedelta(minutes=10):
                msg = 'WARNING - Nó com ID = {} não responde desde {}!'.format(node['ID'], node['Heartbeat'])
                logs.log(msg)
                subject = self.__config['email']['failure']['subject']
                msg_config = self.__config['email']['failure']['message']
                msg = msg_config + '\nNó com ID = {} não responde desde {}!'.format(node['ID'], node['Heartbeat'])
                email = Email()
                email.send_email(subject, msg)

                self.update_status_node(node['ID'], 'Inativo')


    def scheduler(self, office):
        scheduler = AsyncIOScheduler()
        scheduler.add_job(self.heartbeat, 'interval', minutes=5, id='heartbeat', args=[office])
        scheduler.start()
        
        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
        try:
            asyncio.get_event_loop().run_forever()
        except (KeyboardInterrupt, SystemExit):
            pass 
    