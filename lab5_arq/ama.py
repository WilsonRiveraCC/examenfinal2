import time
import multiprocessing

def f1(x):
    suma = 0
    for i in range(2500):
        suma += (i + 1) * (x ** (i + 1))
    return suma

def f2(x):
    suma = 0
    for i in range(2500):
        suma += (i + 2501) * (x ** (i + 2501))
    return suma

def f3(x):
    suma = 0
    for i in range(2500):
        suma += (i + 5001) * (x ** (i + 5001))
    return suma

def f4(x):
    suma = 0
    for i in range(2500):
        suma += (i + 7501) * (x ** (i + 7501))
    return suma

if __name__ == '__main__':
    inicio = time.perf_counter()
    x = 2023
    pool = multiprocessing.Pool()
    results = [pool.apply_async(f, (x,)) for f in [f1, f2, f3, f4]]
    output = [r.get() for r in results]
    tiempo_total = time.perf_counter() - inicio
    print(f'Tiempo total de ejecución: {tiempo_total} segundos')