
import os; os.system("cls")

# Conjuntos
conjunto_A = {"Juan", "Maria", "Pedro", "Jose", "Rocio"}
conjunto_B = {"Pedro", "Juan", "Pablo", "Mateo", "Esther"}


print("Conjunto A:", conjunto_A)
print("Conjunto B:", conjunto_B)


union_conjuntos = conjunto_A | conjunto_B
print("Unión de los conjuntos (A U B):", union_conjuntos)


interseccion_conjuntos = conjunto_A & conjunto_B
print("Intersección de los conjuntos (A ∩ B):", interseccion_conjuntos)

# Diferencia 
diferencia_conjuntos = conjunto_A - conjunto_B
print("Diferencia de los conjuntos (A - B):", diferencia_conjuntos)


diferencia_simetrica_conjuntos = conjunto_A ^ conjunto_B
print("Diferencia simétrica de los conjuntos (A △ B):", diferencia_simetrica_conjuntos)

# subconjunto de otro
subconjunto_pablo_mateo = {"Pablo", "Mateo"}.issubset(conjunto_B)
print("¿{'Pablo', 'Mateo'} es subconjunto de B?", subconjunto_pablo_mateo)


superconjunto_reynaldo_angelica = conjunto_A.issuperset({"Reynaldo", "Angelica"})
print("¿A es superconjunto de {'Reynaldo', 'Angelica'}?", superconjunto_reynaldo_angelica)


esta_pedro_en_A = "Pedro" in conjunto_A
print("¿Pedro está en A?", esta_pedro_en_A)


no_esta_lilia_en_B = "Lilia" not in conjunto_B
print("¿Lilia no está en B?", no_esta_lilia_en_B)