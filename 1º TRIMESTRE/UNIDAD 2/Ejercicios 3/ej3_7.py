#  Contar vocales, en una palabra

import os

def vocales(palabra):
    vocal = "aeiouáéíóú"
    contador = 0
    palabra = palabra.lower()
    for i in palabra:
        if i in vocal:
            contador += 1
    return contador

# Programa principal

os.system("cls")

n = str(input("Intoduce una palabra para saber el numero de vocales que tiene: "))

print ("La palabra seleccionada tiene", vocales(n))