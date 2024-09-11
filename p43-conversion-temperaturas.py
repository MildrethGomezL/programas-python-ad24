# Calcula la temperatura 
while True:
    
    temp_inicial = int(input("Introduce la temperatura inicial en grados centígrados: "))
    temp_final = int(input("Introduce la temperatura final en grados centígrados: "))

    print("\nConversión de grados Centígrados a Fahrenheit:")

    for temp_c in range(temp_inicial, temp_final + 1):
       
        temp_f = (temp_c * 9/5) + 32
        print(f"{temp_c}°C = {temp_f:.2f}°F")

    repetir = input("\n¿Quieres repetir el proceso? (s/n): ")
    if repetir.lower() != 's':
        break

print("Programa finalizado.")