# Leer n nombres de ciudades en una lista hasta introducir 

import os; os.system("cls")

ciudades = []
ciudadesC = []


while True:
    city = input("Nombre de ciudad: ")
    if city !="$":
        ciudades.append(city)
        if city.upper().startswith("A") or city.upper().startswith("E") or city.upper().startswith("I") or city.upper().startswith("O") or city.upper().startswith("U"):
            ()
        else:
            ciudadesC.append(city)
    else:
        break

print("\nCuantas ciudades son                          :", len(ciudades))
print("Nombres de ciudades                           :", ciudades)
ciudades.sort()
print("Orden descendente                             :", ciudades)
print("Ciudades que inician con consonante           :", ciudadesC)
print("Numero de ciudades que inician con consonante :", len(ciudadesC))







