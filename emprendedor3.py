import math

P = int(input("Ingrese Precio de Suscripción: "))
U = int(input("Ingrese Número de Usuarios: "))
GT = int(input("Ingrese Gastos Totales: "))
UA = int(input("Ingrese utilidades año anterior: "))

razón_utilidades = ((P*U)-GT) / UA

# print("La utilidad es:  $ ", razón_utilidades) 

print(f'La utilidad es:  $  {razón_utilidades:.2f}')