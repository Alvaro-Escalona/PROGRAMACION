# Escribe un programa que solicite dos números por teclado y nos diga si son primos gemelos
# o no. Dos números primos son gemelos cuando son primos, y además están separados por
# dos unidades. Por ejemplo, 3 y 5, 11 y 13, etc.

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n1 = int(input("Introduce el primer numero: "))
n2 = int(input("Introduce el segundo numero: "))

if es_primo(n1) and es_primo(n2) and abs(n1 - n2) == 2:
    print(f"{n1} y {n2} son primos gemelos.")
else:
    print(f"{n1} y {n2} no son primos gemelos.")