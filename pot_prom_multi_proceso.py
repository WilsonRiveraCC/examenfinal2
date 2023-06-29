import time
import multiprocessing as mp

#FORMA MÁS EFICIENTE PARA EJECUTAR ESTO CREANDO
#POOL 
def fun(x):
    val=1
    val=x*2
    time.sleep(0.05)
    return val


if __name__ == "__main__":
    nums = [x for x in range(100, 200)]
    acc=0
    #creamos nuestro pool que va a ser la misma cantidad de elementos
    #que los núcleos de cpu
    p=mp.Pool(processes=mp.cpu_count())

    inicio= time.perf_counter()
    #aplicamos y se va a llamar a una función por cada valor de num
    resultados =p.map(fun,nums)
    #cerrar pool para no aceptar más valores
    p.close()
    #esperamos a que terminen los procesos
    p.join()

    for resultado in resultados:
        acc+= resultado
    prom=acc/len(nums)
    fin=time.perf_counter()

    print(f"el tiempo de ejecución es de {fin -inicio}")

