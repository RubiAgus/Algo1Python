# this practice is to start using imperative programing. 
import math 

#hola_mundo() python es secuencial, hola_mundo no está definido acá
def hola_mundo ():
 return   print ("hello world")
#I can call this function whenever I want in my code from now onwards

#I can even redefine it.
def hola_mundo():
    return print(3)


def imprimir_un_verso():
   print ("don't you like it bigger, better?\nBut you do what you can\nDont you like it a little better\nWhen you dont understand \nI was gonna save the planet, but today I got plans\nI guess this is just what I am")


def raiz2 ():
  calculo = math.sqrt (2)
  redondeo = round(calculo,4)
  print (redondeo)


def factorial_2():
   print(2*1)


def perimetro():
    longitud = 2 *  math.pi
    print(longitud)

#eso es todo el ejc 1.

#ejc 2, with parameters

def imprimir_saludo(name):
   print("\nHola "+ name +"!\n")
#imprimir_saludo(input("cual es tu nombre? \n"))  

def raizCuadrada(x):
   raizCuadrada = math.sqrt(x)
   print (raizCuadrada)

def ask_Float ():
    numero = float(input("dame un número: ") )
    return numero

def farenheit_to_celcius(temperature):
   conversion = (temperature-32)*(5/9)
   return print(conversion)

def esMultiploDe(x,y):
   if (x/y) == int (x/y):
        return True
   else:
      return False
#utilizar la funcion de arriba para determinar si un numero es par
def esPar (x):
    if esMultiploDe(x,2) == True:
       return (True)
    else: return(False)

def cantidad_dePizzas(guests,minPortions):
   totalPorciones = guests * minPortions
   pizzaCondecimal = float(totalPorciones/8)
   return (print(math.ceil(pizzaCondecimal)))
# cantidad_dePizzas(10,7)


def algunoEs0 (x,y):
   if (x == 0 or y == 0):
      return (True)
   else: return(False)
# print(algunoEs0(0,11))

def ambosSon0 (x,y):
   if(x==0 and y==0):
      return(True)
   else: return(False)
# print(ambosSon0(0,0))

def esNombreLargo(str):
   if (len(str) >= 3 or len(str) <=8):
      return(True)
   else: 
      return(False)
# print( esNombreLargo("cas") )


# esta es una función aux
def esEntero(x):
   if(x==int(x)):
      return(True)
   else: return(False)
print(esEntero(100/4))
def esBisiesto (año):
   if(esEntero(año/4)):
      return(True)
   else:return(False)