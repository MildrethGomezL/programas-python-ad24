#verifica la suma de dos numeros es igual a un tercero
# 5 5 9 ?  4 9 5?  9 4 5?

import os; os.system("clear")
print("Verifica si la suma de dos numeros es igual a un tercer:\n " )
n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if n1 + n2 == n3:
    print(f"{n1} + {n2} = {n3}")
elif n1 + n3 == n2:
    print(f"{n1} + {n3} = {n2}")
elif n1 + n3 == n2:
    print(f"{n2} + {n3} = {n1}")
elif n1 == n2 == n3:
    print(f"{n1} = {n2} = {n3} son iguales " )
else:
    print(f"Los numeros son diferentes: {n1}, {n2}, {n3}")

print("\nProceso terminado... ")


