#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import timeit
import websockets
from datetime import datetime
import pandas as pd
import producer

message_time = []
messages = []
connection_time = []
end_took = 0

def extract_csv_file():
    merge_list = [producer.instantMessage , producer.charactercount , message_time , connection_time]
    df = pd.DataFrame(merge_list).transpose()
    df.columns = ['Messages','Message Length','Dealy Time in Millisec' , 'Connection Time ("%H:%M:%S")']
    df.to_csv('Record.csv')
    print("Your Record Is Saved!")


async def time(websocket, path):
    print("Connecting to the server........")
    count = 0
    while count < producer.generate_message:
        now = producer.instantMessage[count]
        time = datetime.now()
        current_time = time.strftime("%H:%M:%S")
        connection_time.append(current_time)
        start_time = timeit.default_timer()
        await websocket.send(now)
        end_took = (timeit.default_timer() - start_time) * 1000.0
        time_message = ''.join("𝐌𝐞𝐬𝐬𝐚𝐠𝐞 Delay 𝐓𝐢𝐦𝐞: " + str(end_took))
        await websocket.send(time_message)
        message_time.append(end_took)
        count += 1
    extract_csv_file()
start_server = websockets.serve(time, "127.0.0.1", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()