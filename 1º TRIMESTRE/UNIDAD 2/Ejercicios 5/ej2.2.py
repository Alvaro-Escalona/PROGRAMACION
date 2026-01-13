# Escribe otro programa que pida una lista de números como la anterior y al 
# final muestre por pantalla el máximo y mínimo de los números, en vez de la media.

def numero_final(a):
    total = 0
    cantidad = 0
    numeros = []
    while a != "fin":
        try:
            numero = float(a)
            numeros.append(numero)
            total += numero
            cantidad += 1
        except ValueError:
            print("Entrada no válida, por favor introduce un número o 'fin' para terminar.")
        a = input("Introduce un número (o 'fin' para terminar): ")
    if cantidad > 0:
        maximo = max(numeros)
        minimo = min(numeros)
        print(f"Total: {total}, Cantidad de números: {cantidad}, Máximo: {maximo}, Mínimo: {minimo}")
    else:
        print("No se introdujeron números.")

# Programa principal

n = input("Introduce un número (o 'fin' para terminar): ")
numero_final(n)