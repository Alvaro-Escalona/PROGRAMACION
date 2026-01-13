#Crear un programa que solicite el ingreso de números enteros positivos, hasta que el 
# usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares 
# tiene. Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en 
# total. 

par=0
impar=0

n=input("Introduce un número entero: ")
for i in n:
    aux=int(i)
    if aux % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"Ha intodducido {par} digitos pares y {impar} digtos impares con un total de {par + impar} digitos.")
