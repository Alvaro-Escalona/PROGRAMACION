#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y
# quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la 
# entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años 
# debe pagar 5€ y si es mayor de 18 años, 10€. 

import os

def  edad(edad):
    coste=0
    if edad < 0 or edad > 120:
        raise NameError("IMPOSIBLE. EDAD FUERA DE RANGO")
    elif edad < 4:
        coste=0
    elif edad >= 4 and edad <= 18:
        coste=5
    else:
        coste=10
    return coste

# Programa principal

os.system("cls")

try:
    edad_cliente = int(input("Introduce la edad del cliente: "))
    precio = edad(edad_cliente)
    print(f"El precio de la entrada es de {precio}€")
except ValueError:
    print("Por favor, introduce un número.")
except Exception as e:
    print(f"Ha ocurrido un error: {e}")
