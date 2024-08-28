#Volúmen de un cilindro

import math as mt

print("Ingresa las dimensiones del cilindro en centímetros\n")

radio =  int(input(" radio :"))
altura = int(input(" altura :"))

volum =  mt.pi*(radio**2)*altura

print(f"El volúmen del cilindro es: {volum} cm^3")