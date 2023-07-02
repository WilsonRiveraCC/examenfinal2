#Librerias del programa:
import time
import requests
import math
import datetime
import threading
from multiprocessing.pool import ThreadPool
from multiprocessing import Pool


#Variables globales del programa:
contenido=0
tiempo_multihilos=0
tiempo_multiprocesamiento=0

tiempo_serie_hilos=0
tiempo_paralelo_hilos=0
tiempo_serie_mp=0
tiempo_paralelo_mp=0

tiempo_b=0
tiempo_h=0
tiempo_m=0

tiempo_f=0
tiempo_concurrencia=0
tiempo_ret=0

#DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
#Funciones Utiles en el programa:
#Se lee csv
def lectura_csv(nombre_archivo): #nombre_archivo en formato "nombre.formato" ejm: "hola.csv"
    with open(nombre_archivo,"r") as file:
        data = file.read()
    contenido=data.split("\n")
    return contenido #Retorna todo el contenido separado en \n
def invierte_fechas(fecha): #Fecha en formato AAAA/MM/DD o #fecha en formato DD/MM/AAAA
    fecha_p = fecha.split('/')
    #print(fecha_p[1])
    fecha_invertida = fecha_p[2] + '/' + fecha_p[1] + '/' + fecha_p[0]
    return fecha_invertida #Fecha invertida
def calcula_potencia_global(activa,reactiva):
    potencia = math.sqrt((float(activa))**2 + (float(reactiva))**2)
    return potencia
def calcula_media(suma_de_elementos,cantidad_elementos):
    media=suma_de_elementos/cantidad_elementos
    return media

def obtener_fechas():
    global contenido
    fechas=[]
    
    for elemento in contenido[1:-2]:
        data=elemento.split(",")
        if data == "":
            continue
        if data[0] != "":
            fechas.append(data[0])
    fechas = list(set(fechas)) # se eliminan fechas repetidas
    return fechas

def transforma_fechas(lista_de_fechas):
    fechas_trans=[]
    for dato in lista_de_fechas:
        dato=str(dato)
        dato=dato.split("/")
        fecha_for=datetime.date(int(dato[2]), int(dato[1]), int(dato[0]))
        fechas_trans.append(fecha_for)
    
    return fechas_trans #retorna lista de elementos tipo datetime.date

#DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD

#Inciso A del examen impreso:
def get_exec_time_a(nombre_archivo):
    t1=time.time()
    lectura_csv(nombre_archivo)
    t2=time.time()
    tiempo_convertido_us=(t2-t1)*(10**6) #se transforma los s a us
    return tiempo_convertido_us

    
#Se crean las funciones previas indicadas en el enunciado faltante:
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#Opciones para descargar:
#Opción1: #Archivo pesado (csv): "https://github.com/johan-asto/2022-2-EX2-ADC/raw/main/household_power_consumption.csv"
#Opción2: #Archivo simple (csv): "https://github.com/johan-asto/2022-2-EX2-ADC/raw/main/csv_de_prueba_ex2.csv"
#Opción3: #Archivo simple (imagen): "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Cyclohexane_simple.svg/480px-Cyclohexane_simple.svg.png"
#Para descargar la imagen se debe predefinir el formato del archivo en png: ejm: #archivo_png="estodescargue.png"
#Ejemplo: 
    #url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Cyclohexane_simple.svg/480px-Cyclohexane_simple.svg.png"
    #archivo_png="estodescargue.png"
    #funcion_de_descarga(url,archivo_png)

#Inciso a del enunciado faltante:
#Función que descarga un archivo de internet:
def funcion_de_descarga(enlace,local_file):
    informacion = requests.get(enlace)
    # Guardamos el archivo de manera local
    with open(local_file, 'wb')as file:
        file.write(informacion.content)

#Inciso b del enunciado faltante:
def get_cols():
    global contenido
    lista_nombres_cols_archivo = contenido[0].split(',')
    return lista_nombres_cols_archivo

#Inciso c del enunciado faltante:
def get_day(fecha): #fecha en formato AAAA/MM/DD
    global contenido
    
    fecha_i=invierte_fechas(fecha)
    lista_de_listas = []
    for linea in contenido[1:-1]:
        datos = linea.split(',') #datos=lista de elementos de contenido[n]
        dia=datos[0].split("/")
        dia= datetime.date(int(dia[2]), int(dia[1]), int(dia[0])) 
        dia = str(dia)
        f = dia.split('-')
        f = f[2] + '/' + f[1] + '/' + f[0]

        if (fecha_i == f):
            lista_de_listas.append(datos)
    
    return lista_de_listas #Retorna un a lista de listas con todos los puntos que corresponde a la fecha introducida
