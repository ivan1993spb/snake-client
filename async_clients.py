import asyncio
import websockets
from random import random

connections = (
    (0, 20),
    (1, 20),
    (2, 20),
    (3, 20),
    (4, 20),
    (5, 20),
    (6, 20),
    (7, 20),
    (8, 20),
    (9, 20),
)

async def run_conn(conn, group):
    await asyncio.sleep(random())
    async with websockets.connect("ws://localhost:8080/games/{}/ws".format(group)) as websocket:
        while True:
            res = await websocket.recv()
            print(res)

async def run_tasks():
    tasks = [asyncio.ensure_future(run_conn(conn=conn, group=group[0])) for group in connections for conn in range(0, group[1])]
    await asyncio.wait(tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(run_tasks())
loop.close()

