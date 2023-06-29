import time 
from multiprocessing import Process
CUENTA = 10000000

def cuenta(n):
    while n>0:
        n-=1

#   caso ideal cuando se tiene que el número de procesos es 
# cpu_count()

if __name__ == '__main__':
    #ojo se debe de colocar el .start y join separados, ya que
    #sino no se iniciaría los otros procesos cuando el join va después del start
    #detendría la inicialización
    num_procesos=2
    lista_procesos=[]
    for i in range(num_procesos):
        p=Process(target=cuenta, args=(CUENTA/num_procesos,))
        lista_procesos.append(p)
    
    inicio = time.perf_counter()    
    for proceso in lista_procesos:
        proceso.start()
    for proceso in lista_procesos:
        proceso.join()

    fin = time.perf_counter()
    print(f"el tiempo de ejecución es de {fin -inicio}")




    #utilizo cuenta/2 ya que estoy usando dos procesos y es dividir esa cuenta en 2
    #por eso va entre 2
    #dividir la operación a la mitad
    #p1= Process(target=cuenta, args=(CUENTA/2,)) 
    #p2= Process(target=cuenta, args=(CUENTA/2,))
    #para usar 4 procesos
    """p3= Process(target=cuenta, args=(CUENTA/8, )) 
    p4= Process(target=cuenta, args=(CUENTA/8, ))
    p5= Process(target=cuenta, args=(CUENTA/8, )) 
    p6= Process(target=cuenta, args=(CUENTA/8, ))
    #para usar 4 procesos 
    p7= Process(target=cuenta, args=(CUENTA/8, )) 
    p8= Process(target=cuenta, args=(CUENTA/8, ))
"""
    #inicio = time.perf_counter()
    #p1.start()
    """"p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p1.join()  
    p2.join()
    p3.join()  
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()"""
    #fin = time.perf_counter()
    #print(f"el tiempo de ejecución es de {fin -inicio}")

