import math

P = int(input("Ingrese Precio de Suscripción: "))
U = int(input("Ingrese Número de Usuarios: "))
GT = int(input("Ingrese Gastos Totales: "))

utilidades = (P*U)-GT

print("La utilidad es:  $ ", utilidades) 