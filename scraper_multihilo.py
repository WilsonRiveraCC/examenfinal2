import concurrent.futures
import requests
import threading
import time

#se puede usar threading o concurrent.futures

#Variable global para cada thread de manera individual
thread_local= threading.local()

def get_session():
#sino existe ese atributo voy a emplearlo   
    if not hasattr(thread_local, 'session'):
        #creo la sesión
        #si ya fue creado lo creo y sino lo retorno
        thread_local.session = requests.Session()
    return thread_local.session


def get_site(url):
    session = get_session()
    #es una operación de entrada y salida
    #hay impacto positivo porque mientrs espera salta al otro
    #y el tiempo mejora
    with session.get(url) as response:
        print(f"Lei {len(response.content)} bytes de {url}")

def get_all(sites):
    #paso todos los sites
    #max workers significa que van a haber 5 hilos en cada momento
    #map mapear va una llamada de get_site a cada url que está pasando
    #de toda forma que va a generar un hilo por cada site que se genere
    #pool es de 5
    #si aumento los trabajadores el tiempo debería ser menor
    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        executor.map(get_site, sites)

if __name__ == "__main__":
    sites =[
        "https://www.jython.org",
        "http://olympus.realpython.org/dice"
    ]*80

    inicio= time.perf_counter()
    get_all(sites)
    fin= time.perf_counter()

    print(f"Descarga completa en {fin-inicio} segundos")
