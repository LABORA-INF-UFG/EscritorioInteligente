import logging
from datetime import datetime, date, timedelta
import yaml, os

cwd = str(os.getcwd())
log_file = cwd + '/Logs/logs_monitoring.log'

def log(msg):
    string = '{} - {}'.format(str(datetime.now()), msg)
    os.system(f"echo '{string}' >> {log_file}")