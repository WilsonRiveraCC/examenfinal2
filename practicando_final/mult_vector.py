import time
import numpy as np
import random
from itertools import repeat
from multiprocessing import Pool, cpu_count

M=500
N=500

def mult_vector_vector(x,y):
    suma=0
    for i in range(len(y)):
        suma += x[i]*y[i]
    return suma

if __name__ == "__main__":
    resultado_serial =[]
    #Para este caso de acá genero vectores de tamaño 50000,
    #unos 50000 ojo
    mat_M= np.random.randint(100, size=(M,N))
    #Para este caso solo tomo un vector de tamaño N
    vector_A= np.random.randint(100, size=(N))
    
    #operación serial
    inicio= time.perf_counter()
    for vector in mat_M:
        res_parcial=mult_vector_vector(vector, vector_A)
        resultado_serial.append(res_parcial)
    fin=time.perf_counter()
    print(f"el tiempo de ejecución serial es de {fin -inicio}")

    #operación paralela
    inicio= time.perf_counter()
    args=zip(mat_M, repeat(vector_A))
    p=Pool(processes=cpu_count())
    #USO DE STARMAP POR SER 2 ARRGUMENTOS, SI ES SOLO UNO MAP
    #la ventaja de usar multiprocesos con los pool es que los valores se guardan en un lugar
    # y se evitan los race condition acá es que 
    resultado_paralelo=p.starmap(mult_vector_vector,args )
    p.close()
    p.join()
    fin=time.perf_counter()
    print(f"el tiempo de ejecución paralela es de {fin -inicio}")
    print(f"Evaluación de resultado es {resultado_serial == resultado_paralelo}")
    
    
    
    
    #cómo funciona el zip?
    #x=[1,2,3]
    #y=[4,5,6]
    #res=zip(x,y)
    #list(res) junta en tuplas
     
    """Para el caso de usar el repeat
    x=[1,2,3] 
    y=[4]
    from itertools import repeat 
    res=zip(x,repeat(y))
    list(res)
    [(1, [4]), (2, [4]), (3, [4])]"""
    #combinamos todo y rellenamos cuando no hay argumento


