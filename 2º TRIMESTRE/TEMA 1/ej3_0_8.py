# Contar cuántas veces aparece una letra.

palabra = (input("Introduce una frase: "))
letra= (input("Introduce una letra para ver cuantas veces aparece: "))
contador= 0
for cuenta in palabra:
    if cuenta==letra:
        contador+=1
print(f"La letra {letra} aparece {contador} veces en la frase")