# Crear una clase Perro con atributos nombre
# Y un metodo que sea ladrar
# Crear 2 perros distintos

class Perro:
    def __init__ (self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print(f"{self.nombre} dice: !WOF WOF!")

perro1 = Perro("Ellie")
perro2 = Perro("Benito")
        
perro1.ladrar()
perro2.ladrar()
