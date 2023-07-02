import socket
import time 
from csv import writer
import pickle

SOCK_BUFFER = 1024

if __name__ == '__main__':
    # Creamos el objeto de socket para el servidor
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 5231)
    print(f"Iniciando el servidor en la direccion {server_address[0]} y puerto {server_address[1]}")
    sock.bind(server_address)

    # Escuchamos conexiones
    sock.listen(1)

 
    print("Esperando conexiones...")
    conn, client_address = sock.accept()
    try:
        informacion_data= conn.recv(SOCK_BUFFER)
        datos_paciente= pickle.loads(informacion_data)
        print(f'la lista es {datos_paciente}')
        print(f"Conexion establecida con {client_address}")

        with open('pacientes.csv', 'a', newline='') as f_object:  
            writer_object = writer(f_object)
            writer_object.writerow(datos_paciente)  
            f_object.close()
    except ConnectionResetError:
        print("Conexion cerrada por el cliente abruptamente")
    finally:
        print("El cliente ha cerrado la conexion")
        conn.close()