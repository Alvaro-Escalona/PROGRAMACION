#Crear un programa que permita al usuario ingresar los montos de las compras de un 
# cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada 
# ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa 
# un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al 
# finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total 
# de $1000, se le debe aplicar un 10% de descuento. 

total=0
importe=-1
while importe != 0:
    importe=float(input("Introduce el importe del producto (0 para finalizar): "))
    if importe > 0:
        total += importe

if total>=1000:
    print(f"El total de la compra es {total} y se aplica un descuento del 10%: {total * 0.9}")
else:
    print(f"El total de la compra es {total} y no se aplica descuento.")