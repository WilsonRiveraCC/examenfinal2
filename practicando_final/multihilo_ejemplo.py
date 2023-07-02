
import concurrent.futures

def tarea(arg):
    # Simulación de una tarea que toma cierto tiempo
    resultado = arg[0] + arg[1] + arg[2]
    return resultado

if __name__ == '__main__':
    argumentos = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        # Aplicar la función tarea a los conjuntos de argumentos utilizando starmap
        resultados = executor.map(tarea, argumentos)

        # Imprimir los resultados
        for resultado in resultados:
            print(resultado)