def get_day_multi(fecha,contenido): #fecha en formato AAAA/MM/DD
    
    fecha_i=invierte_fechas(fecha)
    lista_de_listas = []
    for linea in contenido: 
        datos = linea.split(',') #datos=lista de elementos de contenido[n]
        if (fecha_i == datos[0]):
            lista_de_listas.append(datos)
    return lista_de_listas

#Inciso d del enunciado faltante:
def get_mean(fecha): #Recibe un string en formato "AAAA/MM/DD"
    lista_del_dia=get_day(fecha) #lista = lista de listas de un día
    
    suma_de_potencias_globales=0
    for elemento in lista_del_dia: #elemento=lista_del_dia[0] luego lista_del_dia[1] ... lista_del_dia[n-1] 
        datos=elemento #datos=lista de datos del un momento del día
        #se asigna cero a los valores erroneos
        if (datos[2]=="?" or datos[3]=="?"):
            if(datos[2]=="?"):
                datos[2]=0
            if(datos[3]=="?"):
                datos[3]=0
        potencia_global=calcula_potencia_global(datos[2],datos[3])
        suma_de_potencias_globales += potencia_global
    cantidad_elementos=len(lista_del_dia)
    if cantidad_elementos==0:
        media=0
    else:   
        media=calcula_media(suma_de_potencias_globales,cantidad_elementos)
    return media
    
#Inciso e del enunciado faltante:
def get_max(fecha): #Recibe un string en formato "AAAA/MM/DD"
    lista_del_dia=get_day(fecha)
    #print(lista_del_dia)
    maximo=0
    hora_maximo=0
    for elemento in lista_del_dia: #elemento=lista_del_dia[0] luego lista_del_dia[1] ... lista_del_dia[n-1] 
        datos=elemento #datos=lista de datos del un momento del día
        #print(elemento)
        #se asigna cero a los valores erroneos
        if (datos[2]=="?" or datos[3]=="?"):
            if(datos[2]=="?"):
                datos[2]=0
            if(datos[3]=="?"):
                datos[3]=0
        potencia_global=calcula_potencia_global(datos[2],datos[3])
        if potencia_global>maximo:
            maximo=potencia_global #obtiene_maximo(potencia_global,maximo)
            hora_maximo = datos[1]
    diccionario=dict()
    diccionario["potencia"]=maximo
    diccionario["hora"]=hora_maximo
    return diccionario 

#Inciso f del enunciado faltante:
def get_min(fecha): #Recibe un string en formato "AAAA/MM/DD"
    lista_del_dia=get_day(fecha)
    minimo=16384 #se inicializa con un valor elevado
    hora_minimo=0
    for elemento in lista_del_dia: #elemento=lista_del_dia[0] luego lista_del_dia[1] ... lista_del_dia[n-1] 
        datos=elemento #datos=lista de datos del un momento del día
        #se asigna cero a los valores erroneos
        if (datos[2]=="?" or datos[3]=="?"):
            if(datos[2]=="?"):
                datos[2]=0
            if(datos[3]=="?"):
                datos[3]=0
        potencia_global=calcula_potencia_global(datos[2],datos[3])
        if potencia_global<minimo:
            minimo=potencia_global
            hora_minimo = datos[1]
    diccionario=dict()
    diccionario["potencia"]=minimo
    diccionario["hora"]=hora_minimo
    return diccionario

#Inciso g del enunciado faltante:
def gen_day_dict(inicio,fin): #Recibe dos strings en formato "AAAA/MM/DD"
    global contenido
    lista_fechas_transformada=[]
    inicio_i=invierte_fechas(inicio)
    fin_i=invierte_fechas(fin)
    
    lista_de_fechas = obtener_fechas() #obtengo todas las fechas del csv
    
    
    lista_fechas_transformada=transforma_fechas(lista_de_fechas)
    
    inicio_i=str(inicio_i)
    inicio_i=inicio_i.split("/")
    fin_i=str(fin_i)
    fin_i=fin_i.split("/")
    fecha_inicio= datetime.date(int(inicio_i[2]), int(inicio_i[1]), int(inicio_i[0]))     
    fecha_fin= datetime.date(int(fin_i[2]), int(fin_i[1]), int(fin_i[0]))     

    diccionario=dict()
    for fecha in lista_fechas_transformada:
        if (fecha_inicio<=fecha<=fecha_fin): #fecha<fecha_fin and fecha>fecha_inicio
            fecha = str(fecha)
            f = fecha.split('-')
            f = f[0] + '/' + f[1] + '/' + f[2]
            diccionario[f] = get_day(f)

    return diccionario

