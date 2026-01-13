
def burbuja(n):
    for i in range (0, len(n) -1):
        for j in range (0, len (n) -1 - i):
            if n[j] > n [j + 1]:
            # Intercambio de numero si estan en el orden correcto
                n[j], n[j + 1] = n[j+ 1], n [j]

# Programa principal

numeros = [34, 12, 5, 66, 1, 89, 23]

print(numeros)
burbuja(numeros)
print(numeros)