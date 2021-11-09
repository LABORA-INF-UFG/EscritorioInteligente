
# WS server that sends messages at random intervals

import asyncio
from datetime import datetime
import random
import websockets
import json
import os

cwd = '/home/francielly/EscritorioInteligente/Dojot/Monitoring/Logs'
log_file = cwd + '/logs_monitoring.log'

async def showlogs(websocket, path):
    arquivo = open(log_file, 'r')
    lines = arquivo.readlines()
    arquivo.close()
    last_message = lines[len(lines)-1]
    for line in lines:
        await websocket.send(json.dumps(line))
    await asyncio.sleep(random.random() * 3)

    arquivo = open(log_file, 'r')
    file_lines = arquivo.readlines()
    arquivo.close()
    message = file_lines[len(file_lines)-1]
    if(message == None): message = file_lines[len(file_lines)-2]
    if(not bool(message == last_message)):
        try:
            await websocket.send(json.dumps(message))
            await asyncio.sleep(random.random() * 3)
            print(message)
            last_message = message
        except Exception as e:
            print(e)
    else:
        try:
            await websocket.send(None)
            await asyncio.sleep(random.random() * 3)
            print(message)
        except Exception as e:
            pass

start_server = websockets.serve(showlogs, "localhost", 5678)


asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()