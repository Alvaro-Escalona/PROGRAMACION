#  Calcular el área de un rectángulo

import os

def area(a,b):
    return a*b

# Programa principal

os.system ("cls")

n1 = int(input("Introduce la base del rectangulo: "))
n2 = int(input("Introduce la altura del rectangulo: "))

print("El area del rectagulo de lado {} y {} es {}".format (n1,n2,area(n1,n2)))