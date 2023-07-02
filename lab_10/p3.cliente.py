import socket

SERVER_ADDRESS = ('localhost', 8888)

# Crea el socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(SERVER_ADDRESS)

# Ingresa el número por el terminal
num = input("Ingrese un número: ")

# Envía el número al servidor
client_socket.sendall(num.encode())

# Cierra la conexión
client_socket.close()


