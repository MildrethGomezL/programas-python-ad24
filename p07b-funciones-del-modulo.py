#Ejemplificar el uso de algunas funciones de la libreria math

import math as mt

w = 10.64
x = 10
y = 20
z = 35

print(f"Los numeros son: {x}, {y}, {z}")
print(f"Maximo comun divisor: {mt.gcd(x,y,z)}")
print(f"Valor Maximo        : {max(x,y,z)}")
print(f"Valor minimo        : {min(x,y,z)}")
print(f"Eleva a la potencia : {mt.pow(x,y)}")

print(f"Redondear hacia arriba: { mt.ceil(w)}")
print(f"Redondear haca abajo  : {mt.floor(w)}")
print(f"Redondear             : {round(w)}")
print(f"Truncar               : {mt.trunc(w)}")



