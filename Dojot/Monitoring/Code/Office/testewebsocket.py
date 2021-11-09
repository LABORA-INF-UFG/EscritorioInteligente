import logging
from datetime import datetime, date, timedelta
import yaml, os
import asyncio
import random
import websockets
import json
import os, time

cwd = os.path.abspath(os.path.join(os.path.dirname( __file__ ), "../..", 'Logs'))
log_file = cwd + '/logs_monitoring.log'

def log(msg):
    print(msg)
    string = msg
    os.system(f"echo '{string}' >> {log_file}")


while(True):
    log(str(datetime.now()))
    time.sleep(5)