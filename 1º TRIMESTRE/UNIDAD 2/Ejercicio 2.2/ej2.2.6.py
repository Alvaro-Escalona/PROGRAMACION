# Escribir un programa que pida al usuario un número entero y muestre por pantalla un 
# triángulo rectángulo como el de más abajo, de altura el número introducido. 

import os

def triangulo(a):
    lista= ""
    for i in range(0, a+2, 1):
        i= "*"
        lista += i
        print (lista[:-2])

# PROGRAMA PRINCIPAL

n = int(input("Introduce la altura del triangulo: "))

triangulo(n)