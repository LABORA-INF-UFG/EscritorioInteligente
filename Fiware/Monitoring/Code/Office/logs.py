import logging
from datetime import datetime, date, timedelta
import yaml, os

cwd = os.path.abspath(os.path.join(os.path.dirname( __file__ ), "../..", 'Logs'))
log_file = cwd + '/logs_monitoring.log'

def log(msg):
    string = '{} - {}'.format(str(datetime.now()), msg)
    os.system(f"echo '{string}' >> {log_file}")