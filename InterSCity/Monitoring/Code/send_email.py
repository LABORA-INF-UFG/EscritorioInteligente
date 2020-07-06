from MQTT.connection import Connection
#from MQTT import server
import _thread
import time, yaml

try:
    import asyncio
except ImportError:
    import trollius as asyncio

if __name__ == "__main__":
    connection = Connection()
    _thread.start_new_thread(connection.subscribe_schedule, ())
    print("ok")
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        connection.loop_stop()
        pass 