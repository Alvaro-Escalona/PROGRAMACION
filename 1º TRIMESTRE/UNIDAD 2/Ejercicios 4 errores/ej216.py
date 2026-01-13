# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el
# nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los
# hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa
# que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le
# corresponde.

import os


# Programa principal

os.system("cls")


sexo = input("Introduce tu sexo (M/F/O): ")
nombre = input("Introduce tu nombre: ")

nombre=nombre.lower()
sexo=sexo.upper()

if sexo not in ["M","F","O"] or len(nombre)<1:
    print("Datos incorrectos")
else:
    if (sexo=="F" and nombre[0]<"m") or (sexo=="M" and nombre[0]>"n"):
        print("Grupo A")
    else:
        print("Grupo B")     
