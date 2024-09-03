# Calcular la segunda ley de newton

import os; os.system("clear")

print("calcular la segunda ley de newton (f = m* a)")
print("[F] fuerza    f = m* a ")
print("[M]  masa     m = f/a")
print("[A] aceleracion a = f/m")
op= input("Elije:  ").upper()

if op=="F":
    print("\Calculando la fuerza...")
    m = float(input("Dame la masa      "))
    a = float(input("Dame la aceleracion "))
    f = m * a
    print(f"la fuerza es {f}")
elif op=="M":
    print("\nCalculando la masa ...")
    f = float(input("Dame la fuerza:  "))
    a = float(input("Dame la aceleracion: "))
    m = f / a
    print(f"La masa es {m}")
elif op=="A":
    print("\nCalculando la aceleracion... ")
    f = float(input("Dame la fuerza:  "))
    m = float(input("Dame la masa:  "))
    a = f / m
    print(f"La aceleracion es {a}")
else:
    print("\nOpcion invalida...")

print("\nProceso terminado...")