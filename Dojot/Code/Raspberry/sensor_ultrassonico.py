#Libraries
from datetime import datetime, date, timedelta
#import RPi.GPIO as GPIO
import time
import json, _thread
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe

class Ultrassonico():
    def __init__(self):
        self.__id = 1
        self.__client_id = "admin"
        self.__topic_to_publish = "/admin/20270c/attrs"
        self.__topic_to_subscribe = "/admin/249eb4/config"
        self.__end = False
        self.__client = mqtt.Client()

        self.__client.connect(host='localhost', port=1883)
        self.__client.loop_start()

        #GPIO Mode (BOARD / BCM)
        '''GPIO.setmode(GPIO.BCM)
 
        #set GPIO Pins
        GPIO_TRIGGER = 23
        GPIO_ECHO = 24
 
        #set GPIO direction (IN / OUT)
        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)'''

    def distance(self):
        return 90
 
    def monitoring(self, time_stop):
        while datetime.now() <= time_stop - timedelta(seconds=60) and not self.__end: # enquanto ainda nao falta 15 min pra finalizar a reserva e o monitoramento ainda nao foi encerrado
            dist = self.distance()
            if dist > 10: # verifica se a distancia é maior que 10 (sem presença) e se o monitoramento nao foi encerrado
                start = datetime.now() #inicia o temporizador de 30 seg
                while self.distance() > 10 and not self.__end: # verifica se a distancia é maior que 10 (sem presença)
                    if datetime.now() >= start + timedelta(seconds=30) and not self.__end: # verifica se já se passaram 30 seg sem presença  e se o monitoramento nao foi encerrado
                        msg = {'id': self.__id}
                        print(msg)
                        self.__client.publish(self.__topic_to_publish, json.dumps(msg))
                        time.sleep(1)
                        start = datetime.now() #inicia o temporizador de 30 seg
        print("Fim da reserva.")

    def on_message_schedule(self, client, userdata, message):
        decoded_message = json.loads(message.payload.decode())
        print(decoded_message)
        try:
            end_time = datetime.strptime(decoded_message["fim"], '%Y-%m-%d %H:%M:%S.%f')
            print(end_time)
            self.__end = False
            _thread.start_new_thread(self.monitoring, (end_time,))
        except Exception as e:
            pass
        try: 
            self.__end = decoded_message["termino"]
        except Exception as e:
            pass

        #self.__mail.send_email('escritoriointeligente123@gmail.com', 'franciellysouza552@gmail.com', 'teste ', 'oi')
    
    def subscribe_schedule(self):
        subscribe.callback(self.on_message_schedule, self.__topic_to_subscribe)

if __name__ == '__main__':
    try:
        sensor = Ultrassonico()
        print("Subscribing to topic /admin/249eb4/config...")
        sensor.subscribe_schedule()
        
        while True:
            pass
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        pass
        #GPIO.cleanup()
