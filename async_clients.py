import asyncio
import websockets
from random import random

connections = (
    (0, 10),
    (1, 10),
    (2, 10),
    (3, 10),
    (4, 10),
    (5, 10),
)

print("connections", connections)

async def run_conn(conn, group):
    await asyncio.sleep(random())
    async with websockets.connect("ws://localhost:8080/games/{}/ws".format(group)) as websocket:
        while True:
            res = await websocket.recv()

async def run_tasks():
    tasks = [asyncio.ensure_future(run_conn(conn=conn, group=group[0])) for group in connections for conn in range(0, group[1])]
    await asyncio.wait(tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(run_tasks())
loop.close()

