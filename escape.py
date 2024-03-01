import math

r = float(input("Ingrese radio en kilometros: "))
g = float(input("Ingrese constante gravitacional G: "))


Ve = math.sqrt(2*g*(r*1000))

print(f'La velocidad de Escape es {Ve:.1f} [m/s]')