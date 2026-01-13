# HAZ LA FACTORIZACION DE UN NUMERO
n=int(input("Introduce un numero: "))
factor=2
print("La factorizacion de",n,"es: ")
while n>1:
    while n%factor==0:
        print(factor)
        n=n//factor
    factor+=1

