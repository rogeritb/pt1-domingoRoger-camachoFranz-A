import random

def jugar():
    print("Bienvenido a Adivina el número!")
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        intento = int(input("Introduce tu número: "))
        intentos += 1

        if intento < numero_secreto:
            print("El número es mayor.")
        elif intento > numero_secreto:
            print("El número es menor.")
        else:
            print(f"Felicidades! Has adivinado el número en {intentos} intentos.")
            break
