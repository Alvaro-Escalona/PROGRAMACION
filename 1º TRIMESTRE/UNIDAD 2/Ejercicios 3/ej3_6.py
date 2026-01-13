# Convertir grados Celsius a Fahrenheit
import os

def celsius(a):
    
    resultado = (a*(9/5))+32
    return resultado

#Programa principal

os.system("cls")
n1= float(input("Introduce los grados celsius: "))

print(n1," grados Celsius son ",celsius(n1), "grados Fahrenheit")

