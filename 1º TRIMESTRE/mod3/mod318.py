# Realiza el control de acceso a una caja fuerte. La combinación será un número de 4 cifras.
# El programa nos pedirá la combinación para abrirla. Si no acertamos, se nos mostrará el
# mensaje “Lo siento, esa no es la combinación” y si acertamos se nos dirá “La caja fuerte se
# ha abierto satisfactoriamente”. Tendremos cuatro oportunidades para abrir la caja fuerte

combinacion_correcta = "1234"
intentos = 4

while intentos > 0:
    usuario = input("Introduce la combinación de 4 cifras: ")
    if usuario == combinacion_correcta:
        print("La caja fuerte se ha abierto satisfactoriamente.")
        intentos = 0
    else:
        intentos -= 1
        if intentos > 0:
            print("Lo siento, esa no es la combinación. Te quedan", intentos, "intentos.")
        else:
            print("Lo siento, esa no es la combinación. No te quedan más intentos.")