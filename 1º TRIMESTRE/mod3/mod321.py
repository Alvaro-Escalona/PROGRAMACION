# Escribe un programa que permita ir introduciendo una serie indeterminada de números
# mientras su suma no supere el valor 10000. Cuando esto último ocurra, se debe mostrar el
# total acumulado, el contador de los números introducidos y la media.

n=0
contador=0
suma=0

while suma < 10000:
    n = int(input("Introduce un numero positivo (o un numero negativo para terminar): "))
    if suma <= 10000 and n >= 0:
        suma += n
        contador += 1
    else:
        suma= suma
        contador= contador

media = suma / contador
print(f"Has introducido un total de {contador} numeros siendo la suma {suma} y la media {media}")