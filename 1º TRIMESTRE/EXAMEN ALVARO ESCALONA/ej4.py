import os
def suma(a,b):
    
    """
    Calcula la suma de dos números racionales.
    Parámetros
    ----------    
    a: int
    Primer número racional
    b: int
    Segundo número racional
    Retorna
    -------
    int
    La suma de "a" y "b".
    Ejemplos
    --------
    >>> suma(5, 4)
    9
    >>> suma(3, 20)
    23
    """
    pass

def ecuacion(a,b,c):
    """
    Calcula la ecuacion de segundo grado de 3 numero racionales
    Parámetros
    -------
    a: int
    Coeficiente cuadrático
    b: int
    Coeficiente lineal
    c: int
    Término independiente.
    Retorna
    -------
    tuple
    Una tupla con las dos soluciones (x1, x2).
    Lanza
    -----
    ValueError
    Si "a" y "b" son 0.
    Si (b ** 2) - (4 * a * c) es un número negativo.
    Ejemplos
    --------
    >>> ecuacion_segundo_grado(1, -3, 2)
    (2.0, 1.0)
    >>> ecuacion_segundo_grado(1, -7, 12)
    (3.0, 4.0)
    """
    pass

def menu():
    print("Bienvenido al menu calculadora")
    print("1. Suma")
    print("2. Ecuacion")
    print("0. Salir")

#Programa principal

option = -1

while option!=0:
    menu()
    try:
        option= int(input("Seleccione una opcción: "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        input("Pulsa Enter para continuar...")
        continue

    match option:
        case 1:
            
            print("La suma es 16")

        case 2:
            print("La ecuacion de segundo grado sale x1=3 y x2=4")
            
        case 0:
            os.system("cls")
            print("HAS SALIDO DE LA CALCULADORA")
