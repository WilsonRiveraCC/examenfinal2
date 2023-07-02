import time 
from threading import Thread

CUENTA = 50_000_000

def cuenta(n):
    while n > 0:
        n-=1
#cada uno de estos hilos en python se ejecuta de manera ininterrumpida
#mientras el hilo está haciendo tareas de cpu 
#cuando hay tareas que requieren esperas, ahí sí el hilo salta de un lado a otro
#y con esto no hay mayor beneficio y es peor en desempeño
if __name__ == "__main__":
    #generando dos hilos
    #ojo con esta parte para args si se le quita esa coma
    #no deja compilar se puede deber a que para hilos se debe 
    #de alcanzar una tupla como argumento
    t1=Thread(target=cuenta, args=(CUENTA/2,))
    t2=Thread(target=cuenta, args=(CUENTA/2,))

    inicio=time.perf_counter()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    fin=time.perf_counter()

    print(f"el tiempo de ejecución es de {fin -inicio}")