import math

P = int(input("Ingrese Precio de Suscripción Normal: "))
PU = int(input("Ingrese Precio de Suscripción Premium: "))
U = int(input("Ingrese Número de Usuarios Suscripción Normal: "))
UP = int(input("Ingrese Número de Usuarios Suscripción Premium: "))
GT = int(input("Ingrese Gastos Totales: "))

utilidades_Total= (P*U)+(PU*UP)-GT

print("La utilidad total es:  $ ", utilidades_Total) 