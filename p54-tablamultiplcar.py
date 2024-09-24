#Imprimir tabla de multiplicar usndo ciclo for

import os;

while True:
    os.system("clear")

    t = int(input("Dame la tabla que deseas imprimr: "))
    n = int(input("Hasta donde?: "))

    for i in range(1, n+1,1):
        print(f"{t} x{i} = {t*i}")

    if input("\nContinuar (S/N)").lower().startswith('n'): break

print("\nPrceso terminado")