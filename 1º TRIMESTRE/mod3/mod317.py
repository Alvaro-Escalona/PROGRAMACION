# Muestra la tabla de multiplicar de un número introducido por teclado.

n=int(input("Introduce un numero para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)
    