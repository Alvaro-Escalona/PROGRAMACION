# Comprueba que una palabra dada está en una frase

frase=input("Introduce una frase: ")
palabra=input("Introduce una palabra: ")

encontrado= frase.endswith(palabra)

if encontrado == True:
    print(f"La palabra '{palabra}' se encuentra en la frase '{frase}'")
else:
    print(f"La palabra no se encuentra en la frase")