#Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio. 
horas = float(input ("Escribe tus horas de trabajo: ")) 
precio = float(input ("Escribe el precio por hora de trabajo: "))
m = horas*precio
print ("El importe total del servicio realizado es: ", m , "euros")