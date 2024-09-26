# Numero de renglones que el usuario desee:
n = int(input("Dame un número: "))

for i in range(1, n + 1):
    
    for j in range(i):
        print(i, end=" ")
   
    print()