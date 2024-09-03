# Muestra el tipo de angulo en base a su magnitud
# <90 agudo, =90 es recto y <180 obtuso, =180 llano, >180 y >360 concavo, =360 cerrado

import os; os.system("clear")

print("muestra el tipo de angulo en base a su magnitud \n")

angulo = int(input("dame un angulo:  "))

if angulo>=0 and angulo<=360:
    print(f"El angulo tiene {angulo} grados, entonces es:  ", end="")
    if angulo < 90:
        print("Agudo")
    elif angulo ==90:
        print("recto")
    elif angulo>90 and angulo <180:
        print("obtuso")
    elif angulo == 180:
        print("llano")
    elif angulo>180 and angulo<360:
        print("concavo")
    else:
        print("cerrado o completo")
else:
    print("\nEl angulo esta fuera de rango")