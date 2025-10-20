#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
# dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior
# para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

fecha=str(input("Introduce una fecha (separando dd/mm/aaaa): "))

fecha2= fecha.split("/")

dia = int (fecha2[0])
mes = int (fecha2[1])
año = int (fecha2[2])

if (dia>31):
    print ("Ese dia no es valido")
elif (mes>12):
    print ("Ese mes no es valido")
elif (año>2025):
    print ("Ese año no es valido")
else:
    print ("Naciste en el dia {}, del mes {}, del año {}".format(dia, mes, año))