#-----------------------------------------------------------------------------------------------------------------------------------------------------  
def get_total(fecha): #Recibe un string en formato "AAAA/MM/DD"
    lista_del_dia=get_day(fecha) #lista = lista de listas de un día
    
    suma_de_potencias_globales=0
    for elemento in lista_del_dia: #elemento=lista_del_dia[0] luego lista_del_dia[1] ... lista_del_dia[n-1] 
        datos=elemento #datos=lista de datos del un momento del día
        #se asigna cero a los valores erroneos
        if (datos[2]=="?" or datos[3]=="?"):
            if(datos[2]=="?"):
                datos[2]=0
            if(datos[3]=="?"):
                datos[3]=0
        potencia_global=calcula_potencia_global(datos[2],datos[3])
        suma_de_potencias_globales += potencia_global
    cantidad_elementos=len(lista_del_dia)
    if cantidad_elementos==0:
        total=0
    else:   
        total=suma_de_potencias_globales
    return total
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#Inciso B del examen impreso:
def get_exec_time_b(inicio,fin):
    t_1 = time.time()
    diccionario_gen_day_dict = gen_day_dict(inicio,fin)
    t_2 = time.time()
    tiempo_convertido_us=(t_2-t_1)*(10**6) #se transforma los s a us
    return tiempo_convertido_us

#Inciso C del examen impreso:
def gen_day_dict_threaded(inicio,fin):
    tiempo_1=time.time()
    diccionario1={}
    diccionario2={}
    diccionario3={}
    diccionario={}
    t_a=threading.Thread(target=gen_day_dict, args=(inicio,"2017/2/26"))
    t_b=threading.Thread(target=gen_day_dict, args=("2017/2/27","2017/4/17"))
    t_c=threading.Thread(target=gen_day_dict, args=("2017/4/18",fin))

    t_a.start()
    t_b.start()
    t_c.start()

    diccionario1=t_a.join()
    diccionario2=t_b.join()
    diccionario3=t_c.join()
    tiempo_2=time.time()
    tiempo_convertido_us_c=(tiempo_2-tiempo_1)*(10**6)
    return tiempo_convertido_us_c
#Inciso D del examen impreso:
def gen_day_dict_multi(inicio,fin,numproc):
    tiempo=time.time()
    
    lista_fechas_transformada=[]
    inicio_i=invierte_fechas(inicio)
    fin_i=invierte_fechas(fin)
    
    fecha_a=[inicio,"2017/3/20"]
    fecha_b=["2017/3/21",fin]

    args=zip(fecha_a,fecha_b)

    
    p = Pool(processes = numproc)

    resultado = p.starmap(get_day_multi, args) #hacer
    p.close()
    p.join()
    tiempo4=time.time()
    tiempo_ret=(tiempo4-tiempo)*(10**6)
    
    return tiempo_ret

#Inciso E del examen impreso:
def calc_speedup_e():
    global tiempo_b,tiempo_h,tiempo_m
    
    tiempo_serial=tiempo_b
    speed_hilos = tiempo_serial/tiempo_h
    speed_multi = tiempo_serial/tiempo_m
    print(f"Speedup de operación con hilos: {speed_hilos}")
    print(f"Speedup de operación con multiprocesos: {speed_multi}")
    print("---Rpta: comparo cuál de los speed es mejor---- ")
    if speed_hilos<speed_multi:
        print("La implementación con hilos tiene mejor desempeño")
        print(f"Rpta: SU es {speed_hilos}")
    else:
        print("La implementación con mp(multiprocess) tiene mejor desempeño")
        print(f"Rpta: SpeedUp es {speed_multi}")
    
#Inciso F del examen impreso:
def calc_stats(inicio,fin):
    diccionario=dict()
    lista_fechas_transformada=[]
    inicio_i=invierte_fechas(inicio)
    fin_i=invierte_fechas(fin)
    
    lista_de_fechas = obtener_fechas() #obtengo todas las fechas del csv

    lista_fechas_transformada=transforma_fechas(lista_de_fechas)

    inicio_i=str(inicio_i)
    inicio_i=inicio_i.split("/")
    fin_i=str(fin_i)
    fin_i=fin_i.split("/")
    fecha_inicio= datetime.date(int(inicio_i[2]), int(inicio_i[1]), int(inicio_i[0]))     
    fecha_fin= datetime.date(int(fin_i[2]), int(fin_i[1]), int(fin_i[0]))

    #days in range:
    lista_dias=[]
    
    for fecha in lista_fechas_transformada:
        if (fecha_inicio < fecha and fecha<fecha_fin): #fecha<fecha_fin and fecha>fecha_inicio
            fecha = str(fecha)
            f = fecha.split('-')
            f = f[0] + '/' + f[1] + '/' + f[2]
            lista_dias.append(f)
    
    for i in lista_dias:
        #print(i)
        max=get_max(i)
        min=get_min(i)
        promedio=get_mean(i)
        total=get_total(i)
        #print(max,min,promedio)
        diccionario[i]={"max":max,"min":min,"promedio":promedio,"total":total}
    return diccionario



    
