import time
import asyncio
import random

PRECIO_MINIMO = 20000   #El precio base al que se inicia la subasta
PRECIO_MAXIMO = 100000  #El precio maximo que cualquiera de los participantes está dispuesto a pagar(úselo como tope en random.randint()

async def oferta_participante(p):
	oferta=random.randint(PRECIO_MINIMO, PRECIO_MAXIMO)
	inicio=time.perf_counter()
	await asyncio.sleep(random.randint(1,10))
	final=time.perf_counter()
	print(f"El {p} se demora {final -inicio}")
	return oferta

async def main():
	res = await asyncio.gather(*(oferta_participante(i) for i in range(6)))
	return res



if __name__ == "__main__":
	p=["a", "b", "c", "d", "e"]
	mayor_valor=0
	j=0
	#para correr el main asyncio principal se utiliza asyncio.run(FUNCION)
	res = asyncio.run(main())
	args=list(zip(p, res))
	

	print(f"Ofertas finales: {p[0]}:{args[0][1]}, {p[1]}:{args[1][1]}, {p[2]}:{args[2][1]}, {p[3]}:{args[3][1]},{p[4]}:{args[4][1]},")



