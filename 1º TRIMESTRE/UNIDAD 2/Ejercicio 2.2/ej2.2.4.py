# Escribir un programa que pida al usuario un número entero positivo y muestre por
# pantalla la cuenta atrás desde ese número hasta cero separados por comas.

def mostrar_cuenta_atras(a):
    lista=""
    if a>=0:
        for i  in range (a, -1, -1):
            lista += str(i) + ", "
        print (lista[:-2])
    else:
        raise NameError ("Imposible el numero tiene que ser positivo")
    
# PROGRAMA PRINCIPAL

n = int(input("Introduce un numero para ver una cuenta atras desde ese numero: "))
try:
    mostrar_cuenta_atras(n)
except Exception as e:
    print(e)
except ValueError:
    print("Por favor, introduce un número entero.")
