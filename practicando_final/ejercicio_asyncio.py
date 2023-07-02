import asyncio
import time

async def cuenta(idx: int):
    print(f"[{idx}] Uno")
    #se comporta en plan mientras que espero voy ejecutando la otra función
    await asyncio.sleep(19)
    print(f"[{idx}] Dos")

#cuando no se le colcoa el tiempo esta función como tal se ejecuta de manera síncrona
#por eso entra y sale al instante en este caso no deja de hacer lo que está haciendo tal 
#como sucede en las otras dos funciones
#sino le pongo tiempo de espera a cada función pareciera si es que lo corre en paralelo. Sinembargo, 
#3 no lo hace por que mis recursos de mi pc tampoco se alteran
async def suma():
    print("entre")
    suma=0
    for i in range(40):
        suma=suma+i
    print(suma)

#async def main():
#    este va a recoger los resultados de las llamadas de las otras funciones 
# ejecuta de manera asíncrona estas 3 funciones y las espera a que esa terminen 
#    await asyncio.gather(cuenta(0),cuenta(1),cuenta(2), suma())

"""
El código *(cuenta(i) for i in range(5)) desempaqueta los valores generados por la expresión cuenta(i) for i in range(5). En este caso, cuenta(i) representa una función o expresión que devuelve un valor para cada valor de i en el rango del 0 al 4. La expresión cuenta(i) for i in range(5) crea 
un generador que produce estos valores.Al utilizar el operador "*", se desempaquetan
los valores generados por el generador y se pasan como argumentos individuales a la función o constructor que los recibe. En este caso, los valores generados por el generador
se desempaquetan y se pasan como argumentos individuales a una función o constructor no especificada en el código que has proporcionado.
En resumen, el código *(cuenta(i) for i in range(5)) toma los valores generados por el generador y los pasa como argumentos
individuales a una función o constructor específico que no está visible en el código proporcionado."""
#se genera el main de otra forma con esta sintaxis
async def main():
    await asyncio.gather(*(cuenta(i) for i in range(100000)))


if __name__ == "__main__":
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()

    print(f"El programa ejecuto en {fin-inicio} segundos")

