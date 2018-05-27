import pygame, random, sys
from pygame.locals import *
from sys import argv
from websocket import create_connection
import json

group = "0"

if len(argv) > 1:
    group = argv[1]

url = "ws://localhost:8080/games/{}/ws".format(group)
print(url)

ws = create_connection(url)

pygame.init()

s=pygame.display.set_mode((600, 600))

pygame.display.set_caption('Snake')
img = pygame.Surface((20, 20))
img.fill((255, 0, 0))

class Objects:
    def __init__(self):
        self.objects = []

    def get(self, id):
        for object in self.objects:
            if object["id"] == id:
                return object
        return None

    def set(self, id, dots):
        object = self.get(id)

        if self.get(id) is None:
            self.objects.append({
                "id":   id,
                "dots": dots,
            })
        else:
            object["dots"] = dots

    def delete(self, id):
        self.objects = list(filter(lambda object: object["id"] != id, self.objects))

    def all(self):
        for object in self.objects:
                for x, y in object["dots"]:
                    yield (x, y)

objects = Objects()

while True:
    try:
        result =  ws.recv()
        print("Received '{}'".format(result))
        data = json.loads(result)

        if data["type"] == "game":
            print(data["payload"]["type"])

            if data["payload"]["type"] in ["update", "create"]:
                snake = data["payload"]["payload"]
                objects.set(snake["id"], snake["dots"])
            elif data["payload"]["type"] == "delete":
                snake = data["payload"]["payload"]
                objects.delete(snake["id"])

            s.fill((0xaa, 0xaa, 0xaa))

            for x, y in objects.all():
                s.blit(img, (x*20, y*20))

    except KeyboardInterrupt:
        break

    pygame.display.update()
