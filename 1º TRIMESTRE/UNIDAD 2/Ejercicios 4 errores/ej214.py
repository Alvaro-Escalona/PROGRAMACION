#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es
# par o impar.

import os

def par(a):
    if a%2==0:
        return True
    else:
        return False
    
# Programa principal

if __name__=="__main__":

    os.system("cls")

    n = -1

    while n<0:
        try: 
            n= int(input("Introduce un numero: "))
        
        except ValueError:
            print("Por favor, introduce un número.")
        else:
            if par(n):
                print("El número es PAR")
            else:
                print("El número es IMPAR")