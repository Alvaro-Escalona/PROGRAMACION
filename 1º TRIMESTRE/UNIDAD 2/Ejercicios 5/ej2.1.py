#Escribe un programa que lea repetidamente números hasta que el usuario 
# introduzca “fin”. Una vez se haya introducido “fin”, muestra por pantalla el total, la 
# cantidad de números y la media de esos números. Si el usuario introduce cualquier otra 
# cosa que no sea un número, (mas adelante veremos como detectar los fallos usando try 
# y except) 

def numero_final(a):
    total = 0
    cantidad = 0
    while a != "fin":
        try:
            numero = float(a)
            total += numero
            cantidad += 1
        except ValueError:
            print("Entrada no válida, por favor introduce un número o 'fin' para terminar.")
        a = input("Introduce un número (o 'fin' para terminar): ")
    if cantidad > 0:
        media = total / cantidad
        print(f"Total: {total}, Cantidad de números: {cantidad}, Media: {media}")
    else:
        print("No se introdujeron números.")

# Programa principal

n = input("Introduce un número (o 'fin' para terminar): ")
numero_final(n)