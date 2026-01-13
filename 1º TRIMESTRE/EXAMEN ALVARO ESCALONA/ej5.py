encontrado = False
i = 0
j = 1
punta = i + j

try:
    numero = int(input("Introduce un numero para saber si esta en la sucesion de fibonacci: "))
except ValueError:
    print("Por favor, introduce un nmero.")
else:
    if numero>=50 and numero<=200:
        while not encontrado and punta <= numero:
            if (punta == numero):
                encontrado = True
            
            else:
                i = j
                j = punta
                punta = i+j
            
        if encontrado:
                print ("Este numero se encuentra en la sucesion de Fibonacci ")
        else: 
                print ("Este numero no se encuentra en la sucesion de Fibonacci ")
        
    i = 0
    j = 1
    punta = i + j
    print (i)
    print (j)
    print (punta)
    while (punta<=233):
        i = j
        j = punta
        punta= i + j
        if punta<=233:
            print (punta)