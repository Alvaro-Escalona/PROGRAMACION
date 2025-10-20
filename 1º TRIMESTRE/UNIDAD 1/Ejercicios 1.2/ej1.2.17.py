#Escribir un programa que pregunte el nombre del usuario en la consola y un número
# entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como
# el número introducido.

nombre = str(input("Introduce tu nombre: "))
n = int(input("Inroduce un numero: "))
for i in range (n):
    print (nombre)