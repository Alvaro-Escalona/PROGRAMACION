# El tiempo de cocción.
# Sabiendo que:
# ● Para cocinar 500 gramos de carne de vacuno, se necesita:
# ○ 10 minutos si quieres una cocción casi cruda
# ○ 17 minutos si quieres una cocción al punto
# ○ 25 minutos si quieres una cocción bien hecha.
# ● Para cocinar 400 gramos de carne de cordero se necesita:
# ○ 15 minutos si quieres una cocción casi cruda
# ○ 25 minutos si quieres una cocción al punto
# ○ 40 minutos si quieres una cocción bien hecha.
# ● El tiempo de cocción es proporcional al peso.
# Dependiendo de la información introducida por el usuario (tipo de carne, modo de cocción y
# peso), mostrar el tiempo de cocción de una carne en segundos.

carne=input("Introduce el tipo de carne (vacuno/cordevo): ").lower()
modo=input("Introduce el modo de cocción (casi cruda/al punto/bien hecha): ").lower()
peso=float(input("Introduce el peso de la carne en gramos: "))

if carne == "vacuno":
    if modo == "casi cruda":
        tiempo = (10 / 500) * peso
    elif modo == "al punto":
        tiempo = (17 / 500) * peso
    elif modo == "bien hecha":
        tiempo = (25 / 500) * peso
    else:
        tiempo = None

elif carne == "cordero":
    if modo == "casi cruda":
        tiempo = (15 / 400) * peso
    elif modo == "al punto":
        tiempo = (25 / 400) * peso
    elif modo == "bien hecha":
        tiempo = (40 / 400) * peso
    else:
        tiempo = None

else:
    tiempo = None

if tiempo is not None:
    print("El tiempo de cocción es de", tiempo * 60, "segundos.")