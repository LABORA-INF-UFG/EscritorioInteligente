from MQTT.connection import Connection

class Monitoring():

    def __init__(self):
        self.__msg = None
        self.__connection = Connection()
        self.__connection.subscribe('/admin/f47551/config')

    def distance():
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18,GPIO.OUT)
        GPIO.output(18,GPIO.LOW)
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

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
	        message = {"distancia": dist}
            print ("distancia: %.1f" % dist)
	        print("Publishing", message)
            self.__connection.publish('/admin/77dccd/attrs', message)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        GPIO.cleanup()

