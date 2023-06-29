import socket
from threading import Thread

SOCK_BUFFER = 1024
num_hilos=0


def client_handler(conn, client_address):
    global num_hilos
    num_hilos+=1
    try:
        while True:
            data = conn.recv(SOCK_BUFFER)
            print(f"Recibi: {data}")
            if data:
                print(f"Enviando: {data}")
                conn.sendall(data)
            else:
                print("No hay mas datos")
                break
    except Exception as e:
        print(f"Exception {e}")
    finally:
        print("Cerrando conexion")
        conn.close()
    num_hilos-=1


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 5050)
    print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")
    sock.bind(server_address)

    sock.listen(5)

    while True:
        print("Esperando conexiones...")

        conn, client_address = sock.accept()

        client_thread = Thread(target=client_handler, args=(conn, client_address))
        client_thread.start()