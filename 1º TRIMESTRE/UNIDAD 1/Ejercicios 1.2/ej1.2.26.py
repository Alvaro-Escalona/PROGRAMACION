# Escribir un programa que pregunte por consola por los productos de una cesta de la
# compra, separados por comas, y muestre por pantalla cada uno de los productos en una
# línea distinta. 

compra = str(input("Introduce los productos de tu compra (separados por comas): "))
compra2 = compra.split (",")
n = len (compra2)
for i in range(n):
    print (compra2[i])
