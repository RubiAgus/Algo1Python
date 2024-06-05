import array 

#para la función pertenece el loop while itera toda la lista.


def pertenece (x, list1):
    for i in list1:
      if i  == x:
         return(True)
    else: return(False)
   
   
      
# print(pertenece(1,[2,3,4,5,1,10,11]))


def divideATodos(x:int, list:[int]) -> bool: # type: ignore
    for i in list:
        if (i % x != 0):
           return(False)
    return True
    
        
# print(divideATodos (3,[3,99,0,1,11])) #False

def sumaTotal(lista:[int])->int: # type: ignore
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