# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def pinta_10_veces(a):
    for i in range(10):
        print(a)
    
# Programa Principal

n = input("Escribe una palabra: ")
print(pinta_10_veces(n))