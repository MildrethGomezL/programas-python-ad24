#Calcula el factorial de un numero usando for

import os; os.system("clear")
# n = 5

n = int(input("Dame un numero: "))
f = 1
print(f"{n}! =", end="")

for i in range(1, n+1):
    f = f * i
    print(f"{i}{"x"if i!=n else ""}",end ="")

print(f"={f}")