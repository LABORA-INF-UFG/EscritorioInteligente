#Libraries
from datetime import datetime, date, timedelta
#import RPi.GPIO as GPIO
import time, os, re, yaml, json, _thread
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
from apscheduler.schedulers.asyncio import AsyncIOScheduler

try:
    import asyncio
except ImportError:
    import trollius as asyncio

class Ultrassonico(object):
    def __init__(self):
        self.__config = yaml.load(open('../Scripts/config.yaml', 'r'))
        self.__id = self.__config['node']['node_id']
        self.__distance_max = self.__config['node']['distance_max']

        self.__client_id = "admin{}".format(self.__id)
        self.__end = False
        self.__client = mqtt.Client()

        self.__client.connect(host=self.__config['mqtt_broker']['host'], port=self.__config['mqtt_broker']['port'])
        self.__client.loop_start()
        self.__log_file = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Logs'))+'/logs.log'

        self.log("INFO - Subscribing to topic {}...".format(self.__config['topics']['topic_scheduler']))
        _thread.start_new_thread(self.subscribe_schedule, ())
        #GPIO Mode (BOARD / BCM)
        '''GPIO.setmode(GPIO.BCM)
 
        #set GPIO Pins
        GPIO_TRIGGER = 23
        GPIO_ECHO = 24
 
        #set GPIO direction (IN / OUT)
        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)'''
        self.heartbeat()
        self.scheduler()

    def log(self, msg):
        string = '{} - {}'.format(str(datetime.now()), msg)
        os.system(f"echo '{string}' >> {self.__log_file}")
    
    def loop_stop(self):
        try:
            self.__client.loop_stop()
        except:
            self.log('ERROR - Unable to kill the thread!')
    
    def distance(self):
        time.sleep(1)
        # set Trigger to HIGH
        GPIO.output(GPIO_TRIGGER, True)
 
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
 
        StartTime = time.time()
        StopTime = time.time()
 
        # save StartTime
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()
 
        # save time of arrival
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()
 
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
 
        return distance
 
    def monitoring(self, time_stop):
        #print(not self.__end)
        self.log('INFO - Monitoramento Iniciado.')
        while datetime.now() <= time_stop - timedelta(minutes=5) and not self.__end: # enquanto ainda nao falta 15 min pra finalizar a reserva e o monitoramento ainda nao foi encerrado
            dist = self.distance()
            if dist > self.__distance_max: # verifica se a distancia é maior que 10 (sem presença) e se o monitoramento nao foi encerrado
                start = datetime.now() #inicia o temporizador de 30 seg
                while self.distance() > self.__distance_max and not self.__end and datetime.now() <= time_stop - timedelta(minutes=5): # verifica se a distancia é maior que 10 (sem presença)
                    if datetime.now() >= start + timedelta(seconds=29) and not self.__end: # verifica se já se passaram 30 seg sem presença  e se o monitoramento nao foi encerrado
                        msg = 'i|{}|t|{}'.format(self.__id, str(datetime.now()))
                        self.log('INFO - Ausencia detectada!')
                        self.log('INFO - Publicando: {}'.format(msg))
                        self.__client.publish(self.__config['topics']['topic_raspberry'], msg)
                        time.sleep(1)
                        start = datetime.now() #inicia o temporizador de 30 seg
        self.log("INFO - Monitoramento finalizado.")

    def on_message_schedule(self, client, userdata, message):
        decoded_message = str(message.payload)
        print(decoded_message)
        try:
            end_time = datetime.strptime(decoded_message[33:59], '%Y-%m-%d %H:%M:%S.%f')
            print(end_time)
            self.__end = False
            _thread.start_new_thread(self.monitoring, (end_time,))
        except:
            pass
        try: 
            if(bool(re.search('true', decoded_message, re.IGNORECASE))):
                self.__end = bool(decoded_message[4:-1])
                print(self.__end)
        except Exception as e:
            pass

        #self.__mail.send_email('escritoriointeligente123@gmail.com', 'franciellysouza552@gmail.com', 'teste ', 'oi')
    
    def subscribe_schedule(self):
        subscribe.callback(self.on_message_schedule, self.__config['topics']['topic_scheduler'], hostname = self.__config['mqtt_broker']['host'])

    def heartbeat(self):
        msg = 'i|{}|t|{}'.format(self.__id, str(datetime.now()))
        self.log("INFO - Nó ativo: {}".format(msg))
        response = self.__client.publish(self.__config['topics']['topic_heartbeat'], msg)
        time.sleep(1)
        response.wait_for_publish()

    def scheduler(self):
        scheduler = AsyncIOScheduler()
        scheduler.add_job(self.heartbeat, 'interval', minutes=5, id='heartbeat', max_instances= 10)
        scheduler.start()
        
        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
        try:
            asyncio.get_event_loop().run_forever()
        except (KeyboardInterrupt, SystemExit):
            pass 



if __name__ == '__main__':
    try:
        sensor = Ultrassonico()
        
        try:
            asyncio.get_event_loop().run_forever()
        except (KeyboardInterrupt, SystemExit):
            sensor.loop_stop()
            pass 
 
        # Reset by pressing CTRL + C
    except (KeyboardInterrupt, SystemExit):
        sensor.loop_stop()
        pass
        #GPIO.cleanup()
