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
def esMultiploDe(x,y):
   if(x/y==int(x/y)):
      return(True)
   else: return(False)

def esBisiesto (año):
   if(esMultiploDe(año,400) or ((esMultiploDe (año,4)) and (esMultiploDe(año,100)== False)) ):
      return(True)
   else: return(False)
# print(esBisiesto(2020))

# Ejc 4 composition
def PesoPino (pinoLen: int):
   if (pinoLen > 300):
      excess_pinoLen = pinoLen - 300
   else: excess_pinoLen = 0
   weight = excess_pinoLen * 2 + pinoLen * 3
   return(weight)

# print(PesoPino(200))

def es_peso_util(weight:int):
   if ( weight >= 400 and weight <= 1000 ):
    return(True)
   else: 
      return(False)

# print(es_peso_util(562))

def sirve_pino(height : int):
   
   if(es_peso_util(PesoPino(height))==True):
      return (True)
   else: return(False)

# print (sirve_pino(300))

def return_double(x:int):
   if (x/2 == int(x/2)):
      return(x*2)
   else: return(x)

# print(return_double(800))

def return_nextEven(x):
   if (x % 2 == 0):
      return(x)
   else: 
      return(x+1)
# print(return_nextEven(13))
def vacations(gender :str,age :int):
   if(age < 18):
      return("Anda de vacaciones")
   elif(gender == "M"):
      if (age < 65):
         return("Te toca trabajar")
      else: return("Andá de vacaciones")
   else:
      if (age < 60):
         return("Te toca trabajar")
      else: return("Andá de vacaciones")
# print(vacations("F",60))

#ejc 6----- while loops
def diezNumeros():
   i =  0
   while i < 10:
      i = i +1
      print(i)

# diezNumeros()

def odd_numbers10to40():
   i = 10
   while i <= 40:
      
      print(i)
      i = i + 2
# odd_numbers10to40()

def rocket_launch():
   i = 10
   while (i > 0):
      print (i)
      i -= 1
   
   print("Standby for titanfall")
# rocket_launch()

def for_rocket_launch():
   for i in range(1,11):
      print(i)
   print("RAJA EL COHETE")

for_rocket_launch()