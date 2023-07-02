import time
import asyncio
import random

PRECIO_MINIMO = 20000  # El precio base al que se inicia la subasta
PRECIO_MAXIMO = 100000  # El precio máximo que cualquiera de los participantes está dispuesto a pagar (úsalo como tope en random.randint())
TIEMPO_SUBASTA = 60
flag = True

#esta función es muy importante porque en paralelo me está controlando el tiempo 
#que es de 60 segundos si es que ese tiempo se acaaba cambio la bandera flag a False

async def controlatiempo():
    global flag
    await asyncio.sleep(TIEMPO_SUBASTA)
    flag = False


async def oferta_participante(p):
    oferta = random.randint(PRECIO_MINIMO, PRECIO_MAXIMO)
    await asyncio.sleep(random.randint(1, 10))
    return p, oferta


async def reoferta(participante, monto_mayor):
    monto_actual = participante[1]
    if monto_actual <= monto_mayor:
        nuevo_minimo = monto_actual + 500
        nuevo_maximo = int(nuevo_minimo * 1.20)
        nueva_oferta = random.randint(nuevo_minimo, nuevo_maximo)
        await asyncio.sleep(random.randint(1, 10))
        return participante[0], nueva_oferta
    else:
        return participante


async def main(p):
    #acá se crea una tarea para que haga eso en paralelo mientras espera hago lo demás en el main
    #  
    asyncio.create_task(controlatiempo())
    #en esta parte se usa el gather para ejecutar una
    #función varias veces los resultados se guardan en res
    res = await asyncio.gather(*(oferta_participante(i) for i in p))
    #esta función ordena los elementos de un arreglo considerando
    #el elemto del arreglo de índice 1
    res.sort(key=lambda x: x[1])  # ordeno el arreglo considerando el segundo elemento
    max_oferta = res[-1][1]
    while flag:
        reoferta_participantes = await asyncio.gather(*(reoferta(i, max_oferta) for i in res))
        reoferta_participantes.sort(key=lambda x: x[1])  # ordeno el arreglo considerando el segundo elemento
        max_oferta = reoferta_participantes[-1][1]
        if res == reoferta_participantes:
            break
        res = reoferta_participantes
    return res


if __name__ == "__main__":
    p = ["a", "b", "c", "d", "e"]
    res = asyncio.run(main(p))
    res.sort(key=lambda x: x[1], reverse=True)
    ganador = res[0]
    print("Ganador:", ganador[0], "con una oferta de $", ganador[1])


"""import time
import asyncio
import random

PRECIO_MINIMO = 20000   #El precio base al que se inicia la subasta
PRECIO_MAXIMO = 100000  #El precio maximo que cualquiera de los participantes está dispuesto a pagar(úselo como tope en random.randint()
TIEMPO_SUBASTA=60
flag=True

async def controlatiempo():
	print("entré")
	global flag
	await asyncio.sleep(TIEMPO_SUBASTA)
	flag=False
	print("salí")

async def oferta_participante(p):
	oferta=random.randint(PRECIO_MINIMO, PRECIO_MAXIMO)
	inicio=time.perf_counter()
	await asyncio.sleep(random.randint(1,10))
	final=time.perf_counter()
	return p,oferta


async def reoferta(participante, monto_mayor):
    monto_actual = participante[1]
    if monto_actual <= monto_mayor:
        nuevo_minimo = monto_actual + 500
        nuevo_maximo = int(nuevo_minimo * 1.20)
        nueva_oferta = random.randint(nuevo_minimo, nuevo_maximo)
        await asyncio.sleep(random.randint(1, 10))
        return participante[0], nueva_oferta
    else:
        return participante
    
async def main(p):
	task_tiempo = asyncio.create_task(controlatiempo())
	res = await asyncio.gather(*(oferta_participante(i) for i in p))
	res.sort(key = lambda x: x[1])#ordeno el arreglo considerando el segundo elemento
	max_oferta=res[4][1]
	j=0
	while(flag):
		if(j==0):
			reoferta_p = await asyncio.gather(*(reoferta(i,max_oferta) for i in res))
			reoferta_p.sort(key = lambda x: x[1])#ordeno el arreglo considerando el segundo elemento
			max_oferta=reoferta_p[4][1]
			j=1
			continue
		reoferta_p = await asyncio.gather(*(reoferta(i,max_oferta) for i in reoferta))
		reoferta_p.sort(key = lambda x: x[1])#ordeno el arreglo considerando el segundo elemento
		max_oferta=reoferta_p[4][1]
	return reoferta
	


if __name__ == "__main__":
	mayor_valor=0
	j=0
	p=["a", "b", "c", "d", "e"]
	#para correr el main asyncio principal se utiliza asyncio.run(FUNCION)
	res = asyncio.run(main(p))
	print(res)



	#print(f"Ofertas finales: {p[0]}:{args[0][1]}, {p[1]}:{args[1][1]}, {p[2]}:{args[2][1]}, {p[3]}:{args[3][1]},{p[4]}:{args[4][1]},")
	#print(f"Ganador es participante {args_nuevo[4][0]}")
"""