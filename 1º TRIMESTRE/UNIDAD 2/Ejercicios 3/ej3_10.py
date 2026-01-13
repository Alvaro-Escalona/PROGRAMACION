# Evaluar si una edad permite votar

import os

def edad(a):
    if a>=18:
        print ("Esta persona si puede votar")
    else:
        print ("Esta persona no puede votar")

# Programa principal

os.system("cls")

n = int(input("Introduce tu edad para saber si puedes votar: "))

print(edad(n))