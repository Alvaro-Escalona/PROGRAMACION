def ecuacion_segundo_grado (a: int, b: int, c: int) -> float:
    """
    Resuelve una ecuación de segundo grado del tipo ax^2 + bx + c = 0.
    Parámetros
    ----------
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
    if a == 0:
        if b == 0:
            raise NameError ("TIENE QUE TENER AL MENOS UNA VARIABLE CON UN VALOR DISTINTO A CERO")
        return -c / b
    elif b == 0:
        return (-c ** 0.5) / a, -(-c ** 0.5) / a
    elif c == 0:
        return 0, -b / a
    else:
        raiz = (b ** 2) - (4 * a * c)
        if raiz < 0:
            raise NameError ("NO EXISTE SOLUCIÓN")
        else:
            return (-b + (raiz ** 0.5)) / (2 * a), (-b - (raiz ** 0.5)) / (2 * a)
        
# -----PROGRAMA PRINCIPAL-----

try:
    # Variables
    num1 = int(input("Escriba el valor de _x^2: "))
    num2 = int(input("Escriba el valor de _x: "))
    num3 = int(input("Escriba el valor de _: "))

    print(ecuacion_segundo_grado(num1, num2, num3))

except ValueError:
    print("Debes introcucir un valor entero")
except Exception as e:
    print(f"Ha ocurrido algo mal: {e}")
