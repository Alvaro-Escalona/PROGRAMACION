# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y 
# muestre por pantalla el número de veces que aparece la letra en la frase.


frase=input("Introduce una frase: ")
letra=input("Introduce una letra: ")

contador=0
encontrado=False
i=0
while i < len(frase):
    if frase[i]==letra:
        contador += 1
        encontrado=True
    i+=1
if not encontrado:
    print(f"La letra {letra} no se encuentra en la frase.")

else:   
    print(f"La letra '{letra}' aparece {contador} veces en la frase.")