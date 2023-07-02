import requests
import multiprocessing
import time


def potencia(n: int, div: int = 1) -> int:
    res = 1
    for _ in range(1, (n // div) + 1):
        res *= n
    
    return res


if __name__ == '__main__':
    with multiprocessing.Pool(initializer=potencia, processes=multiprocessing.cpu_count()) as pool:
        pool.starmap()
    print(f"Tiempo total de ejecucion: {fin - inicio} segundos")