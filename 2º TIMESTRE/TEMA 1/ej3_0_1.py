# Escribe un bucle while que comience con el último carácter en la cadena y haga un
# recorrido hacia atrás hasta el primer carácter en la cadena, imprimiendo cada letra en
# una línea independiente

frase=input("Introduce una frase: ")
frase= frase[::-1]

for i in frase:
    print(i)