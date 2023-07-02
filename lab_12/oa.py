import time
import numpy as np
from multiprocessing import Pool, cpu_count

def multi_f(min, max, n):
    sum = 0
    for i in range(min, max+1):
        sum = sum + i * (n**i)
    return sum

if __name__ == '__main__':
    n = 2023
    inicio = time.perf_counter()
    num_procesos = 4
    division = 10000 // num_procesos
    rango = [(i, i+division, n) for i in range(1, 10000, division)]
    print(rango)
    p = Pool(processes=num_procesos)
    #acá se usa starmap porque mi función  tiene dos entradas
    resultado = p.starmap(multi_f, rango)
    p.close()
    p.join()
    
    suma_total = sum(resultado)
    
    final = time.perf_counter()
    

    print(f"Tiempo total de ejecución: {final - inicio} segundos")
