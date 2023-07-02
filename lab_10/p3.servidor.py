import time
import asyncio
import random
import socket

PRECIO_MINIMO = 20000   # El precio base al que se inicia la subasta
PRECIO_MAXIMO = 100000  # El precio máximo que cualquiera de los participantes está dispuesto a pagar
TIEMPO_SUBASTA = 60
SNIPER_TIME = 3  # Tiempo restante para que el sniper haga su oferta

# Dirección y puerto del servidor
SERVER_ADDRESS = ('localhost', 8888)

flag = True

async def controlatiempo():
    print("Iniciando subasta...")
    global flag
    await asyncio.sleep(TIEMPO_SUBASTA)
    flag = False
    print("Subasta finalizada.")

async def oferta_participante(p):
    oferta = random.randint(PRECIO_MINIMO, PRECIO_MAXIMO)
    await asyncio.sleep(random.randint(1, 10))
    return p, oferta

async def reoferta(participante, monto_mayor):
    monto_actual = participante[1]
    if monto_actual <= monto_mayor:
        nuevo_minimo = float(monto_actual) + 500
        nuevo_maximo = float(monto_actual) * 1.20
        nueva_oferta = random.uniform(nuevo_minimo, nuevo_maximo)
        await asyncio.sleep(random.randint(1, 10))
        return nueva_oferta

async def sniper():
    # Cliente para enviar el número al servidor
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(SERVER_ADDRESS)

    # Número ingresado por el cliente
    num = input("Ingrese un número: ")

    # Envía el número al servidor
    client_socket.sendall(num.encode())

    # Cierra la conexión
    client_socket.close()

async def main(p):
    task_tiempo = asyncio.create_task(controlatiempo())
    res = await asyncio.gather(*(oferta_participante(i) for i in p))
    res.sort(key=lambda x: x[1])  # Ordena el arreglo considerando el segundo elemento
    max_oferta = res[4][1]
    j = 0
    while flag:
        if j == 0:
            reoferta_p = await asyncio.gather(*(reoferta(i, max_oferta) for i in res))
            reoferta_p.sort(key=lambda x: x[1])  # Ordena el arreglo considerando el segundo elemento
            max_oferta = reoferta_p[4][1]
            j = 1
            continue
        reoferta_p = await asyncio.gather(*(reoferta(i, max_oferta) for i in reoferta_p))
        reoferta_p.sort(key=lambda x: x[1])  # Ordena el arreglo considerando el segundo elemento
        max_oferta = reoferta_p[4][1]

    return reoferta_p

if __name__ == "__main__":
    p = ["a", "b", "c", "d", "e", "Sniper"]

    # Inicia el servidor para recibir la oferta del Sniper
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(SERVER_ADDRESS)
    server_socket.listen(1)

    print("Esperando conexión del cliente...")
    client_socket, _ = server_socket.accept()
    print("Cliente conectado.")

    # Recibe el número enviado por el cliente
    num_data = client_socket.recv(1024)
    num = num_data.decode()

    # Guarda el número en el archivo oferta_del_sniper.txt
    with open("oferta_del_sniper.txt", "w") as file:
        file.write(num)

    # Cierra la conexión
    client_socket.close()
    server_socket.close()

    # Ejecuta el programa del Sniper después de 57 segundos
    asyncio.run(asyncio.sleep(TIEMPO_SUBASTA - SNIPER_TIME))
    asyncio.run(sniper())

    # Espera a que termine la subasta
    asyncio.run(main(p))
