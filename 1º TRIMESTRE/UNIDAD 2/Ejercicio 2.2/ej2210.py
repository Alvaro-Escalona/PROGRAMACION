# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es 
# un número primo o no.

def es_primo(n):
    if n <= 1:
        #encontrado = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                encontrado = True
        encontrado = False

    if encontrado:
        return False
    else:
        return True    

# PROGRAMA PRINCIPAL

if __name__ == "__main__":

    numero = int(input("Introduce un número entero: "))
    if es_primo(numero):
        print(f"El número {numero} no es primo.")
    else:
        print(f"El número {numero}  es primo.")