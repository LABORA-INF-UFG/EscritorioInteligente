#Libraries
from datetime import datetime, date, timedelta
#import RPi.GPIO as GPIO
import time
import json, _thread
'''import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe

#properties definition

#internal definitions setup
client_id = "admin"
topic_to_publish = "/admin/20270c/attrs"
topic_to_subscribe = "/admin/249eb4/config"
termino = False'''

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 23
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

'''def on_message(client, userdata, message):
    decoded_message = json.loads(message.payload.decode())
    print(decoded_message)
    try:
        end_time = datetime.strptime(decoded_message["fim"], '%Y-%m-%d %H:%M:%S.%f')
        termino = False
        _thread.start_new_thread(monitoring, (end_time,))
    except Exception as e:
        pass
    try: 
        termino = decoded_message["termino"]
    except Exception as e:
        pass


#MQTT client setup and connection
client = mqtt.Client()

print("Connecting to mqtt broker...")
client.connect(host='localhost', port=1883)
client.loop_start()

print("Subscribing to topic /admin/249eb4/config...")
client.subscribe(topic_to_subscribe)
client.on_message = on_message'''

def distance():
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

'''def distance():
    return 90
 
def monitoring(time_stop):
    while datetime.now() <= time_stop - timedelta(seconds=60): # enquanto ainda nao falta 15 min pra finalizar a reserva
        dist = distance()
        print(dist)
        if dist > 10: # verifica se a distancia é maior que 10 (sem presença)
            start = datetime.now() #inicia o temporizador de 30 seg
            while distance() > 10:
                print(termino)
                if datetime.now() >= start + timedelta(seconds=30): # verifica se já se passaram 30 seg sem presença
                    msg = {'estado': 'Vazio'}
                    print(msg)
                    client.publish(topic_to_publish, json.dumps(msg))
                    time.sleep(1)
                    start = datetime.now() #inicia o temporizador de 30 seg'''
                    
                        
    

if __name__ == '__main__':
    try:
        while True:
           ''' dist = distance()
            message = {"distancia": str(dist)}
            print ("distancia: %.1f" % dist)
            print ("Publishing", message, 'to topic', topic_to_publish)
            client.publish(topic_to_publish, json.dumps(message))'''
           print(distance())
           time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        pass
        #GPIO.cleanup()
