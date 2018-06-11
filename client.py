from sys import argv
from websocket import create_connection

group = "0"

if len(argv) > 1:
    group = argv[1]

url = "ws://localhost:8080/games/{}/ws".format(group)
print(url)

ws = create_connection(url)

while True:
    try:
        result =  ws.recv()
        print(result)
    except KeyboardInterrupt:
        break

ws.close()

