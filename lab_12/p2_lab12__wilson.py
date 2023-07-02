import time
import random
from werkzeug.security import check_password_hash
from multiprocessing import Pool


"""
Esta es la contraseña que usted tiene que adivinar. Está encriptada para que no pueda saber cuál es la respuesta correcta a priori.
Lo que tiene que hacer es generar combinaciones de 3 letras y llamar a la función comparar_con_password_correcto(línea 24 de la plantilla)
"""
contrasena_correcta = 'pbkdf2:sha256:260000$rTY0haIFRzP8wDDk$57d9f180198cecb45120b772c1317b561f390d677f3f76e36e0d02ac269ad224'


# Arreglo con las letras del abecedario. Puede serle de ayuda, no es obligatorio que lo use
abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
vocales=['a', 'e', 'i', 'o', 'u']


def genera_contrasena():
	global abecedario
	global vocales
	contrasena=[]
	for j in range(3):
		if(j==2):
			contrasena.append(abecedario[(random.randint(0,len(abecedario)-1))])
		else:
			contrasena.append(vocales[(random.randint(0,4))])
			
	return contrasena
	
	
"""
Función que sirve para comparar su palabra(cadena de 3 caracteres) con la contraseña correcta.
Entrada: Su cadena de 3 caracteres
Salida: True(verdadero) si es que coincide con la contraseña correcta, caso contrario retorna False(falso)
"""
def comparar_con_password_correcto(palabra):
	return check_password_hash(contrasena_correcta, palabra)

def func_sync():
	global abecedario
	global vocales
	password=[]
	for i in vocales:
		password.append(i)
		for j in  vocales:
			password.append(j)
			for m in abecedario:
				password.append(m)
				contrasena_input=password[0]+password[1]+password[2]
				if(comparar_con_password_correcto(contrasena_input)):
					return contrasena_input
				else:
					password=password[:2]
			password=password[:1]
		password=[]

def func_paralelo(letra):
	global abecedario
	global vocales
	password=[]
	password.append(letra)
		
	for j in  vocales:
		password.append(j)
		for m in abecedario:
			password.append(m)
			contrasena_input=password[0]+password[1]+password[2]
			if(comparar_con_password_correcto(contrasena_input)):
				return contrasena_input
			else:
				password=password[:2]
		password=password[:1]
		




if __name__ == "__main__":
	#formar un str de 3 letras con multi procesos y luego llamar a la función comparar_con_password
	#si sale true es la contraseña y la imprimo
	argumento=vocales
	print(argumento)
	inicio=time.perf_counter()
	contrasena_ok=func_sync()
	print(contrasena_ok)
	final=time.perf_counter()
	print(f"Tiempo total de ejecucion sincrono: {final - inicio} segundos")


	num_procesos=5
	p = Pool(processes=num_procesos)
	inicio2=time.perf_counter()
	resultado = p.map(func_paralelo, argumento)
	p.close()
	p.join()
	print(resultado[2])
	final2=time.perf_counter()
	print(f"Tiempo total de ejecucion sincrono: {final2 - inicio2} segundos")





