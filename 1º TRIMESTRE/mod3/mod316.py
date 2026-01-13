# Muestra los números del 320 al 160, contando de 20 en 20 hacia atrás utilizando los tres
# bucles, al igual que el ejercicio anterior.

# Versión con bucle for
print("Versión con bucle for:")
for i in range(320, 159, -20):
    print(i)

# Versión con bucle while
print("\nVersión con bucle while:")
i = 320
while i >= 160:
    print(i)
    i -= 20