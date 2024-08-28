# Convertir temperaturas de celcius a farenheit y viceversa

import os; os.system("clear")

print("convertir temperatura de celcius a franheit y viceversa\n")
print("[1]convertir farenheit a celcius")
print("[2]convertir celcius a farenheit")
op = int(input("Elige "))


if op == 1:
    print("Convirtiendo de farenheit a celcius")
    temp = float(input("Dame los grados farenheit: "))
    res = (temp - 32)* 5 / 9
    print(f"{temp} farenheit equivale a {res} celcius")
else:
    print("Convirtiendo de celcius a farenheit ")
    temp = float(input("Dame los grados celcius: "))
    res = (temp * 9/5 )+ 32
    print(f"{temp} celcius  equivale a {res} farenheit")