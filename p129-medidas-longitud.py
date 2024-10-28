
def pulgadas_a_centimetros(pulgadas):
    return pulgadas * 2.54


def metros_a_pies(metros):
    return metros * 3.281

while True:
    print("\nConversor de Unidades")
    print("[1] Convertir pulgadas a centímetros")
    print("[2] Convertir metros a pies")
    print("[3] Salir")

    opcion = int(input("\nElige una opción [1-3]: "))

    if opcion == 1:
        pulgadas = float(input("Ingresa el número de pulgadas: "))
        cm = pulgadas_a_centimetros(pulgadas)
        print(f"\n{pulgadas} pulgadas son {cm:.2f} centímetros")
    elif opcion == 2:
        metros = float(input("Ingresa el número de metros: "))
        pies = metros_a_pies(metros)
        print(f"\n{metros} metros son {pies:.2f} pies")
    elif opcion == 3:
        print("Saliendo...")
        break
    else:
        print("Opción inválida. Solo numeros entre 1 y 3.")