# Realiza la documentación del proyecto calculadora, donde se indicaba con un
# menú la opción de sumar, restar, multiplicar, dividir… a través de funciones.

def menu ():
    """
    Devuelve un menú de opciones aritméticas en forma de cadena.
    """
    return ("1. Sumar \n" \
    "2. Restar \n" \
    "3. Multiplicar \n" \
    "4. Dividir \n"
    "5. Potencia \n"
    "6. Raiz cuadrada \n"
    "0. SALIR")

def suma (a: float, b: float) -> float: 
    """
    Calcula la suma de dos números racionales.
    Parámetros
    ----------    
    a: float
    Primer número racional
    b: float
    Segundo número racional
    Retorna
    -------
    float
    La suma de "a" y "b".
    Ejemplos
    --------
    >>> suma(5, 4)
    9
    >>> suma(3, 20.6)
    23.6
    """
    return a + b

def resta (a: float, b: float) -> float:
    """
    Calcula la resta de dos números racionales.
    Parámetros
    ----------    
    a: float
    Primer número racional
    b: float
    Segundo número racional
    Retorna
    -------
    float
    La resta de "a" y "b".
    Ejemplos
    --------
    >>> resta(10.7, 4.2)
    6.5
    >>> resta(2, 5)
    -3
    """
    return a - b

def multiplicacion (a: float, b: float) -> float:
    """
    Calcula la multiplicación de dos números racionales.
    Parámetros
    ----------    
    a: float
    Primer número racional
    b: float
    Segundo número racional
    Retorna
    -------
    float
    La multiplicación de "a" y "b".
    Ejemplos
    --------
    >>> multiplicacion(2.8, 7.8)
    21.84
    >>> multiplicacion(3, 9)
    27
    """
    return a * b

def division (a: float, b: float) -> float:
    """
    Calcula la división de dos números racionales.
    Parámetros
    ----------    
    a: float
    Dividiendo, número
    b: float
    Divisor, número racional
    Retorna
    -------
    float
    La división de "a" y "b".
    Lanza
    -----
    ValueError
    Si el parámetro "b" es 0.
    Ejemplos
    --------
    >>> division(3.1, 2)
    1.55
    >>> division(6, 14)
    0.42857142857142855

    """
    if b == 0:
        return NameError ("EL DIVIDENDO NO PUEDE SER 0")
    else:
        return a / b
    
def potencia (a: float, b: float) -> float:
    """
    Calcula la potencia de dos números racionales.
    Parámetros
    ----------    
    a: float
    Base, número racional
    b: float
    Exponente, número racional
    Retorna
    -------
    float
    La potencia de "a" y "b".
    Ejemplos
    --------
    >>> potencia(9, 0.5)
    3
    >>> resta(2.5, 3)
    15.625
    """
    return a ** b

def raiz_cuadrada (a: float) -> float:
    """
    Calcula la raiz cuadrada de un número racionale.
    Parámetros
    ----------    
    a: float
    Primer número racional
    Retorna
    -------
    float
    La raiz cuadrada de "a".
    Lanza
    -----
    ValueError
    Si el parámetro "a" es negativo.
    Ejemplos
    --------
    >>> raiz_cuadrada(5.7)
    2.3874672772626644
    >>> raiz_cuadrada(4)
    2

    """
    if a < 0:
        return NameError ("LA RAIZ CUADRADA DE UN NÚMERO NEGATIVO NO EXISTE")
    return a ** 0.5

    
# -----PROGRAMA PRINCIPAL-----
# Variables
programa = True

try:
    num1 = float(input("Escriba el primer número: "))
    num2 = float(input("Escriba el segundo número: "))

    while programa == True:
        print (menu ())
        opcion = int(input("Elija una opción:"))
        print("---------------")
        match opcion:
            case 1: # Suma
                print (suma (num1, num2))
            case 2: # Resta
                print (resta (num1, num2))
            case 3: # Multiplicación
                print (multiplicacion (num1, num2))
            case 4: # División
                print (division (num1, num2))
            case 5: # Potencia
                print (potencia (num1, num2))
            case 6: # Raiz cuadrada
                print (raiz_cuadrada (num1))
            case 0:
                programa = False
            case _:
                raise NameError ("OPCIÓN NO VÁLIDA")
        print("---------------")

except ValueError:
    print("Debes introcucir un valor entero")
except Exception as e:
    print(f"Ha ocurrido algo mal: {e}")