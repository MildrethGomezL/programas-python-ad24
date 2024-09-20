# Imprime los números desde 0 a n con for con k incrementos

print("Números del 0 a m con for")

m = int(input("Hasta donde quieres contar?: "))
f= int(input("En incrementos de: "))

for n in range(1,m+1,f):
    print(n,end="\n")