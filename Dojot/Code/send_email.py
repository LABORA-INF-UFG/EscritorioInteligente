from MQTT.connection import Connection
import time

if __name__ == "__main__":
    connection = Connection()
    print("Subscribing to topic /admin/10de5d/config...")
    connection.subscribe(topic='/admin/10de5d/config')
    while True:
        mail = connection.get_mail()
        if(mail.get_allRasp() == 1):
            mail.send_email(('escritoriointeligente123@gmail.com', 'franciellysouza552@gmail.com', 'teste ', 'oi'))
        else:
            mail.set_allRasp()

        time.sleep(10)
    time.sleep(50000)