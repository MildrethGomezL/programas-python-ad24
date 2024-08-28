#Divide un numero entero de 3 ciifras en centenas, decenas, unidades

import os

os.system ("clear")

print("Divide un numero entero de 3 cifras en centenas, decenas, unidades \n")
n = int(input("Dame un numero entero de 3 cifras "))

c= n // 100
d= (n-(c*100))//10
u = (n-(c*100 + d *10))

print("El numero orginas es", n)
print("Centenas: ", c)
print("Decenas : ", d)
print("Unidades: ", u)

print("\n Tu numero de la suerte es: ", c+d+u)