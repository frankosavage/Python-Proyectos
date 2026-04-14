# Crear una clase Calculadora 
# Con un método estático que sume dos números.

class Calculadora:
    @staticmethod
    def sumar(numero01, numero02):
        numero01 = numero01
        numero02 = numero02
        resultado = numero01 + numero02

        print(f"El resultado de {numero01} + {numero02} es {resultado}")

Calculadora.sumar(3, 3)
        