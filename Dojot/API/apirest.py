from flask import Flask, Blueprint, request, jsonify
import json
import yaml
import os
import _thread

config = Blueprint('config', 'config', url_prefix='/config')
monitoring = '../Monitoring'
scheduler = '../Scheduler'

@config.route('', methods=['GET'])
def get():
    file = open(monitoring+'/Scripts/config.yaml', 'r')
    config = yaml.load(file.read())
    response = jsonify(message=config)
    file.close()
    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    'result = json.loads(response.get_data().decode("utf-8"))'
    return response, 201


@config.route('', methods=['POST'])
def post():
    try:
        config = json.loads(request.data)

        response = jsonify(message=newConfig(config))
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response, 201
    except Exception as e:
        print(e)
        return 'ok', 404

def newConfig(config_request):
    #alterando informacoes do arquivo de configuracao
    file_monitoring = open(monitoring+'/Scripts/config.yaml', 'r')
    config_file = yaml.load(file_monitoring.read())
    pid_monitoring = config_file['pid']
    file_monitoring.close()

    file_scheduler = open(scheduler+'/Scripts/config.yaml', 'r')
    pid_scheduler = yaml.load(file_scheduler.read())['pid']

    config_file['room']['id'] = int(config_request['id'])
    config_file['room']['nodes'] = int(config_request['nos'])

    config_file['email']['email_receiver'] = config_request['destinatario']
    config_file['email']['availability']['subject'] = config_request['asdisp']
    config_file['email']['availability']['message'] = config_request['mesdisp']

    config_file['set_times']['query_database'] = int(config_request['query'])
    config_file['set_times']['cancel_booking'] = int(config_request['booking'])

    #reexecutando aplicacoes de email e relogio
    try:
        file = open(monitoring+'/Scripts/config.yaml', 'w')
        file.write(str(config_file))
        file.close()

        file = open(scheduler+'/Scripts/config.yaml', 'w')
        file.write(str(config_file))
        file.close()

        os.system('kill -9 {}'.format(pid_scheduler))
        os.system('kill -9 {}'.format(pid_monitoring))

        os.system('nohup python3 {}/Code/send_email.py &'.format(monitoring))
        os.system('nohup python3 {}/Code/run.py &'.format(scheduler))
        #_thread.start_new_thread(os.system('python3 {}/Code/send_email.py'.format(monitoring)), ())
        #_thread.start_new_thread(os.system('python3 {}/Code/run.py'.format(scheduler)), ())
        
    except Exception as e:
        print(e)

    return config_file