#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un
# descuento del 60%. Escribir un programa que comience leyendo el número de barras
# vendidas que no son del día. Después el programa debe mostrar el precio habitual de una
# barra de pan (establecido en el programa como una constante), el descuento que se le hace
# por no ser fresca y el coste final total de todas las barras no frescas.
barra =  3.49
descuento = barra - (barra * 0.4) 
n = float(input("Introduce el número de barras de pan del dia anterior: "))
pan = n* (barra * 0.4)
print("El precio de la barra de pan es de {:.2f} pero al ser del dia anterior tiene un descuento del {:.2f} cada barra, lo que sale un total de {:.2f} euros" .format(barra,descuento,pan))