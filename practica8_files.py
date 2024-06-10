import random
from queue import LifoQueue as Pila


#cada vez que utilizamos el texto de nuevo lo cerramos y luego abrimos

archivo = open("file.txt", "r")
content = archivo.readlines()
archivo.close
# print(content)

archivo = open("file.txt","r",encoding="utf-8")
def contar_Lineas(archivo)-> int:
    counter = 0
    for i in archivo.readlines(): #it didn't like when I called a variable of archivo.readlines
        counter += 1
    return(counter)
archivo.close
# print(contar_Lineas(archivo))


#nesecito pasar linea por linea
createFile = open("hello.txt","w")
createFile.write("hola como va? \n")



def existePalabra(palabra:str, archivo:str)-> bool:
        for linea in archivo.readlines():
             if (pertenece(palabra, linea)):
                  return(True)
        return(False)


# NO SE TOMA ARCHIVOS, tomarlo con pinzas 
# ojo con el tipado de variabes, se recomienda hacerlo pero no entra dentro del testing.
#LOOK UP PYTHON unittest and how to use the library. Rudimentariamente.

