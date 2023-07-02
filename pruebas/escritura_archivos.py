num="Hola amigos"
#w para escribir 
with open("oferta_del.txt", "w") as file:
    file.write(num)

#r para lectura
archivo=open("oferta_del.txt")
lista=archivo.read()

print(lista[0])