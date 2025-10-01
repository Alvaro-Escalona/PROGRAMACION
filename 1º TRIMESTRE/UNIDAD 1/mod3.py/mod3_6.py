n=0
hay_negativos=False
for i in range (0,5):   #El numero 5 se cambiaria por un 100
    n= int(input("Introuce valor: "))
    if (n<=0):
        hay_negativos= True
if (hay_negativos):
    print("Existen numeros negativos, almenos uno")
else:
    print("Todos son positivos")

