import random

def jugar():
    print("Bienvenido a Piedra, Papel, Tijeras!")
    opciones = ["piedra", "papel", "tijeras"]
    while True:
        jugador = input("Elige piedra, papel o tijeras (o 'salir' para volver al menú): ").lower()
        if jugador == "salir":
            break
        elif jugador not in opciones:
            print("Opción inválida. Inténtalo de nuevo.")
            continue

        computadora = random.choice(opciones)
        print(f"La computadora eligió: {computadora}")

        if jugador == computadora:
            print("Empate!")
        elif (jugador == "piedra" and computadora == "tijeras") or \
             (jugador == "papel" and computadora == "piedra") or \
             (jugador == "tijeras" and computadora == "papel"):
            print("¡Ganaste!")
        else:
            print("¡Perdiste!")
