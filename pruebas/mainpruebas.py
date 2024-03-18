from pruebas import *


def main():
    """Función principal"""
    frase = input("Introduce una frase: ")
    frase_desordenada = desordenar_frase(frase)
    print("Frase desordenada:", frase_desordenada)

main()