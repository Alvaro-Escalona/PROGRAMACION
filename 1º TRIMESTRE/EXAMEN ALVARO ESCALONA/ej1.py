import os

def menu():
    print("Bienvenido a la pasteleria: ")
    print("¿De que sabor quiere la tarta?")
    print("1. Manzana = 18€")
    print("2. Fresa = 16€ ")
    print("3. Chocolate")
    print("4. Extras")
    print("0. Terminar pedido")

def chocolate():
    print("¿Que tipo de chocolate quieres?")
    print("1. Chocolate blanco = 15€")
    print("2. Chocolate negro = 14€")

def extras():
    print("1. ¿Quieres añadirle nata? +2,5€")
    print("2. ¿Quieres añadirle un nombre? +2,75")
    print("0. Terminar con el pedido")

#Programa principal

suma=0
option = -1

while option !=0:
    menu()

    
    option = int(input("Selecciona un tipo de pastel: "))
    
    match option:
        case 1: 
            print("Has seleccionado tarta de manzana")
            suma+= 18
            continue
        case 2:
            print("Has seleccionado tarta de fresa")
            suma+= 16
            continue
        case 3:
            chocolate()
            ing_option= int(input("Selecciona que tipo de chocolate: "))
            match ing_option:
                case 1:
                    print("Has seleccionado tarta de chocolate blanco")
                    suma+=15
                    continue
                case 2:
                    print("Has seleccionado tarta de chocolate negro")
                    suma+=14
                    continue
        case 4:
            extras()
            ex_option= int(input("Selecciona que tipo de extra quieres: "))
            match ex_option:
                case 1:
                    print("Has añadido nata")
                    suma+= 2.5
                    continue
                case 2:
                    print("Has añadido un nombre")
                    suma+=2.75
                    continue
                case 0:
                    print("Has terminado el pedido")
                    print(f"El la tarta que has seleccionado cuesta {suma} €")
        case 0:
            print("Has terminado el pedido")
            print(f"La tarta que has seleccionado cuesta {suma} €")
