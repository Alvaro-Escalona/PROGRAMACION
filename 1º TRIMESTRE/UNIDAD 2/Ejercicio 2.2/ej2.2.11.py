# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a 
# una las letras de la palabra introducida empezando por la última.


frase=input("Introduce una frase: ")

i=len(frase)-1
while i >= 0:
    print(frase[i])
    i-=1

