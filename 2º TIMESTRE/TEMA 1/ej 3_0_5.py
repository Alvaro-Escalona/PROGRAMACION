# Diseña un programa que permita contar vocales en una frase.

try:
    frase = (str(input("Introduce una frase: ")))
except ValueError:
    print("Valor no valido")
else:
    contador= 0
    frase= frase.lower()
    vocal=["a","e","i","o","u"]
    for vocales in frase:
        if vocales in vocal:
            contador+=1
    print(contador)




