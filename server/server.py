import socket
from threading import Thread
import json

HOST = "127.0.0.1"
PORT = 9123
MAX_PLAYERS = 2
players = []
serverSocket = socket.socket()
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)


def handler_client(conn):
    player = {
        "x": 0,
        "y": 0
    }
    while True:
        try:
            data = conn.recv(1024)
            data = json.loads(data.decode('utf-8'))
            if data["request"] == "get_players":
                print("Отдаём игроков")
            if data["request"] == "move":
                if data["move"] == "left":
                    player["x"] -= 5
                if data["move"] == "right":
                    player["x"] += 5
                if data["move"] == "top":
                    player["y"] -= 5
                if data["move"] == "bottom":
                    player["y"] += 5
        except:
            pass

while True:
    if len(players) <= MAX_PLAYERS:
        conn, addr = serverSocket.accept()
        print("Подключён клиент, ",addr)
        Thread(target=handler_client, args=((conn, ))).start()