# Escribe un programa que calcule la media de un conjunto de números positivos introducidos
# por teclado. A priori, el programa no sabe cuántos números se introducirán. El usuario
# indicará que ha terminado de introducir los datos cuando meta un número negativo.

n=0
contador=0
suma=0

while n >= 0:
    n = int(input("Introduce un numero positivo (o un numero negativo para terminar): "))
    if n >= 0:
        suma += n
        contador += 1
    else:
        media = suma / contador 
        print(f"La media de los numeros introducidos es: {media}")
    