from scheduler import Scheduler
import os
import yaml

pid = os.getpid()
print(pid)
file = open('../Scheduler/Scripts/config.yaml', 'r')
config = yaml.load(file.read())
file.close()
config['pid'] = pid
file = open('../Scheduler/Scripts/config.yaml', 'w')
file.write(str(config))
file.close()

Scheduler(config)