# Crear una clase Persona con nombre y edad
# Y un metodo que diga "Hola, soy [nombre]"

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad}")
        
        
persona = Persona("Franko", 25)
persona.saludar()

