# Realiza un subprograma que intercambie el valor de dos variables enteras.

import os

def intercambio(a,b):
    c=0
    c=a
    a=b
    b=c
    print ("Ahora se ha intercambiado {} con {}".format(a,b))
    

# Programa principal

os.system ("cls")
n1 = int(input("Introduce un numero: "))
n2 = int(input("Introduce otro numero para intercambiarlo: "))

print(intercambio(n1,n2))