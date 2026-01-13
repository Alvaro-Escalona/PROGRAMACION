# Escribir un programa que almacene la cadena de caracteres contraseña en una
# variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
# introducida por el usuario coincide con la guardada en la variable sin tener en cuenta
# mayúsculas y minúsculas.

import os

def comprobar_contraseña(contraseña, usuario):

    if contraseña.lower() == usuario.lower():
        return True
    else: 
        return False
    
# Programa principal

if __name__ == "__main__":

    os.system("cls")

    contraseña = "PApaconchocO"
    usuario = input("Introduce la contraseña: ")

    if comprobar_contraseña(contraseña, usuario):
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")