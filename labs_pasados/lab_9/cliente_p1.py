import socket
import time
import random
import csv
import pickle

SOCK_BUFFER = 4

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5231)
    print(f"Conectando al servidor en {server_address[0]} y puerto {server_address[1]}")

    sock.connect(server_address )
    
    try:
        print(f'Ingrese datos del paciente:\n')
        nombre= input(f'Nombre(s):')
        apellido= input(f'Apellidos:')
        peso=input("Peso(kg):")
        talla=input("Talla(cm):")
        edad=input("Edad:")
        seguro=input("¿Cuenta con seguro? (s/n):")
        informacion=[nombre, apellido, peso, talla, edad, seguro]
        if(informacion[5]=="s"):
            informacion[5]= "True"
        else:
            informacion[5]= "False"
        informacion_dt= pickle.dumps(informacion)
        sock.sendall(informacion_dt)
    finally:
        print("Cerrando socket")
        sock.close()

