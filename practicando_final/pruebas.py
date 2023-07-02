"""x="AAAA/MM/DD"
print(x[5:7])
a = [1, 2, 3, 4, 5]
first = a.pop(0)
 
print(first)        # 1
print(a)            # [2, 3, 4, 5]
"""
"""
# Cadena de texto
cadena = "Hola, cómo estás, hoy?"

# Usamos el método split() para dividir la cadena en palabras
palabras = cadena.split()

# Imprimimos las palabras resultantes
print(palabras)
"""
#x=[[4896, '60'], [4971, '60'], [5022, '60']]
#print(x[0][1])
import asyncio
import random

PRECIO_BASE = 20000
DURACION_SUBASTA = 60
INCREMENTO_MINIMO = 500
INCREMENTO_PORCENTUAL = 0.20

async def participante(nombre):
    mejor_oferta = PRECIO_BASE
    while True:
        tiempo_espera = random.randint(1, 10)
        await asyncio.sleep(tiempo_espera)

        oferta = random.randint(mejor_oferta + INCREMENTO_MINIMO, int(mejor_oferta * (1 + INCREMENTO_PORCENTUAL)))
        print(f"{nombre} hizo una oferta de ${oferta}")

        if oferta > mejor_oferta:
            mejor_oferta = oferta
            print(f"¡{nombre} ha hecho la mejor oferta hasta ahora: ${mejor_oferta}!")

async def subasta():
    participantes = ["Participante 1", "Participante 2", "Participante 3", "Participante 4", "Participante 5"]
    tareas = [asyncio.create_task(participante(nombre)) for nombre in participantes]

    try:
        await asyncio.sleep(DURACION_SUBASTA)
    except asyncio.CancelledError:
        print("La subasta ha sido cancelada antes de finalizar el tiempo.")

    for tarea in tareas:
        tarea.cancel()

    await asyncio.gather(*tareas, return_exceptions=True)  # Esperar a que todas las tareas se cancelen correctamente

    print("La subasta ha finalizado. Calculando el ganador...")

asyncio.run(subasta())