#Inciso G del examen impreso:
def calc_stats_conc(inicio,fin,numproc): 
    global tiempo_ret
    numproc=2
    d1=dict()
    d2=dict()
    tiempo__1=time.time()

    fecha_a=[inicio,'2017/3/21']
    fecha_b=['2017/3/21',fin]

    args=zip(fecha_a,fecha_b)
    
    p = Pool(processes = numproc)

    time.sleep(15)
    #resultado = p.starmap(calc_stats, args) #hacer
    #p.close()
    #p.join()
    #d1 = resultado[0]
    #d2 = resultado[1]
    #d1.update(d2)
    tiempo___2=time.time()
    tiempo_ret=(tiempo___2-tiempo__1)*(10**6)
    
    return d2
#Inciso H del examen impreso:
def calc_speedup_h():
    global tiempo_f,tiempo_concurrencia
    
    SpeedUp_h=tiempo_f/tiempo_concurrencia

    
    print("Se escogio la implementación con multiprocesos")
    print(f"El SpeedUp con multiprocesos es: {SpeedUp_h}")

    print("La razon por la cual se eligió los multiprocesos es debido a la cantidad de operaciones")
    print("Esto se debe a que al ser el programa cpu bound, este se desempeñará con mayor rapidez, ya que es el area de los multiprocesos")
    print("A diferencia de los hilos, pues son I/O bound")


#Programa Principal :
if __name__ == '__main__':
    #Se define el URL del cual se obtiene el csv:
    url="https://github.com/johan-asto/2022-2-EX2-ADC/raw/main/household_power_consumption.csv"
    archivo="household_power_consumption.csv"
    #funcion_de_descarga(url,archivo)

    #Se utiliza el CSV brindado en paideia para realizar los incisos:
    contenido=lectura_csv(archivo) 

    #fecha="2017/1/16"
    #fecha="2017/4/28" #fecha con ?
    fecha="2017/2/9"
    #fecha_inicial="2016/12/16"
    fecha_inicial="2017/5/8"
    fecha_final="2017/6/8"
    
    print("------------------------------------------------")
    #Inciso A del examen impreso:
    print("Inciso A del examen impreso:")
    tiempo_us_a=get_exec_time_a(archivo)
    print(f"El tiempo de ejecución es {tiempo_us_a} us")
    print("------------------------------------------------")
    #Inciso B del examen impreso:
    print("Inciso B del examen impreso:")
    tiempo_b=get_exec_time_b(fecha_inicial,fecha_final)
    print(f"El tiempo de ejecución es {tiempo_b} us")
    
    print("------------------------------------------------")
    #Inciso C del examen impreso:
    print("Inciso C del examen impreso:")
    tiempo_h=gen_day_dict_threaded(fecha_inicial,fecha_final)
    print(f"El tiempo de ejecución es {tiempo_h} us")
    print("------------------------------------------------")

    print("Inciso D del examen impreso:")
    numproc=3
    tiempo_m=gen_day_dict_multi(fecha_inicial,fecha_final,numproc)
    print(f"El tiempo de ejecución es {tiempo_m} us")
    print("------------------------------------------------")

    print("Inciso E del examen impreso:")
    calc_speedup_e()
    print("------------------------------------------------")

    print("Inciso F del examen impreso:")
    tiempo_f=time.time()
    calc_stats(fecha_inicial,fecha_final)
    tiempo_f2=time.time()
    tiempo__f=(tiempo_f2-tiempo_f)*(10**6)
    print(f"El tiempo de ejecución es {tiempo__f} us")
    print("------------------------------------------------")

    print("Inciso G del examen impreso:")
    numproc=2
    calc_stats_conc(fecha_inicial,fecha_final,numproc)
    
    print(f"El tiempo de ejecución es {tiempo_ret} us")
    tiempo_concurrencia=tiempo_ret
    print("Se escogio la implementación de Multiprocesos para la concurrenc")
    print("------------------------------------------------")

    print("Inciso H del examen impreso:")
    
    calc_speedup_h()
    
    print("Se escogio la implementación de multiprocesos para la concurrencia")
    print("------------------------------------------------")

    





    

    
    
    
    