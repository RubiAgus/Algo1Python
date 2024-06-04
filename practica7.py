
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

def analizar_fortaleza(password:str):
   
   return()

def bank_statment (lst:[(chr,int)]):
   for i in lst:
      if lst[i][1] == 'i':
        return()
   