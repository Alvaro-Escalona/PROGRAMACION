# Escribir un programa que pida al usuario dos números y muestre por pantalla su
# división. Si el divisor es cero el programa debe mostrar un error.

def dividir(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError("Imposible dividir entre cero")
    else:
        return n1 / n2

# Programa principal

if __name__ == "__main__":

    try:
        n1= int(input("Introduce un numero: "))
        n2= int(input("Introduce otro numero: "))
        
        resultado= dividir(n1, n2)
        
        
    # except ZeroDivisionError:
       # print("CUIDADO... DIVISION POR CERO")
    except ValueError:
        print("Por favor, introduce números enteros.")
    except Exception as e:
        print(f"Algo ha salido mal:{e}")
    else:
        print("El resultado de la division es:", resultado)
