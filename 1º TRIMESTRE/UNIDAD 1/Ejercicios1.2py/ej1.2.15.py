# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés
# al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden
# al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la
# cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después
# el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer,
# segundo y tercer años. Redondear cada cantidad a dos decimales. 

dinero = float(input("Introduce la cantidad de saldo  que quieres ahorrar: "))
i = 1.04

año1 = dinero * i
año2 = año1 * i
año3 = año2 * i

print("En el primer año has ahorrado {:.2f}euros." .format(año1))
print("En el segundo año has ahorrado {:.2f}euros." .format(año2))
print("En el tercer año has ahorrado {:.2f}euros." .format(año3))