# Escribir un programa que pida al usuario un número entero y muestre por pantalla un 
# triángulo rectángulo como el de más abajo. 


def mostrar_numeros_impares(a):
    if a >= 0:
        for i in range(1, a+1):
            linea = " "
            for j in range(2*i-1, 0 ,-2):
                linea= linea + " " + str(j)
            print (linea)
    else:
        raise NameError ("IMPOSIBLE EL NUMERO TIENE QUE SER POSITIVO")
    
# PROGRAMA PRINCIPAL

n = int(input("Introduce un numero entero positivo: "))
try:
    mostrar_numeros_impares(n)
except Exception as e:
    print(e)
except ValueError:
    print("Por favor, introduce un número entero.")