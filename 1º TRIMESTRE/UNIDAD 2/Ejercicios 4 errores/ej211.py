# Escribir un programa que pregunte al usuario su edad
#  y muestre por pantalla si es mayor de edad o no

def eresMayorEdad(valor):

    if valor < 0 or valor > 120:
        raise NameError("IMPOSIBLE. EDAD FUERA DE RANGO")
    if valor >= 18:
        return True
    else:
        return False

#Programa principal

try:
    edad= int(input("Introduce tu edad: "))
    if eresMayorEdad(edad):
        print("Eres mayor de edad. Puedes pasar a la discoteca")
    else:
        print("Toma zumito de piña...")
except ValueError:
    print("Por favor, introduce un número entero.")
except Exception as ex:
    print(f"ha ocurrido algo malo: {ex}")