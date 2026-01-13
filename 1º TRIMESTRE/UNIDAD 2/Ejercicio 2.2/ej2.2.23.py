# Crear un programa que permita al usuario ingresar títulos de libros por teclado, 
# finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese 
# un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una 
# línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) 
# aparecieron en total (en todos los títulos de libros que componen en esa línea). 
# Finalmente, informar cuántas líneas completas se ingresaron. 

print("Ingrese títulos de libros. Ingrese '*' para finalizar y '/' para terminar una línea.")

linea_actual = ""
lineas_completas = 0
entrada=""

while entrada!="*":
    entrada = input("Titulo: ")
    if entrada == "/":
        # para contar los dígitos
        total_digitos = 0
        for titulo in linea_actual:
            for caracter in titulo:
                if caracter in "0123456789":
                    total_digitos += 1
        print(f"Línea completa. Total de dígitos numéricos: {total_digitos}")
        lineas_completas += 1
        linea_actual = ""
    else:
        linea_actual = linea_actual + entrada

print(f"Se ingresaron {lineas_completas} líneas completas.")