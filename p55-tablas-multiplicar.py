# Imprime las tablas del 1 a tabla n, desde 1 hasta m


import os;

while True:
    os.system("clear")

    n = int(input("Hasta que tabla deseas imprimr: "))
    m = int(input("Hasta donde?: "))

    for i in range(1, n+1):
        print("Tabla del " + str(i) )
        for j in range(1, m+1):

         print(f"{i} x {j} = {i*j}")

    if input("\nContinuar (S/N)").lower().startswith('n'): break

print("\nPrceso terminado")