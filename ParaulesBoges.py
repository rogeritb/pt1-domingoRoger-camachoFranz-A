"""
Roger Domingo Meléndez - Franz Camacho Panozo
23/02/2024
ASIXc M03 UF2 pt1 R1: Disseny descendent: Dividir en funcions
Descripció: ParaulesBoges.
Implementar en Python un programa que demani una frase per teclat i la retorni per pantalla amb les lletres de cada paraula de la frase desordenada, tal com diu l’estudi de la Universitat de Cambridge.

"""

import random
import string

def desordenar_palabra(palabra):
    """Función para desordenar una palabra"""
    if len(palabra) <= 1:
        return palabra

    primera_caracter = palabra[0]
    ultima_caracter = palabra[-1]
    caracteres_intermedios = palabra[1:-1]
    caracteres_intermedios_desordenados = list(caracteres_intermedios)
    random.shuffle(caracteres_intermedios_desordenados)

    palabra_desordenada = primera_caracter + ''.join(caracteres_intermedios_desordenados) + ultima_caracter
    return palabra_desordenada

def desordenar_frase(frase):
    """Función para desordenar una frase"""
    palabras = frase.split()
    frase_desordenada = ""
    for palabra in palabras:
        if palabra.isalpha():
            palabra_desordenada = desordenar_palabra(palabra)
        else:
            palabra_desordenada = palabra
        frase_desordenada += palabra_desordenada + ' '
    return frase_desordenada.strip()

def main():
    """Función principal"""
    frase = input("Introduce una frase: ")
    frase_desordenada = desordenar_frase(frase)
    print("Frase desordenada:", frase_desordenada)

# Llamada a la función main al final del script
main()

