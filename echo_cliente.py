import socket
import time
import random


SOCK_BUFFER = 4
MSG_NUM=10
SLEEP_TIME=2

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5050)
    print(f"Conectando al servidor en {server_address[0]} y puerto {server_address[1]}")

    sock.connect(server_address )
    try:
        for i in range(MSG_NUM):
            msg = f"Este es el mensaje de prueba {i+1}"
            msg = msg.encode('utf-8')
            sock.sendall(msg)
            amnt_recvd=0
            amnt_expected= len(msg)
            msg_rx=""

            while amnt_recvd < amnt_expected:
                data = sock.recv(SOCK_BUFFER)
                amnt_recvd += len(data)
                msg_rx += data.decode('utf-8')
                
            print(f"Mensaje completo: {msg_rx}")
            time.sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        print("Usuario canceló el programa")
        sock.close()
    
    except Exception as e:
        print(f"Excepción: {e}")
        sock.close()       
    finally:
        print("Cerrando socket")
        sock.close()