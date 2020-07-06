from flask import Flask, Blueprint, request
import yaml, time, json

api_alert = Blueprint('api_alert', 'api_alert', url_prefix='/api_alert')
@api_alert.route('monitoring', methods=['POST'])
def monitoring_api():
    msg_request = yaml.load(request.data)
    try:
        print(msg_request)
    except:
        pass

    return "ok", 201
