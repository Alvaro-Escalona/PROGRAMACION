# Escribir un programa que pida al usuario un número entero positivo y muestre por
# pantalla todos los números impares desde 1 hasta ese número separados por comas.

def mostrar_numeros_impares(a):
    lista = ""
    if a >= 0:
        for i in range(1, a+1, 1):
            lista += str(i) + ", "
        print("Los numeros son: ", lista[:-2])
    else:
        raise NameError ("IMPOSIBLE EL NUMERO TIENE QUE SER POSITIVO")
    
# PROGRAMA PRINCIPAL

n = int(input("Introduce un numero entero positivo: "))
try:
    mostrar_numeros_impares(n)
except Exception as e:
    print(e)
except ValueError:
    print("Por favor, introduce un número entero.")