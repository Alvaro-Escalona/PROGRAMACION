# Cálculo de un número aleatorio entre dos valores 


import random

valor1=int(input("Introduce valor 1: "))
valor2=int(input("Introduce valor 2: "))

numeroAleatorio=random.randint(valor1,valor2)

print(numeroAleatorio)