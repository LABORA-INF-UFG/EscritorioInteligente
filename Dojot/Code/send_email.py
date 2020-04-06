from MQTT.connection import Connection
from Office.is_alive import Is_Alive
import _thread
import time, yaml
#from multiprocessing.pool import ThreadPool

try:
    import asyncio
except ImportError:
    import trollius as asyncio

if __name__ == "__main__":
    connection = Connection()
    is_alive = Is_Alive()
    #config = yaml.load(open('./Scripts/config.yaml', 'r'))
    #pool = ThreadPool(processes=1000)
    _thread.start_new_thread(connection.subscribe_schedule, ())
    _thread.start_new_thread(connection.subscribe_raspberry, ())
    #is_alive.scheduler(connection.get_office())
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        connection.loop_stop()
        pass 