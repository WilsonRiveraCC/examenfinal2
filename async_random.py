import asyncio
import random


##OJO COMENTAR TODO ESTE ÇÓDIGO PARA TRATAR DE APLICARLO LAS IDEAS ES CUANDO BOTA VALORES Y CUANDO DIJO EL PROFESOR 
##QUE HASTA NO SE EJECUTE NO RETORNA NADA
c=(
    "\033[0m",
    "\033[36m",
    "\033[91m",
    "\033[35m",
)

#si threshold no está definido usa 6 para la línea de código de abajo
async def makerandom(idx: int, threshold: int =6) -> int:
    print(c[idx+1] + f"Iniciando markerandom ({idx})")
    i= random.randint(0,10)
    while i <= threshold:
        print(c[idx+1]+f"makerandom({idx}) == {i}, muy bajo, Reintentando...")
        await asyncio.sleep(random.randint(1,5))
        i=random.randint(0,10)
    print(c[idx+1] + f"---> Terminando: makerandom({idx}) == {i}" + c[0])

    return i


async def main():
    res = await asyncio.gather(*(makerandom(i, 10-i-1) for i in range(3)))
    return res

if __name__ == "__main__":
    # random.seed(1337)
    r1,r2,r3=asyncio.run(main())
    print()
    print(f"r1:{r1}, r2:{r2}, r3: {r3}")



