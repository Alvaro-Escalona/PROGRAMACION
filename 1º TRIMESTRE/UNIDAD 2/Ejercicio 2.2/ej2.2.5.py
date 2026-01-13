# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y
# el número de años, y muestre por pantalla el capital obtenido en la inversión cada año
# que dura la inversión.

import os

def capital(cantidad, interes, años):
    interes = 1+(interes/100)
    total = 0
    for i in range (1, años+1):
        total = cantidad * interes  
        return total

# PROGRAMA PRINCIPAL
os.system ("cls")

cantidad = int(input("Introduce una cantidad para invertir: "))
interes = int(input("Introduce el interes por año que se le va a aplicar: "))
años = int(input("Introduce el numero de años que quiere invertir: "))



for i in range (1, años+1):
    cantidad = capital(cantidad, interes, años)
    ganancia = capital(cantidad, interes, años) 
    print(f"Ha invertido {cantidad:.2f} € con un interes de {interes} % y ha conseguido {ganancia:.2f} en el año {i}.")    



