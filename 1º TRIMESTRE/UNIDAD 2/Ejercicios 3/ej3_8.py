# Mostrar línea decorativa con guiones
import os

def guion(a):
    n = "-"*a
    return n

# Programa principal

os.system("cls")

n = int(input("Intoduce un valor: "))

print (guion(n))