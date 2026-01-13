# Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar 
# la sumatoria de todos los números ingresados. 

def suma_numeros(a):
    suma=0
    
    while a != 0:
        suma += a
        a=int(input("Introduce un número entero (0 para terminar): "))
    print("La sumatoria de los números ingresados es:", suma)

# PROGRAMA PRINCIPAL

n=int(input("Inroduce los numeros que quieras sumar (0 para terminar): "))
suma_numeros(n)