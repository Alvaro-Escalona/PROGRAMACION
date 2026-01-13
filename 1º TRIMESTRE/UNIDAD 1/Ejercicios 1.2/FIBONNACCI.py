
# dime si un numero pertenece a la secuencia fibonnaci
encontrado = False
n1 = 0
n2 = 1
punta = n1 + n2
numero = int(input("Introduce un numero para saber si esta en la sucesion de fibonacci: "))
while not encontrado and punta <= numero:
    if (punta == numero):
        encontrado = True
       
    else:
        n1 = n2
        n2 = punta
        punta = n1+n2
if encontrado:
    print ("Este numero se encuentra en la sucesion de Fibonacci ")
else: 
    print ("Este numero no se encuentra en la sucesion de Fibonacci ")
