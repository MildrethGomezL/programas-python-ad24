
import os; os.system("cls")

#  listas con los nombres
lista_A = ["Juan", "Maria", "Pedro", "Jose", "Rocio"]
lista_B = ["Pedro", "Juan", "Pablo", "Mateo", "Esther"]

# listas en conjuntos
conjunto_A = set(lista_A)
conjunto_B = set(lista_B)


print("Conjunto A:", conjunto_A)
print("Conjunto B:", conjunto_B)

# Unión
union_conjuntos = conjunto_A.union(conjunto_B)
print("Unión de los conjuntos (A U B):", union_conjuntos)


interseccion_conjuntos = conjunto_A.intersection(conjunto_B)
print("Intersección de los conjuntos (A ∩ B):", interseccion_conjuntos)

# Diferencia de los conjuntos (elementos en A pero no en B)
diferencia_conjuntos = conjunto_A.difference(conjunto_B)
print("Diferencia de los conjuntos (A - B):", diferencia_conjuntos)

# Diferencia simétrica de los conjuntos (elementos en A o en B, pero no en ambos)
diferencia_simetrica_conjuntos = conjunto_A.symmetric_difference(conjunto_B)
print("Diferencia simétrica de los conjuntos (A △ B):", diferencia_simetrica_conjuntos)


subconjunto_pablo_mateo = {"Pablo", "Mateo"}.issubset(conjunto_B)
print("¿{'Pablo', 'Mateo'} es subconjunto de B?", subconjunto_pablo_mateo)


superconjunto_reynaldo_angelica = conjunto_A.issuperset({"Reynaldo", "Angelica"})
print("¿A es superconjunto de {'Reynaldo', 'Angelica'}?", superconjunto_reynaldo_angelica)

# Verificar
esta_pedro_en_A = "Pedro" in conjunto_A
print("¿Pedro está en A?", esta_pedro_en_A)


no_esta_lilia_en_B = "Lilia" not in conjunto_B
print("¿Lilia no está en B?", no_esta_lilia_en_B)