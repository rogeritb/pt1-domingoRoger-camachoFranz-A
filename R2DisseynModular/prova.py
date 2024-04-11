import juego_adivina_numero
import juego_piedra_papel_tijeras

def menu():
    print("1. Adivina el número")
    print("2. Piedra, Papel, Tijeras")
    print("3. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        juego_adivina_numero.jugar()
    elif opcion == "2":
        juego_piedra_papel_tijeras.jugar()
    elif opcion == "3":
        print("¡Hasta luego!")
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
        menu()

if __name__ == "__main__":
    menu()
