# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

def tabla_multiplicar(a):
    for i in range (11):
        multiplicar = a*i
        print(f" {a} * {i} = {multiplicar}")

# PROGRAMA PRINCIPAL

n = int(input("Introduce un numero para ver su tabla de multiplicar: "))

tabla_multiplicar(n)