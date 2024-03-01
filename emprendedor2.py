import math

P = int(input("Ingrese Precio de Suscripción Normal: "))
PU = int(input("Ingrese Precio de Suscripción Premium: "))
U = int(input("Número de Usuarios Suscripción Normal: "))
UP = int(input("Número de Usuarios Suscripción Premium: "))
GT = int(input("Gastos Totales: "))

utilidadesTotal= (P*U)+(PU*UP)-GT

print("La utilidad total es:  $ ", utilidadesTotal) 