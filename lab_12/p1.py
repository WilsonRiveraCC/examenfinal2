import time
import numpy as np
from itertools import repeat
from multiprocessing import Pool, cpu_count

n=2023
def sinc_f(x):
    sum=0
    for i in range(1,10001):
        sum=sum+i*(x**i)
    return sum


def multi_f(rango):
    global n
    sum=0
    for i in range(rango[0],rango[1]):
        sum=sum+i*(n**i)
    return sum


"""
def suma(x,y):
    suma=x+y
    return suma
"""

if __name__ == '__main__':
    inicio=time.perf_counter()
    resultado_serial=sinc_f(n)
    final=time.perf_counter()
    
    num_procesos=16
    p = Pool(processes=num_procesos)
    x=10000
    division=x//num_procesos
    #el rango se presta para meterlo al for

    rango=[(i*division+1,division+division*i+1) for i in range(num_procesos)]#un rango por proceso
    p = Pool(processes=num_procesos)
    #para el caso de la función sum
    #resultado = p.starmap(suma, rango)
    
    inicio2=time.perf_counter()
    #se usa map poerque mi función tiene un soloa argumento de entrada
    resultado = p.map(multi_f, rango)
    resultado_paralelo=sum(resultado)
    p.close()
    p.join()
    final2=time.perf_counter()
    

    print(f"Tiempo total de ejecucion sincrono: {final - inicio} segundos")
    print(f"Tiempo total de ejecucion procesos: {final2 - inicio2} segundos")

    assert resultado_serial == resultado_paralelo


    #division=n//num_procesos
    #rango=list(range(1,n,division))
    #print(rango)


