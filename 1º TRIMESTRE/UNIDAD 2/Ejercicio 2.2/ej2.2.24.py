# Escribir un programa que solicite el ingreso de una cantidad indeterminada de números 
# mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números 
# primos ingresados.

from ej2210 import es_primo

numero=1
primos=0

while (numero!=0):
    numero=int(input("Introduce un número mayor que 1 (0 para finalizar): "))
    if numero==1:
        print("ERROR, el numero 1 no vale")
        numero=abs(numero)
        if es_primo(numero):
            primos += 1

print(f"Ha introducido {primos} números primos.")