# Calcula la solución de una ecuación de segundo grado contemplando las
# diferentes condiciones de entrada que se puedan dar.

import os

def ecuacion(a,b,c):
    if a==0:
        if b==0:
            positivo = None
            negativo = None
        else:
            positivo = c
            negativo = positivo
    elif (b==0):
        if ((-c/a)**0.5)<0:
            positivo = None
            negativo = None
        else:
            positivo =  (-c/a)**0.5
            negativo = positivo
    else:    
        if ((b**2)-(4*a*c))<0:
            positivo = None
            negativo = None
        else:
            positivo = (-b + (((b**2)-(4*a*c)))**0.5)/(2*a)
            negativo = (-b - (((b**2)-(4*a*c)))**0.5)/(2*a)
        
        return positivo, negativo

# Programa principal

os.system ("cls")

n1 = int(input("Introduce el valor de a: "))
n2 = int(input("Introduce el valor de b: "))
n3 = int(input("Introduce el valor de c: "))

sol1,sol2=ecuacion(n1,n2,n3)

print ("La primera solucion de esta ecuacion de segundo grado es: ", sol1)
print ("La segunda solucion de esta ecuacion de segundo grado es: ", sol2)