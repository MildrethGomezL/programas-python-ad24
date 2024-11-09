#Universidad Autonoma de Zacatecas
#Fecha: 09 de noviembre 2024
#Materia: Computación aplicada
#Programa: p140-tercer-examen-parcial
#Mildreth Valeria Gomez Lumbreras

# Div de una academia

class Deportista:
    
    def __init__(self, nombre, nacimiento, genero, beca):
        self.nombre = nombre
        self.nacimiento = nacimiento
        self.genero = genero
        self.beca = beca
        self.total = 1  # Total de deportistas

    
    def __str__(self):
        return f"Nombre: {self.nombre:<20} AñoNac: {self.nacimiento:>4}    Género: {self.genero:>6}    Beca: {self.beca:>5}"

class Division:
   
    def __init__(self, nombre, rango, cuota):
        self.nombre = nombre
        self.rango = rango
        self.cuota = cuota
        self.deportistas = list()


    def agregar_deportista(self, deportista):
        self.deportistas.append(deportista)

    # Total de deportistas
    def total_deportistas(self):
        return sum(deportista.total for deportista in self.deportistas)

    
    def contar_por_genero(self):
        hombres = sum(1 for deportista in self.deportistas if deportista.genero == "Hombre")
        mujeres = sum(1 for deportista in self.deportistas if deportista.genero == "Mujer")
        return hombres, mujeres

    
    def subtotal_division(self):
        return sum(self.cuota for deportista in self.deportistas if deportista.beca.lower() != "becado")

    def __str__(self):
        return f"{self.nombre} - {self.rango} - ({self.total_deportistas()})"

class Academia:
    
    def __init__(self, nombre, propietario, direccion):
        self.nombre = nombre
        self.propietario = propietario
        self.direccion = direccion
        self.divisiones = list()

    # Division
    def agregar_division(self, division):
        self.divisiones.append(division)

   
    def contar_total_genero(self):
        total_hombres = total_mujeres = 0
        for division in self.divisiones:
            hombres, mujeres = division.contar_por_genero()
            total_hombres += hombres
            total_mujeres += mujeres
        return total_hombres, total_mujeres

 
    def total_academia(self):
        return sum(division.subtotal_division() for division in self.divisiones)

   
    def __str__(self):
        return f"\nNombre: {self.nombre} \nPropietario: {self.propietario} \nDirección: {self.direccion}"

def main():
    import os; os.system("cls")

    # Inicializa la academia, divisiones y deportistas
    academia = Academia("Academia Santos Laguna", "Francisco Nava", "Aguanaval 123, Hidráulica")
    academia.agregar_division(Division("Junior A", "2006/2007/2008", 1250))
    academia.divisiones[0].agregar_deportista(Deportista("Alexander Lopez", 2006, "Hombre", "Sin Beca"))
    academia.divisiones[0].agregar_deportista(Deportista("Uriel Puga", 2007, "Hombre", "Becado"))
    academia.divisiones[0].agregar_deportista(Deportista("Alejandra Escalona", 2008, "Mujer", "Sin Beca"))

    academia.agregar_division(Division("Junior B", "2009/2010/2011", 850))
    academia.divisiones[1].agregar_deportista(Deportista("Armando Santana", 2009, "Hombre", "Sin Beca"))
    academia.divisiones[1].agregar_deportista(Deportista("Daniel Mijares", 2010, "Hombre", "Sin Beca"))
    academia.divisiones[1].agregar_deportista(Deportista("Antonio Hernandez", 2011, "Mujer", "Becado"))

    academia.agregar_division(Division("Pony A", "2012/2013/2014", 700))
    academia.divisiones[2].agregar_deportista(Deportista("Andrea Solis", 2012, "Mujer", "Becado"))
    academia.divisiones[2].agregar_deportista(Deportista("Marissa Hernandez", 2013, "Mujer", "Becado"))
    academia.divisiones[2].agregar_deportista(Deportista("Diana Soto", 2014, "Mujer", "Sin Beca"))
    
    total_hombres, total_mujeres = academia.contar_total_genero()

  
    print("REPORTE DEL CLUB DEPORTIVO\n", academia)
    print("\nDatos generales de las Divisiones")

    print("\nTotal de Divisiones  :", len(academia.divisiones))
    print("Total de Hombres     :", total_hombres)
    print("Total de Mujeres     :", total_mujeres)


    print("Nombre: Junior A      Rango: 2006/2007/2008      Cuota: $1,250.00")
    print("Nombre: Junior B      Rango: 2009/2010/2011      Cuota: $850.00")
    print("Nombre: Pony A        Rango: 2012/2013/2014      Cuota: $700.00")

    
    print("\nDeportistas por División:")
    for division in academia.divisiones:
        print(division)
        for deportista in division.deportistas:
            print(deportista)
        print(f"\nSubtotal: ${division.subtotal_division():,.2f}\n")

    print(f"\nTotal: ${academia.total_academia():,.2f}")

if __name__ == "__main__":
    main()
