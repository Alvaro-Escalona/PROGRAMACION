# Utilizando el ejercicio anterior, indica los divisores del número.

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

def divisor(a):
    divs = []
    for i in range(1, a + 1):
        if a % i == 0:
            divs.append(i)
    return divs

#  Programa principal
if __name__=="__main__":
    os.system("cls")

    n = int(input("Introduce un número entero: "))

    if primo(n):
        print(" ES PRIMO")
    else:
        print("NO ES PRIMO")
    
    print("Sus divisores son: ", divisor(n))

