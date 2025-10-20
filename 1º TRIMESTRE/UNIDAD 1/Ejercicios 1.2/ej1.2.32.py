#Calcular la serie de Fibonacci hasta un número dado 

n=int(input("Introduce un número para ver la serie de Fibonnacci hasta ese número: "))

# if n=

i = 0
j = 1
punta = i + j
print (i)
print (j)
print (punta)
while (punta<=n):
    i = j
    j = punta
    punta= i + j
    if punta<=n:
        print (punta)

