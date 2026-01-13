# Indicar si un número es par

def par (a):
    if (a%2==0):
        print("Este numero es par")
    else:
        print("Este numero es impar")
    
# Programa principal

n1 = int(input("Introduce un numero: "))

print (par(n1))