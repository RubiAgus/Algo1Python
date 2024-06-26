import array 

#para la función pertenece el loop while itera toda la lista.


def pertenece (x, list1):
   resultado = False
   i = 0 
   while (i< len(list1) and not resultado):
      resultado = i  == x
      i += 1
   return resultado

def belongs (y, list2)-> bool:
   isTrue = False
   for elem in list2:
      if elem == y:
         isTrue = True
   return(isTrue)   


   
      
# print(pertenece(1,[2,3,4,5,1,10,11]))


def divideATodos(x:int, list:[int]) -> bool: # type: ignore
    for i in list:
        if (i % x != 0):
           return(False)
    return True
    
        
# print(divideATodos (3,[3,99,0,1,11])) #False

def sumaTotal(lista:list[int])->int: # type: ignore
   suma = 0
   for i in lista:
      suma += i
   return(suma)

# print (sumaTotal ([2,1,5]))

def ordenados (lst:[int]) -> bool: # type: ignore
    for i in range (len(lst)):
      if lst[i] >= lst[i+1]:
         return(False)
    return(True)

# print(ordenados([1, 2, 3, 6, 5]))

def unoMayorASiete (lst:[str])->bool: # type: ignore
    for i in lst:
      if len(i) >= 7:
        return(True)
    return(False)

# print(unoMayorASiete(["casa","pedo","pepepepepepo","memo"]))

def isPalindrome (word:str) -> bool: # type: ignore
    if word == "":
       return(True)
    for i in range (len(word)):
       if word[i] != word [-(i+1)]:
          return(False)
       return(True)
#USE pop() in this one and get rid of the [-i] as it's not
# print(isPalindrome("tacocat"))
# print(isPalindrome(""))
# print(isPalindrome("abbb"))
# print(isPalindrome("casa"))

#acá iría el caso fortaleza de un a contraseña pero lo haré mas tarde por que es divertido

def tieneMayuscula(password: str) -> bool:
   for i in password:
      if i.isupper():
         return(True)
   # return(False)
# print(tieneMayuscula("pito"))
def tieneMinuscula(password:str)->bool:
   for i in password:
      if i.islower():
         return(True)
   # return(False)

def tieneCHRespecial(password: str)-> bool:
   for i in password: 
      if not i.isalnum():
         return(True)
   return(False)
      
# print(tieneCHRespecial("aksljfagAKSLF!!HSAN"))

def tieneNumero(password: str)-> bool:
   for i in password:
      if i.isnumeric():
         return(True)
   # return()
# print(tieneNumero("asfjgd2w"))
def condicionesVerde (a): 
      if len(a)>8 and tieneNumero(a) and tieneCHRespecial(a) and tieneMayuscula(a)  and tieneMinuscula(a):
         return(True)
      else: return(False)

def analizar_fortaleza(password:str) -> str:
   if len(password) < 5:
      return("ROJO")
   elif condicionesVerde(password):

      return("VERDE")
   else:
      return("AMARILLO")
# print(analizar_fortaleza(input(("ingrese su contraseña: "))))
   
from typing import List, Tuple

def bank_statement(lista: List[Tuple[chr, int]]) -> int:
    saldo = 0
    for (transaction,amount) in lista:
        if transaction == 'I':
            saldo += amount
        elif transaction == 'R':
            saldo -= amount
    return saldo

# transactions = [('I', 100), ('R', 50), ('I', 200), ('R', 150)]
# print(bank_statement(transactions))  # 100
vowels = ['a','e','i', 'o', 'u']
def isvowel(ltr: str):
   for i in vowels:
      if ltr == i:
         return(True)
      else: return(False)

# print(isvowel("a"))

def alMenos3Vocales(frase:str):
   counter= 0
   for i in str.lower(frase):
      if isvowel(i):
         counter += 1
   
   if counter >= 3:
      return(True)
   else: return(False)
# print(alMenos3Vocales("cAAA"))

#parte 2

#Dada una lista de numeros, en las posiciones 2n+1 

def replaceOdd_with0 (lst:List [int])-> List [int]:
   #debo iterar cada 2 i empezando por el segundo
   for i in range(1,len(lst),2):
      lst[i] = 0
   return(lst)

listaNum = [2,3,11,5,6]
replaceOdd_with0(listaNum)
# print(listaNum)

def replaceODD_with0OUT(lst: List [int])-> List [int]:
   lista = []
   for i in range(len(lst)):
      if i % 2 == 0 and i != 0:
         lista.append(0)
      else:
         lista.append(lst[i])
   
   return(lista)

otraLista = [2,3,45,6,2,5,7,8,99]
# print(replaceODD_with0OUT(otraLista))
# print(otraLista)

#problema 3 ejc 2
def sinVocales(lst:str) -> str:
   newlst = []
   for i in lst:
      if not isvowel(i):
         newlst.append(i)
   return(newlst)

# print(sinVocales("casa"))

def da_vuelta_str(phrase: str)-> str :
   inverted_phrase=[]
   for (i) in range(1, len(phrase) + 1):
      inverted_phrase.append(phrase[-i]) 
   return(inverted_phrase)
# Faltaba agregar el 1, """" + 1 para que me tome el primer i como 1 en vez de 0 para invertir el primer char.
# print (da_vuelta_str("abcd"))

def eliminarRepetidos(frase:str)->str:
   fraseModificada = []
   for i in frase:
      if not pertenece(i,fraseModificada):
         fraseModificada.append(i)
   return(fraseModificada)
# print(eliminarRepetidos("camapada"))

# ejercicio 3
def promedio(lista: list [int])-> int:
   promedio = 0
   counter = 0
   for i in lista:
      promedio += i
      counter += 1
   return(promedio/counter)
   
print(promedio([3,2,4]))
   
def todasAprobadas(n: list [int]) -> bool:
   for i in n:
      if i < 4:
         return(False)
      return(True)


def aprobado(notas: list [int])-> int:
   if promedio(notas) >= 7 and todasAprobadas(notas):
      return(1)
   elif promedio(notas) < 7 and todasAprobadas(notas):
      return(2)
   else: return(3)

# ejercicio 4, utilizando input()
