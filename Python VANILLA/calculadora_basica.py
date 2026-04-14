# Crear una calculadora que pida dos numeros al usuario, una operacion y que devuelva el resultado

numero1 = int(input("Introduce numero 1:"))
numero2 = int(input("Introduce numero 2:"))

operaciones_posibles = ["+", "-", "*", "/"]

operacion = input("Introduce una operacion [+ - * /]: ")

while operacion not in operaciones_posibles:
    operacion = input("Introduce una operacion [+ - * /]: ")

if operacion == "/" and numero2 == 0:
    print("No se puede dividir por 0")
else:
    resultado = eval(f"{numero1} {operacion} {numero2}")
    print(f"{numero1} {operacion} {numero2} = {resultado}")