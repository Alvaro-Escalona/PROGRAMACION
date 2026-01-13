# Realiza un programa que diga si un número introducido por teclado es par y/o divisible entre 5.

n=int(input("Introduce un numero: "))
if n % 2 == 0:
    print(n, "es un numero par")
else:
    print(n, "es un numero impar")

if n % 5 == 0:
    print(n, "es divisible entre 5")
else:
    print(n, "no es divisible entre 5")
    