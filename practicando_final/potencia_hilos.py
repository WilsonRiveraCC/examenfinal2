import time
from threading import Thread

def potencia(n: int, div: int = 1) -> int:
    res = 1
    print(div)
    for _ in range(1, (n // div) + 1):
        res *= n
    
    return res



if __name__ == '__main__':
    n=100_000
    inicio = time.perf_counter()
    pot = potencia(n)
    fin = time.perf_counter()
    


    t1=Thread(target=potencia, args=(n, 4))
    t2=Thread(target=potencia, args=(n, 4))
    t3=Thread(target=potencia, args=(n, 4))
    t4=Thread(target=potencia, args=(n, 4))
    inicio2 = time.perf_counter()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    fin2 = time.perf_counter()

    print(f"Tiempo total de ejecucion sincrono: {fin - inicio} segundos")
    print(f"Tiempo total de ejecucion hilos: {fin2 - inicio2} segundos")