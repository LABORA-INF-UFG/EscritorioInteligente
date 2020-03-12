#Libraries
from datetime import datetime, date, timedelta
import RPi.GPIO as GPIO
import time
import json
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe

#properties definition

#internal definitions setup
client_id = "admin"
topic_to_publish = "/admin/20270c/attrs"
topic_to_subscribe = "/admin/20c259/config"

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 23
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def on_message(client, userdata, message):
    decoded_message = json.loads(message.payload.decode())
    print(decoded_message)
    msg = {'estado': 'vazio'}
    print(msg)
    client.publish(topic_to_publish, json.dumps(msg))
    #time_i = datetime.strptime(decoded_message[4:30], '%Y-%m-%d %H:%M:%S.%f')
'''    time_f = datetime.strptime(decoded_message["fim"], '%Y-%m-%d %H:%M:%S.%f')
    response = monitoring(time_f)
    if(response == 1):
        msg = {'estado': 'Vazio'}
        print(msg)
        client.publish(topic_to_publish, json.dumps(msg))'''

#MQTT client setup and connection
client = mqtt.Client()

print("Connecting to mqtt broker...")
client.connect(host='10.16.1.171', port=1883)
client.loop_start()

print("Subscribing to topic /admin/20c259/config...")
client.subscribe(topic_to_subscribe)
client.on_message = on_message

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
 
def monitoring(time_stop):
    now = datetime.now()
    while now <= time_stop:
        dist = distance()
        print(dist)
        if dist > 10:
            start = datetime.now()
            while True:
                #print(start + timedelta(seconds=60))
                if datetime.now() >= start + timedelta(seconds=60):
                    return 1
                elif distance() < 10:
                    break
        now = datetime.now()  
    return 0

if __name__ == '__main__':
    try:
        while True:
           ''' dist = distance()
            message = {"distancia": str(dist)}
            print ("distancia: %.1f" % dist)
            print ("Publishing", message, 'to topic', topic_to_publish)
            client.publish(topic_to_publish, json.dumps(message))'''
           time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        GPIO.cleanup()
