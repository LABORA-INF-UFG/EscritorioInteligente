from MQTT.connection import Connection
from Office.heartbeat import Heartbeat
import _thread
import time, yaml
import os

pid = os.getpid()
print(os.getcwd())
try:
    import asyncio
except ImportError:
    import trollius as asyncio
file = open('../Monitoring/Scripts/config.yaml', 'r')
config = yaml.load(file.read())
file.close()
config['pid'] = pid
file = open('../Monitoring/Scripts/config.yaml', 'w')
file.write(str(config))
file.close()

if __name__ == "__main__":
    connection = Connection(config)
    heartbeat = Heartbeat(config)
    _thread.start_new_thread(connection.subscribe_schedule, ())
    _thread.start_new_thread(connection.subscribe_raspberry, ())
    heartbeat.scheduler(connection.get_office())
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        connection.loop_stop()
        pass 