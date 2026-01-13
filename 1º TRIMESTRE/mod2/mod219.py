# Escribe un programa que pida por teclado un día de la semana y que diga qué asignatura toca a
# primera hora ese día.

dia=input("Introduce una dia de la semana: ").lower()

if dia=="lunes":
    print("A primera hora toca Base de Datos")
elif dia=="martes":
    print("A primera hora toca Programación")
elif dia=="miércoles":
    print("A primera hora toca Digitalizacion")
elif dia=="jueves":
    print("A primera hora toca Sostenibilidad")
elif dia=="viernes":
    print("A primera hora toca Sistemas Informáticos")
