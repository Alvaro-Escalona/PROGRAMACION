# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos
# ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al
# usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que
# tributar o no

import os

def tributar(edad, ingresos):

    if edad < 0 or edad > 120:
        raise NameError("IMPOSIBLE. EDAD FUERA DE RANGO")
    elif ingresos < 0:
        raise NameError("IMPOSIBLE. INGRESOS NEGATIVOS")
    elif edad > 16 and ingresos >= 1000:
        return True
    else:
        return False

# Programa principal

if __name__=="__main__":

    os.system("cls")

    try:
        edad = int(input("Introduce tu edad: "))
        ingresos= int(input("Introduce tus ingresos mensuales: "))
        if tributar(edad, ingresos):
            print("Tienes que tributar.")
        else:
            print("No tienes que tributar.")
    except ValueError:
        print("Por favor, introduce un número.")    
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
    
        
