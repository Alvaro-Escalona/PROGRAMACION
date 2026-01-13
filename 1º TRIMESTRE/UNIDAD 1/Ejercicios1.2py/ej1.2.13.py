# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los
# siguienteS: "la división de n entre m da un cociente c y un resto r", donde n y m son los
# números introducidos por el usuario, y c y r son el cociente y el resto de la división entera respectivamente. 

n1 = int(input("Introduce un numero para dividir: "))
n2 = int(input("Introduce un numero que divide: "))

cociente = n1//n2
resto = n1%n2

print ("El resultado del cociente de", n1 ,"y", n2 ,"es igual a", cociente, "y su resto es ", resto )