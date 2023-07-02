import socket
import random
import time

HOST = 'localhost'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print("Conectado al servidor")

    while True:
        oxigeno = random.randint(0, 100)
        message = str(oxigeno).encode()
        client_socket.send(message)
        print("Oxígeno enviado:", oxigeno)
        time.sleep(0.3)
