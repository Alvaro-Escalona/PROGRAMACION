# Realiza un programa que pida una hora por teclado y que muestre luego buenos días,
# buenas tardes o buenas noches según la hora. Se utilizarán los tramos de 6 a 12, de 13 a 20 y de
# 21 a 5. respectivamente. Sólo se tienen en cuenta las horas, los minutos no se deben introducir por
# teclado.

hora=int(input("Introduce una hora del día (0-23): "))

if 6 <= hora <= 12:
    print("Buenos días")
elif 13 <= hora <= 20:
    print("Buenas tardes")
elif (21 <= hora <= 23) or (0 <= hora <= 5):
    print("Buenas noches")
else:
    print("Hora no válida")