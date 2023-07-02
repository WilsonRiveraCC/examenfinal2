import socket
import random
import time

HOST = 'localhost'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print("Conectado al servidor")

    while True:
        presion = random.uniform(5, 20)
        message = str(presion).encode()
        client_socket.send(message)
        print("Presión enviada:", presion)
        time.sleep(0.5)
