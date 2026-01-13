# El programa debe mostrar un menú con una lista de películas y una opción para salir. Si el
# usuario elige una de las películas, el programa mostrará una cita de esa película. Luego se
# debe mostrar nuevamente el menú para que el usuario elija otra película o decida salir.
# Ejemplo de ejecución:
# Elija una opción:
# 1. Una cita de Forrest Gump.
# 2. Una cita de James Bond.
# 3. Una cita de Star Wars.
# 4. Una cita de El Sexto Sentido.
# 5. Una cita de El Padrino
# 6. Salir de la aplicación.

import os

def mostrar_menu():
    os.system("cls")
    print("Elija una opción:")
    print("1. Una cita de Forrest Gump.")
    print("2. Una cita de James Bond.")
    print("3. Una cita de Star Wars.")
    print("4. Una cita de El Sexto Sentido.")
    print("5. Una cita de El Padrino.")
    print("6. Salir de la aplicación.")

# Programa principal

option = -1

while option != 6:
    mostrar_menu()

    try:
        option = int(input("Introduce el número de la opción deseada para ver una cita de esta pelicula: "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        input("Pulsa Enter para continuar...")
        continue

    match option:
        case 1:
           
            print("Forrest Gump: La vida es como una caja de bombones, nunca sabes lo que te va a tocar.")
            input("Pulsa Enter para continuar...")
        case 2:
          
            print("James Bond: Mi nombre es Bond, James Bond.")
            input("Pulsa Enter para continuar...")
        case 3:
            
            print("Star Wars: Que la fuerza te acompañe.")
            input("Pulsa Enter para continuar...")
        case 4:
         
            print("El Sexto Sentido: Veo gente muerta.")
            input("Pulsa Enter para continuar...")
        case 5:
           
            print("El Padrino: Le haré una oferta que no podrá rechazar.")
            input("Pulsa Enter para continuar...")
        case 6:
           
            print("Saliendo de la aplicación. ¡Hasta luego!")
       
        case _:
        
            print("Opción no válida. Por favor, elige una opción del 1 al 6.")
            input("Pulsa Enter para continuar...")
        