from MQTT.connection import Connection
import _thread
import time, yaml
#from multiprocessing.pool import ThreadPool

if __name__ == "__main__":
    connection = Connection()
    config = yaml.load(open('./Scripts/config.yaml', 'r'))
    #pool = ThreadPool(processes=1000)
    print("Subscribing to topic " + config['Topics']['topic_raspberry']+"...")
    thread.start_new_thread(connection.subscribe, (config['Topics']['topic_raspberry'], ))
    #pool.apply_async(connection.subscribe, ("/4jggokgpepnvsb2uv4s40d59ov/motion001/attr", ))
    while True:
        mail = connection.get_mail()
        if(mail.get_oneNode() == 1): #recebe resposta de pelo menos um sensor"
            time.sleep(15)# aguarda 15 segundos
            if(mail.get_allNodes() == 1): #verifica se os outros sensores enviam resposta"
                print("sim")
                mail.send_email()
                mail.set_allNodes()
            else: # se os outros sensores nao enviam          
                print("nao")
        mail.set_allNodes()  # False
        time.sleep(1)