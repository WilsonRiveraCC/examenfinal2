import time
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import csv
import requests
import copy
import math
import numpy as np

lineas = []
copia_lineas=[]#se utiliza para copiar los elementos de la lista a la original
#ya se sabe que para variables globales dentro de una función se le llama 
#como global variable
lista_dia=[]
fechas_nuevo_formato=[]

#ojo cuando voy a descargar desde git hub 
#se copia el url desde donde dice RAW
def download_file():
    global lineas # se utiliza para guardar las filas del archivo separado por comas que se abrió
    url="https://raw.githubusercontent.com/WilsonRiveraCC/examenfinal2/main/household_power_consumption.csv"
    
    #consigo el código con request y guardo lo que abro en resp resp se vuelve un objeto
    with requests.get(url) as resp:
        #acá se abre/crea  el documento de household_..... como wb que es escritura y b en binario
        #y le asigno como nombre y objeto file
        with open ('household_power_consumption.csv', 'wb') as file: 
            #luego escribo el contenido de resp a file que en este caso es el documento en csv 
            # y se le guarda el valor en binario del url resp  
            file.write(resp._content)
    with open('household_power_consumption.csv',encoding='latin1') as data:
        Datos_consumo = csv.reader(data, delimiter = ',')
        # de esta manera se pasa a arreglo mi lista separadas por espacio y comas
        # solo asume que en cada salto de línea que hay es una nueva fila 
        lineas = list(Datos_consumo)
        #print(Datos_consumo) no se puede imprimir como tal es un objeto

def get_cols():
    encabezado=str(lineas[0])
    return encabezado

def get_day(fecha):
    #formato de la fecha AAAA/MM/DD
    lista_dia=[]
    for i in fecha:
        lista_dia.append(i[8:10])
    return lista_dia

def organizar_db():
    #función que organiza las fechas al nuevo formato que dan
    #formato de la fecha solicitada AAAA/MM/DD
    #formato de lo que tenemos 16/12/2016
    global lineas
    global copia_lineas
    global fechas_nuevo_formato
    fila_fecha=[]
    #Si la lista tiene objetos que quieres copiar completamente entonces puedes hacer uso del 
    #método deepcopy() del modulo copy.
    #nueva_lista = copy.deepcopy(vieja_lista)
    copia_lineas = copy.deepcopy(lineas)
    #primer elemento a partir de 1, 0 es el encabezado
    j=0

    #Para almacenar solo las fechas en un solo arreglo
    for fecha in copia_lineas:
        if (j==0):
            j=1
            pass #omito el primer término que viene a ser el fecha_sin_encabezado
        #para separar el string de fechas=
        fila_fecha.append(fecha)#saco encabezado
    
    #luego se separa
         






if __name__ == "__main__":
    download_file()
    #print(lineas)






    """
    def get_site(url: str, session: requests.Session):
        with session.get(url) as response:
            print(f"Lei {len(response.content)} bytes de {url}")

    def get_all(sites: list[str]):
        with requests.Session() as session:
            for url in sites:
                get_site(url, session)

    if __name__ == "__main__":
        sites = [
            "https://www.jython.org",
            "http://olympus.realpython.org/dice"
        ] * 80

        inicio = time.perf_counter()
        get_all(sites)
        fin = time.perf_counter()

        print(f"Descarga completa sincrona en {fin - inicio} segundos")
    """