# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que 
# el usuario escriba “salir” que terminará.

def eco():
    palabra=""

    while palabra!="salir":
        palabra=input("Introduce una palabra (escribe 'salir' para terminar): ")
        if palabra!="salir":
            print(palabra)
        else:
            print("Has salido del programa.")

# PROGRAMA PRINCIPAL

print("Introduce salir para terminar el programa")
eco()