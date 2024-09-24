#Calcula el facotial de un numero usando for

import os; os.system("clear")

n = int(input("Dame un numero: "))


# print(f"{n}! =", end="")

for x in range(1,n+1):
    f = 1
    print(f"{x}! = ", end=" ")
    for i in range(1, x+1):
        f = f * i
        print(f"{i}{"x"if i!=x else ""}",end ="")
    print(f"={f}")