# Diseñe un algoritmo que lea un número de tres cifras y determine si es capicúa.

n=int(input("Introduce un numero de tres cifras: "))

cifra1=n//100
cifra2=(n//10)%10
cifra3=n%10

if cifra1==cifra3:
    print(n, "es un numero capicua")
else:
    print(n, "no es un numero capicua")