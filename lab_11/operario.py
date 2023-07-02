import socket
import threading
import time

HOST = 'localhost'
PORT = 12345

def handle_client(client_socket, client_address):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode()
        if client_address == operario_address:
            print("Dato recibido del operario:", message)
        elif client_address == presion_address:
            print("Dato recibido del sensor de presión:", message)
            tiempo_actual = time.time()
            profundidad = float(message) / (1023.6 * 9.81)
            profundidad_data = "Profundidad: {} metros - Tiempo: {}".format(profundidad, tiempo_actual)
            operario_socket.send(profundidad_data.encode())
            print("Profundidad enviada al operario:", profundidad_data)
        elif client_address == oxigeno_address:
            print("Dato recibido del sensor de oxígeno disuelto:", message)
            tiempo_actual = time.time()
            oxigeno_data = "Oxígeno disuelto: {}% - Tiempo: {}".format(message, tiempo_actual)
            operario_socket.send(oxigeno_data.encode())
            print("Oxígeno disuelto enviado al operario:", oxigeno_data)

    client_socket.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print("Servidor escuchando en {}:{}".format(HOST, PORT))

    operario_socket, operario_address = server_socket.accept()
    print("Operario conectado:", operario_address)

    presion_socket, presion_address = server_socket.accept()
    print("Sensor de presión conectado:", presion_address)

    oxigeno_socket, oxigeno_address = server_socket.accept()
    print("Sensor de oxígeno disuelto conectado:", oxigeno_address)

    threading.Thread(target=handle_client, args=(operario_socket, operario_address)).start()
    threading.Thread(target=handle_client, args=(presion_socket, presion_address)).start()
    threading.Thread(target=handle_client, args=(oxigeno_socket, oxigeno_address)).start()
