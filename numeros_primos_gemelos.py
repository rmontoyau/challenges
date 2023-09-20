'''  
Crea un programa que encuentre y muestre todos los pares de números primos gemelos en un rango concreto.
El programa recibirá el rango máximo como número entero positivo.
   - Un par de números primos se considera gemelo si la diferencia entre
    ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 
  - Ejemplo: Rango 14
    (3, 5), (5, 7), (11, 13)'''
import math 
def is_prime_number(n):
    if n <= 0:
      return False
    if (n == 1 or n == 2):
      return True
    sqrt = int(math.sqrt(n)) + 1
    for i in range(2, sqrt):
       if n % i == 0:
          return False       
    return True

def twin_prime(n):
    last_prime = 0
    twins = []
    for i in range(1,(n + 1)):
      if is_prime_number(i):
         if last_prime > 0  and (i - last_prime == 2):
            twins.append([last_prime, i])
         last_prime = i
    return twins

print(twin_prime(20))