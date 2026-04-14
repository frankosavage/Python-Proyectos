import random
from colorama import Fore, Style, init

init(autoreset=True)

movimientos = ["piedra", "papel", "tijera"]

while True:
    print(Fore.CYAN + "\n✊ ✋ ✌️")
    print("1. Jugar")
    print("2. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "2":
        print(Fore.YELLOW + "Saliendo del juego...")
        break

    elif opcion == "1":

        puntos_usuario = 0
        puntos_ia = 0

        while puntos_usuario < 3 and puntos_ia < 3:

            movimiento_pc = random.choice(movimientos)
            movimiento_usuario = input(Fore.WHITE + "Que vas a sacar (Piedra - Papel - Tijera): ")

            if movimiento_usuario.lower() not in movimientos:
                print(Fore.RED + "Eso no existe")
                continue
            
            print(Fore.BLUE + f"SACASTE {movimiento_usuario}. LA PC SACO {movimiento_pc}")

            if movimiento_usuario.lower() == "piedra":
                if movimiento_pc == "piedra":
                    print(Fore.YELLOW + "Empate")
                elif movimiento_pc == "papel":
                    print(Fore.RED + "Perdiste")
                    puntos_ia += 1
                elif movimiento_pc == "tijera":
                    print(Fore.GREEN + "Ganaste")
                    puntos_usuario += 1
                    
            if movimiento_usuario.lower() == "papel":
                if movimiento_pc == "piedra":
                    print(Fore.GREEN + "Ganaste")
                    puntos_usuario += 1
                elif movimiento_pc == "papel":
                    print(Fore.YELLOW + "Empate")
                elif movimiento_pc == "tijera":
                    print(Fore.RED + "Perdiste")
                    puntos_ia += 1
                    
            if movimiento_usuario.lower() == "tijera":
                if movimiento_pc == "piedra":
                    print(Fore.RED + "Perdiste")
                    puntos_ia += 1
                elif movimiento_pc == "papel":
                    print(Fore.GREEN + "Ganaste")
                    puntos_usuario += 1
                elif movimiento_pc == "tijera":
                    print(Fore.YELLOW + "Empate")

            print(Fore.MAGENTA + f"Marcador: {puntos_usuario} a {puntos_ia}")

        if puntos_usuario == 3:
            print(Fore.GREEN + f"🏆 Ganaste {puntos_usuario} a {puntos_ia}")
        else:
            print(Fore.RED + f"💀 Perdiste {puntos_usuario} a {puntos_ia}")

    else:
        print(Fore.RED + "Opción inválida")