from MQTT.connection import Connection
from Office.heartbeat import Heartbeat
import _thread
import time, yaml
#from multiprocessing.pool import ThreadPool

try:
    import asyncio
except ImportError:
    import trollius as asyncio

if __name__ == "__main__":
    connection = Connection()
    heartbeat = Heartbeat()
    _thread.start_new_thread(connection.subscribe_schedule, ())
    _thread.start_new_thread(connection.subscribe_raspberry, ())
    heartbeat.scheduler(connection.get_office())
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        connection.loop_stop()
        pass 