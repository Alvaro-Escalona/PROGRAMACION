#Escribir un programa que pida al usuario dos números y muestre por pantalla su
# división. Si el divisor es cero el programa debe mostrar un error. 

n1 = int(input("Introduce número 1: "))
n2 = int(input("Introduce número 2: "))

if n2<=0:
    print("No se puede dividir entre 0")
else:
    division = n1/n2
    print("El resulado de dividir {} y {} es {}".format (n1,n2,division))