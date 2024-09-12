#Universidad Autonoma de Zacatecas
#Fecha: 11 de septiembre 2024
#Materia: Computación aplicada
#Programa: p45-primer-examen
#Mildreth Valeria Gomez Lumbreras



# Inscripción a un evento académico 
#  Universidad Patito

# tipo de usuario
usr_precios = {
    1: 100,  # Alumno
    2: 200,  # Trabajador
    3: 500   # Docente
}

# Precios 
pkt_precios = {
    1: 600,  # conferencias
    2: 800,  # eventos sociales
    3: 900   # kit de acceso
}

# Descuentos 
usr_desc = {
    1: 0.20,  # Alumno 20%
    2: 0.10,  # Trabajador 10%
    3: 0.05   # Docente 5%
}

#Inicializacion
ventas_totales = 0


while True:
    print("\n      - Universidad Patio SA de CV -")
    print("\n  Sistema de Inscripción Congreso de Sistemas ")
 # tipo de usuario
    usr_tipo = int(input("Tipo de usuario: [1] Alumno $100, [2] Trabajador $200, [3] Docente $500: "))

    while usr_tipo not in [1, 2, 3]:
        print("Opción no válida. Ingrese una opción válida.")
        usr_tipo = int(input("Tipo de usuario: [1] Alumno $100, [2] Trabajador $200, [3] Docente $500: "))

# Tiipo de paquete
    pkt_tipo = int(input("Tipo de paquete: [1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con kit de acceso $900: "))
    
    while pkt_tipo not in [1, 2, 3]:
        print("Opción no válida. Ingrese una opción válida.")
        pkt_tipo = int(input("Tipo de paquete: [1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con kit de acceso $900: "))

# Inscripciones
    cant = int(input("Cantidad de inscripciones: "))

    while cant <= 0:
        print("La cantidad debe ser mayor a 0.")
        cant = int(input("Cantidad de inscripciones: "))
    
# Calcular el subtotal
    subtotal = (usr_precios[usr_tipo] + pkt_precios[pkt_tipo]) * cant

# Descuento si el subtotal es mayor a 5000

    if subtotal > 5000:
        descuento = subtotal * usr_desc[usr_tipo]
        total = subtotal - descuento
    else:
        descuento = 0
        total = subtotal

# Cantidad fnal

    print("\n   Total de inscripción  ")
    print(f"Tipo de usuario:   {'Alumno' if usr_tipo == 1 else 'Trabajador' if usr_tipo == 2 else 'Docente'}")
    print(f"Paquete adquirido: {'Conferencias' if pkt_tipo == 1 else 'Eventos sociales' if pkt_tipo == 2 else 'Kit de acceso'}")
    print(f"Cantidad de insc:  {cant}")
    print(f"Subtotal:          ${subtotal:.2f}")
    if descuento > 0:
        print(f"Se aplico un descuento de: ${descuento:.2f}")
# Si no hubo descuento
    else: 
        print("Sin descuento.")

    print(f"Total a pagar:     ${total:.2f}")

# Total de ventas del día
    ventas_totales += total

# Otra inscripción
    continuar = input("\n¿Desea iingresar otra inscripción? (s/n): ").lower()
    if continuar != 's':
        break

# Total de ventas del día
print(f"\n    - Total de ventas del día: ${ventas_totales:.2f} -")
