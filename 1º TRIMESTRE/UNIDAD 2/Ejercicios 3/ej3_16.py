#Realiza un subalgoritmo que permita a un usuario intentar 3 veces acertar el PIN 
# de acceso a un dispositivo.

def pin(a):
    intentos = 0
    while intentos < 3:
        entrada = input("Introduce el PIN de acceso: ")
        if entrada == a:
            return "Acceso concedido"
        else:
            intentos += 1
            print(f"PIN incorrecto. Te quedan {3 - intentos} intentos.")
    return "Acceso denegado"

# Programa principal

if __name__=="__main__":
    pin1 = "1234"  
    resultado = pin(pin1)
    print(resultado)
    