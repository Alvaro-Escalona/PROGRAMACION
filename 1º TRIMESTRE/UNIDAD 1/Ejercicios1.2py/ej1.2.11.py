# Escribir un programa que lea un entero positivo, n, introducido por el usuario y después 
# muestre en pantalla la suma de todos los enteros desde 1 hasta n.
n = int(input("Intorduce un numero: "))
suma = (n*(n + 1))/2

print ("La suma de todos los numeros hasta", n, "es: ", suma)
