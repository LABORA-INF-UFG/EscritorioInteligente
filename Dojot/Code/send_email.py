from MQTT.connection import Connection
import _thread
import time, yaml
#from multiprocessing.pool import ThreadPool

def callback(self, client, userdata, message):
    print("oi")

if __name__ == "__main__":
    connection = Connection()
    config = yaml.load(open('./Scripts/config.yaml', 'r'))
    #pool = ThreadPool(processes=1000)
    print("Subscribing to topic " + config['Topics']['Subscribe']['topic_scheduler']+"...")
    _thread.start_new_thread(connection.subscribe_schedule, ())
    print("Subscribing to topic " + config['Topics']['Subscribe']['topic_raspberry']+"...")
    _thread.start_new_thread(connection.subscribe_raspberry, ())
    time.sleep(20000)