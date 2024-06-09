import random
from queue import LifoQueue as Pila


#cada vez que utilizamos el texto de nuevo lo cerramos y luego abrimos

archivo = open("file.txt", "r")
content = archivo.readlines()
archivo.close

print(content)

archivo = open("file.txt","r")
def contar_Lineas(archivo)-> int:
    counter = 0
    for i in archivo.readlines(): #it didn't like when I called a variable of archivo.readlines
        counter += 1
    return(counter)

print(contar_Lineas(archivo))


#nesecito pasar linea por linea
def existePalabra(palabra:str, archivo:str)-> bool:
        for i in archivo.readlines():
             return()


# NO SE TOMA ARCHIVOS, tomarlo con pinzas 
# ojo con el tipado de variabes, se recomienda hacerlo pero no entra dentro del testing.
#LOOK UP PYTHON unittest and how to use the library. Rudimentariamente.

