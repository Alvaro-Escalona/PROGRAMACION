sumatotal = 0
contador = 0
numvalores = 1
par = 0
impar = 0
i = 0
while (numvalores<0):
    numvalores = int(input("Introduce un numero: "))

    for i in range (1,numvalores,1):
        valor=int(input("Dame un numero: "))
        if (valor%2==0):
                par +=1
        else:
                impar +=1
    sumatotal += valor

media= sumatotal / numvalores

print (int(f"La media es {media} y hay {par} numeros pares y {impar} numeros impares"))

        

