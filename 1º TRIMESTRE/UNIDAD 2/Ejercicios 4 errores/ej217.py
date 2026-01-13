# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes: 
# Renta                      Tipo impositivo
# Menos de 10000€               5%
# Entre 10000€ y 20000€         15%
# Entre 20000€ y 35000€         20%
# Entre 35000€ y 60000€         30%
# Más de 60000€                 45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el 
# tipo impositivo que le corresponde.

import os

def renta(a):
    if a < 0:
        raise NameError("IMPOSIBLE. RENTA NEGATIVA")
    elif a < 10000:
        return 5
    elif a >= 10000 and a < 20000:
        return 15
    elif a >= 20000 and a < 35000:
        return 20
    elif a >= 35000 and a < 60000:
        return 30
    else:
        return 45
    
# Programa principal

if __name__=="__main__":

    os.system("cls")

    try:
        anual = float(input("Introduce tu renta anual: "))
        tipo = renta(anual)
        print(f"Tu tipo impositivo es del {tipo}%")
    except ValueError:
        print("Por favor, introduce un número.")    
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")