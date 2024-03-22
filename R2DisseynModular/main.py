"""
Roger Domingo Meléndez - Franz Camacho Panozo
04/03/2024
ASIXc M03 UF2 pt1 R2: Disseny Modular, R2, main.py
Descripcio
La seva funcionalitat és obtenir les dades, processar-les per a obtenir les “paraules boges” i finalment mostrar-les per pantalla
"""

from crazy_words import *
from data_source import *

from crazy_words import mostrar_menu, ejecutar_opcion

def ejecutar_menu():
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Ingrese una opción del menú: ")
        if opcion.isdigit():
            continuar = ejecutar_opcion(opcion)
        else:
            print("Aprende a leer, escribe un número del 1 al 5.")

def main():
    ejecutar_menu()

if __name__ == "__main__":
    main()
