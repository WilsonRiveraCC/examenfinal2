import time
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import csv
import requests
import copy
import math

lineas=[]
copia_lineas=[]

def download_file():
    global lineas
    global copia_lineas
    url = "https://jobenas-misc-bucket.s3.amazonaws.com/household_power_consumption.csv"
    with requests.get(url) as resp:
        with open ('household_power_consumption.csv', 'wb') as file:
            file.write(resp._content)
    with open('household_power_consumption.csv',encoding='latin1') as data:
        Datos_consumo = csv.reader(data, delimiter = ',') 
        lineas = list(Datos_consumo)
    copia_lineas=lineas[1:]#sin encabezado


def get_cols():
    global lineas
    columna=lineas[0]
    return columna



"""
Crear una función llamada get_day que reciba como parámetro de 
entrada un string de que indique la fecha en formato “AAAA/MM/DD” y que 
retorne una lista de listas con todos los puntos que correspondan a dicho día
"""
def get_day(fecha):
    global copia_lineas
    fechas=[]

    for i in range(len(copia_lineas)):
        if(fecha==copia_lineas[i][0][0:10]): #SE LE AGREGA EL [0:10] PORQUE DESEO COMPARAR SOLO FECHA Y NO HORA 
            fechas.append(copia_lineas[i])
    return fechas

def cambiar_formato():
    global copia_lineas
    for i in range(len(copia_lineas)):
        fecha_separada=copia_lineas[i][0].split("-")
        fecha_nueva=fecha_separada[0] + "/" + fecha_separada[1] + "/" + fecha_separada[2]
        copia_lineas[i][0]=fecha_nueva


"""Crear una función llamada get_mean que reciba como parámetro de 
entrada un string que indique la fecha en formato “AAAA/MM/DD” y que retorne 
el valor promedio de potencia global que correspondan a dicho día.
"""
def get_mean(fecha):
    #formato AAAA/MM/DD
    fechas=[]
    potencia=[]
    fechas=get_day(fecha)
    for i in range(len(fechas)):
        pot=math.sqrt(float(fechas[i][1])**2+float(fechas[i][2])**2)
        potencia.append(pot)
    return sum(potencia)/len(potencia)    
    
    


if __name__ == "__main__":
    download_file()
    cambiar_formato()
    lista_=get_day("2008/01/16")
    pot=get_mean("2008/01/16")
    print(pot)




