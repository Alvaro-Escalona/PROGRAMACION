# Reemplazar palabras enteras dentro de una cadena.

frase=(str(input("Introduce una frase: ")))
palabra=input("Introduce la palabra para sustituir: ")
sustituto= input("Introduce la nueva palabra")
cambiar= frase.replace(palabra,sustituto)
print(cambiar)