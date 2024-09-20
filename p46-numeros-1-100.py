#imprime numeros de 1 al 100 usando for

import os; os.system("clear")

""" print  (list(range(1,10)))
print(list(range(1,10,2)))
print(list(range(1,10,3)))
print(list(range(10,0,-1))) """

n = int(input("Hasta donde?  "))
i = int(input("Incremento de: "))

for x in range(1,n+1, i):
    print(x, end=" ")