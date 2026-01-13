# Buscar la primera aparición de una letra.

try:
    frase=input("Introduce una frase: ")
    letra=input("Introduce la letra que quieres buscar: ")
except ValueError:
    print("Valor no valido")
else:
    frase=frase.lower()
    letra=letra.lower()
    encontrado=False
    i=0

    while i < len(frase) and not encontrado:
        if frase[i]==letra:
            encontrado=True
        else:
            i+=1
    if not encontrado:
        print(f"La letra {letra} no se encuentra en la frase.")

    else:   
        print(f"La letra '{letra}' aparece {i+1} en esta posicion en la frase.")



