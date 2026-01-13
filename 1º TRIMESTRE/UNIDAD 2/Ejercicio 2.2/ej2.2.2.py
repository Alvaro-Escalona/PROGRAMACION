# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los
# años que ha cumplido (desde 1 hasta su edad).

def mostrar_años_cumplidos(edad):
    for i in range(1, edad + 1):
        print(f"Has cumplido {i} años.")

# Programa Principal

edad_usuario = int(input("¿Cuántos años tienes? "))
mostrar_años_cumplidos(edad_usuario)