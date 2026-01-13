#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el
# nombre.
#  El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N 
# y el grupo B por el resto. Escribir un programa
# que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le
# corresponde. 

Nombre = str(input("Introduce tu nombre: "))
Sexo = str(input("Introduce tu sexo con M o F: "))

Sexo = Sexo.upper()
inicial = Nombre[0]

if Sexo=="F" and inicial<"m":
    print("Perteneces al grupo A")
elif Sexo=="M" and inicial>"n" :
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")