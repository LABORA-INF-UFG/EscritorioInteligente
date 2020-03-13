from MQTT.connection import Connection
import _thread

import time

if __name__ == "__main__":
    connection = Connection()
    print("Subscribing to topic /4jggokgpepnvsb2uv4s40d59ov/motion001/attrs...")
    _thread.start_new_thread(connection.subscribe, ("/4jggokgpepnvsb2uv4s40d59ov/motion001/attrs", ))
    while True:
        mail = connection.get_mail()
        if(mail.get_oneRasp() == 1): #se algum sensor enviou "vazio"
            time.sleep(15)# aguarda 15 segundos
            if(mail.get_allRasp() == 1): #verifica se os outros sensores enviaram "vazio"
                print("sim")
                #mail.send_email(('escritoriointeligente123@gmail.com', 'franciellysouza552@gmail.com', 'teste ', 'oi'))
            else: # se os outros sensores nao enviam          
                print("nao")
        mail.set_allRasp()  # False
        time.sleep(1)