# Crear una clase Auto con el atributo marca
# Y un metodo que muestre la marca.

class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def exhibir(self):
        print(f"Este es mi auto a la venta, un {self.modelo} de {self.marca}")

auto = Auto("Volkswagen", "Gol Power")
auto.exhibir()