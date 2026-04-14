import random
from colorama import Fore


def jugar():
    
    print("\nElegi la dificultad:")
    print("1. Normal")
    print("2. Loco")
    print("3. Adivino")
    
    nivel = input("Selecciona una opcion: ")

    if nivel == "1":
        max = 10
    elif nivel == "2":
        max = 50
    elif nivel == "3":
        max = 100
    else:
        print("Error esa dificultad no existe")
        max = 10

    min = 1
    numero_rnd = random.randint(min, max)
    intentos = 0


    while True:
        intentos += 1
        intento = int(input(Fore.BLUE + "Introduce un numero: "))


        if intento > numero_rnd:
            print(Fore.RED + "Fallaste, el correcto es menor que " + str (intento))



        elif intento < numero_rnd:
            print(Fore.RED + "Te quedaste corto, el numero es mas grande que " + str (intento))



        else:
            break

        
    print(Fore.GREEN + "Felicidades Acertaste el numero era el " + str (numero_rnd))
    print(f"Te costo {intentos} intentos")
    
def menu():
    while True:
        print(Fore.BLUE + "\n --- Adivina el numero ---") 
        print(Fore.BLACK + "1. JUGAR")
        print(Fore.BLACK + "2. SALIR")       
    
        opcion = input(Fore.CYAN + "Selecciona una opcion: ")

        if opcion == "1":
            jugar()
        elif opcion == "2":
            print(Fore.GREEN + "Saliendo...")
            break
        else:
            print(Fore.RED + "Opcion invalida")

if __name__ == "__main__":
    menu()