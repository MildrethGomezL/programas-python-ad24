#Universidad Autonoma de Zacatecas
#Fecha: 17 de octubre 2024
#Materia: Computación aplicada
#Programa: p100-segundo-examen-parcial
#Mildreth Valeria Gomez Lumbreras

lista_empleados = []

print("Bienvenidos a Mueblería Muebles Mildreth")
print("Sistema de Gestión de Empleados")
print("Ingrese los datos de cada empleado (Escriba * para finalizar):")

# Recopilación de datos de los empleados
while True:
    nombre_empleado = input("Nombre del empleado: ")
    if nombre_empleado == "*":
        break

    edad_empleado = int(input("Edad: "))
    genero_empleado = input("Género (h/m): ").lower()
    salario_empleado = float(input("Salario: "))
    hobbies = input("Pasatiempos (separados por comas): ").split(", ")

    # Almacenamos la información en un diccionario y lo añadimos a la lista
    lista_empleados.append({
        "Nombre": nombre_empleado,
        "Edad": edad_empleado,
        "Género": genero_empleado,
        "Pasatiempos": hobbies,
        "Salario": salario_empleado
    })

# Mostrar los datos ingresados en la lista de empleados
print("\nDatos registrados de los empleados:")
for emp in lista_empleados:
    print(emp)

# Formatear la información en una tabla
print("\nTabla de Empleados:")
print(f"{'Nombre':<12} {'Edad':<5} {'Género':<7} {'Salario':<10} {'Pasatiempos'}")
for emp in lista_empleados:
    nombre = emp['Nombre']
    edad = emp['Edad']
    genero = emp['Género']
    salario = emp['Salario']
    pasatiempos = ', '.join(emp['Pasatiempos'])
    print(f"{nombre:<12} {edad:<5} {genero:<7} {salario:<10.2f} {pasatiempos}")

# Resumen de los datos capturados
num_empleados = len(lista_empleados)
num_hombres = sum(1 for e in lista_empleados if e['Género'] == 'h')
num_mujeres = sum(1 for e in lista_empleados if e['Género'] == 'm')

# Contar la frecuencia de cada pasatiempo
conteo_pasatiempos = {}
for emp in lista_empleados:
    for pasatiempo in emp['Pasatiempos']:
        conteo_pasatiempos[pasatiempo] = conteo_pasatiempos.get(pasatiempo, 0) + 1

# Cálculos de edad y salario
total_edades = sum(emp['Edad'] for emp in lista_empleados)
promedio_edad = total_edades / num_empleados if num_empleados > 0 else 0

total_salarios = sum(emp['Salario'] for emp in lista_empleados)
promedio_salario = total_salarios / num_empleados if num_empleados > 0 else 0

# Identificar el empleado más joven y el de mayor edad
empleado_mayor = max(lista_empleados, key=lambda e: e['Edad'])
empleado_menor = min(lista_empleados, key=lambda e: e['Edad'])

# Mostrar el resumen
print("\nResumen:")
print(f"Total de empleados: {num_empleados}")
print(f"Hombres: {num_hombres}")
print(f"Mujeres: {num_mujeres}")
print("Pasatiempos y su frecuencia:", ', '.join(f"{p}/{c}" for p, c in conteo_pasatiempos.items()))
print(f"Suma de edades: {total_edades}, Promedio de edades: {promedio_edad:.1f}")
print(f"Suma de salarios: {total_salarios:.2f}, Promedio de salarios: {promedio_salario:.2f}")
print(f"Empleado de mayor edad: {empleado_mayor['Nombre']} ({empleado_mayor['Edad']} años)")
print(f"Empleado de menor edad: {empleado_menor['Nombre']} ({empleado_menor['Edad']} años)")