
from websocket import create_connection
ws = create_connection("ws://localhost:8080/games/0/ws")

while True:
    try:
        result =  ws.recv()
        print("Received '%s'".format(result))
    except KeyboardInterrupt:
        break

ws.close()

