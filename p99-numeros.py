
import os; os.system("cls")

# conjuntos
conjunto_A = {50, 60, 70, 80, 90, 100, 200}
conjunto_B = {60, 90, 100, 300, 400, 500}
conjunto_C = {10, 20, 60, 90, 70, 100, 600, 700}


print("Conjunto A:", conjunto_A)
print("Conjunto B:", conjunto_B)
print("Conjunto C:", conjunto_C)

# Operaciones
union_A_B = conjunto_A | conjunto_B
print("Unión de A y B:", union_A_B)

union_B_C = conjunto_B | conjunto_C
print("Unión de B y C:", union_B_C)

diferencia_A_C = conjunto_A - conjunto_C
print("Diferencia de A y C:", diferencia_A_C)

diferencia_simetrica_B_C = conjunto_B ^ conjunto_C
print("Diferencia simétrica de B y C:", diferencia_simetrica_B_C)

interseccion_B_C = conjunto_B & conjunto_C
print("Intersección de B y C:", interseccion_B_C)


print("A es subconjunto de B:", conjunto_A.issubset(conjunto_B))
print("C es subconjunto de A:", conjunto_C.issubset(conjunto_A))
print("100 está en A:", 100 in conjunto_A)
print("60 está en A, B y C:", 60 in conjunto_A and 60 in conjunto_B and 60 in conjunto_C)
print("900 no está en C:", 900 not in conjunto_C)