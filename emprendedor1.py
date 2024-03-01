import math

P = int(input("Ingrese Precio de Suscripción: "))
U = int(input("Número de Usuarios: "))
GT = int(input("Gastos Totales: "))

utilidades = (P*U)-GT

print("La utilidad es:  $ ", utilidades) 