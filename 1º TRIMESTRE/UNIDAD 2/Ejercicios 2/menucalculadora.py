import os


# Menu de una calculadora
def suma (a, b):
    resultado = a + b
    return resultado

def resta (a, b):
    if a==b:
        return 0
    elif a<b:
        return b - a
    else:
        return a - b

def multiplicar (a, b):
    resultado = a * b
    return resultado

def dividir (a, b):
    if b != 0:
        resultado = a / b
        return resultado
    else:
        return "Error: División por cero"
    
def raiz_cuadrada (a):
    if a >= 0:
        resultado = a ** 0.5
        return resultado
    else:
        return "Error: Raíz cuadrada de un número negativo"
    
def factorial (a):
    if a < 0:
        return "Error: Factorial de un número negativo"
    elif a == 0 or a == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, a + 1):
            resultado *= i
        return resultado

def potencia (a,b):
    resultado = a ** b
    return resultado

def pintamenu():

    os.system('cls')
    print("Menu calculadora:")
    print("1. SUMAR")
    print("2. RESTAR")
    print("3. MULTIPLICAR")
    print("4. DIVIDIR")
    print("5. RAIZ CUADRADA")
    print("6. FACTORIAL")
    print("7. POTENCIA")
    print("8. INTRODUCIR NÚMEROS NUEVOS")
    print("0. SALIR")

# Programa principal
if __name__=="__main__":
    os.system('cls')
    print("Bienvenido a la calculadora")
    
    n1 = int(input("Introduce el primer número: "))
    n2 = int(input("Introduce el segundo número: "))    

    option = 1
    while option != 0:
    
        pintamenu()

        option = int(input("Elige una opción: "))

        match option:
            case 1: 
                print("La suma es: ", suma(n1, n2))
                os.system ('pause')
            case 2: 
                print("La resta es: ", resta(n1, n2))
                os.system ('pause')
            case 3: 
                print("La multiplicación es: ", multiplicar(n1, n2))
                os.system ('pause')
            case 4: 
                print("La división es: ", dividir(n1, n2))
                os.system ('pause')
            case 5: 
                print("La raíz cuadrada de ", n1, " es: ", raiz_cuadrada(n1))
                os.system ('pause')
            case 6: 
                print("El factorial de ", n1, " es: ", factorial(n1))
                os.system ('pause')
            case 7: 
                print("La potencia de ", n1, " elevado a ", n2, " es: ", potencia(n1, n2))
                os.system ('pause')
            case 8: 
                n1 = int(input("Introduce el primer número: "))
                n2 = int(input("Introduce el segundo número: "))
            case 0: 
                print("HASTA LUEGO")
            case _: 
                print("Opción no válida")
                os.system ('pause')