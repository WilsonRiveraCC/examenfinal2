import time
import asyncio
import random

PRECIO_MINIMO = 20000  # El precio base al que se inicia la subasta
PRECIO_MAXIMO = 100000  # El precio máximo que cualquiera de los participantes está dispuesto a pagar (úsalo como tope en random.randint())
TIEMPO_SUBASTA = 60
flag = True


async def controlatiempo():
    global flag
    await asyncio.sleep(TIEMPO_SUBASTA)
    flag = False


async def oferta_participante(p):
    oferta = random.randint(PRECIO_MINIMO, PRECIO_MAXIMO)
    await asyncio.sleep(random.randint(1, 10))
    return p, oferta


async def reoferta(participante, monto_mayor):
    monto_actual = participante[1]
    if monto_actual <= monto_mayor:
        nuevo_minimo = monto_actual + 500
        nuevo_maximo = int(nuevo_minimo * 1.20)
        nueva_oferta = random.randint(nuevo_minimo, nuevo_maximo)
        await asyncio.sleep(random.randint(1, 10))
        return participante[0], nueva_oferta
    else:
        return participante


async def main(p):
    asyncio.create_task(controlatiempo())
    res = await asyncio.gather(*(oferta_participante(i) for i in p))
    res.sort(key=lambda x: x[1])  # ordeno el arreglo considerando el segundo elemento
    max_oferta = res[-1][1]
    while flag:
        reoferta_participantes = await asyncio.gather(*(reoferta(i, max_oferta) for i in res))
        reoferta_participantes.sort(key=lambda x: x[1])  # ordeno el arreglo considerando el segundo elemento
        max_oferta = reoferta_participantes[-1][1]
        if res == reoferta_participantes:
            break
        res = reoferta_participantes
    return res


if __name__ == "__main__":
    p = ["a", "b", "c", "d", "e"]
    res = asyncio.run(main(p))
    res.sort(key=lambda x: x[1], reverse=True)
    ganador = res[0]
    print("Ganador:", ganador[0], "con una oferta de $", ganador[1])