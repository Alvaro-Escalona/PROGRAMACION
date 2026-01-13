# Diseña un algoritmo en el que se solicite un número por teclado y nos diga si es múltiplo de
# 2, de 3, de ambos o de ninguno. Por ejemplo, 6 es múltiplo de 2 y de 3; 4 es múltiplo de 2, 9
# es múltiplo de 3 y 5 no es múltiplo de ninguno.

n=int(input("Introduce un numero: "))
if n % 2 == 0 and n % 3 == 0:
    print(n, "es multiplo de 2 y de 3")
elif n % 2 == 0:
    print(n, "es multiplo de 2")
elif n % 3 == 0:
    print(n, "es multiplo de 3")
else:
    print(n, "no es multiplo de 2 ni de 3")