import time
import numpy as np
import csv

alumnos = list()

if __name__ == '__main__':
    lista_pacientes=[]
    lista_posicion_edades=[]
    lista_pacientes_ordenados=[]
    posicion=[]
    matriz_tamano=[500,1000,1500,2000,2500,3000,3500,4000,4500,5000]

    tiempos_lectura = []
    tiempos_escritura = []
    tiempos_ordenar = []


    with open("pacientes.csv", "r") as archivo:
        contenido = archivo.read()
    filas = list(contenido.split("\n"))

    
    for N in matriz_tamano:
        inicio=time.perf_counter()
        for i in range(1, N+1):
            lista_pacientes.append(filas[i].split(","))
        
        j=0
        for i in lista_pacientes:
            lista_posicion_edades.append([j, i[4]])
            j=j+1


        #ordenar las edades de menor a mayor
        lista_posicion_edades.sort(key = lambda x: x[1])   #index 1 means second element

        #acomodando la nueva lista de pacientes ordenados por edades
        
        for i in range(0, len(lista_posicion_edades)):
            posicion.append(lista_posicion_edades[i][0])

        for i in posicion:
            lista_pacientes_ordenados.append(lista_pacientes[i])
        

        with open('myfile.csv', 'w', newline='') as file:
            mywriter = csv.writer(file, delimiter=',')
            mywriter.writerows(lista_pacientes_ordenados)
        final=time.perf_counter()