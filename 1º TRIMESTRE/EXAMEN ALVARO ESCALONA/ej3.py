#Zona de variables
par=0
impar=0
"""
Calcula cuantos numero pares e impares hay en un número
Parámetros
------
n: int
Numero racional
Retorna
int
Catidad de numeros pares e impares
------
Ejemplo
>>> 4577
1 numero par y 3 numeros pares
"""
try:
    n=int(input("Introduce un numero entero: "))
    n=str(n)
    for i in n:
        aux=int(i)
        if aux % 2 == 0:
             par += 1
        else:
            impar += 1
    print(f"Ha intodducido {par} digitos pares y {impar} digtos impares con un total de {par + impar} digitos.")
except ValueError:
    print("Por favor, introduce un número.")

"""
Primero coge el numero y luego lo transforma en cadena con str para poder leer cada digito de 1 en 1
hasta el  numero de digitos que tiene el numero, luego lo vuevo a transformar a número
para poder dividirlo entre 2 y poder sacar el resto, si el resto es 0 significa que es par y si es distito
de 0 entonces el digito es impar.
"""