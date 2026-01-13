# Crea un subprogama que indique si un número es primo o no lo es.

import os

def primo(numero): 

    i = 2
    encontrado = False
    if numero == 4:
        return False #("NO ES PRIMO")
    else:
        while (i<(numero/2)) and (not encontrado):
            if (numero%i==0):
                encontrado=True
            i=i+1

        if encontrado:
            return False #("NO ES PRIMO")
        else:
            return True  #("ES PRIMO") 

#  Programa principal
if __name__=="__main__":
    os.system("cls")

    n = int(input("Introduce un número entero: "))

    print(primo(n))

