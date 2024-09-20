# Imprime los números del 100 a n con for con k decrementos

print("Numeros del 100 ")
m = int(input("Hasta: "))
f = int(input("En decrementos: "))

for n in range(100,m-1,-f):
    print(n,end="\n")