# Escribe un programa que dada una hora determinada (horas y minutos), calcule los
# segundos que faltan para llegar a la medianoche.

horas=int(input("Introduce las horas (0-23): "))
minutos=int(input("Introduce los minutos (0-59): "))

total_segundos_dia=24*60*60
segundos_transcurridos=horas*60*60 + minutos*60
segundos_restantes=total_segundos_dia - segundos_transcurridos 

print("Faltan", segundos_restantes, "segundos para llegar a la medianoche.")