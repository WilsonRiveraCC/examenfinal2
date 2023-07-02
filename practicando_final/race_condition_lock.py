import time 
import concurrent.futures
import threading

class FakeDatabase:
    def __init__(self):
        self.value=0
        self._lock = threading.Lock()


    def update(self, name):  
        # acambio de esto se le puede colocar el 
        #self._lock.acquire()
        print(f"Thread {name} iniciando actualización")
        print(f"Thread {name} a punto de generar cambio")
        with self._lock:#genera un candado para cada hilo
            print(f"Thread {name} tiene el candado")
            local_copy = self.value
            local_copy +=1
            self.value = local_copy #actualizao el value que es el valor permanente en la base de datos
            time.sleep(0.1) 
            print(f"Thread {name} a punto de liberar el candado")
        print(f"Thread {name} liberó el candado")
        print(f"Thread {name} ha terminado la actualización")


if __name__ == "__main__":
    workers =50
    db=FakeDatabase()
    print(f"Valor inicial de la base de datos: {db.value}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        for index in range(workers):
            executor.submit(db.update, index)
    print(f"Valor final de la base de datos: {db.value}")
