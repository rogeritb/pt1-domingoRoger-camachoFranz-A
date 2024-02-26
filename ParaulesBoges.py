"""
Roger Domingo Meléndez - Franz Camacho Panozo
23/02/2024
ASIXc M03 UF2 pt1 R1: Disseny descendent: Dividir en funcions
Descripció: ParaulesBoges.
Implementar en Python un programa que demani una frase per teclat i la retorni per pantalla amb les lletres de cada paraula de la frase desordenada, tal com diu l’estudi de la Universitat de Cambridge.

"""

import random
import string

def obtener_letras_validas(palabra):
    """Función para obtener solo las letras válidas de una palabra"""
    return [char for char in palabra if char in string.ascii_letters]

def desordenar_palabra(palabra):
    """Función para desordenar una palabra"""
    letras_validas = obtener_letras_validas(palabra)
    if letras_validas:
        primera_letra = letras_validas.pop(0)
        ultima_letra = letras_validas.pop()

        random.shuffle(letras_validas)

        palabra_desordenada = primera_letra + ''.join(letras_validas) + ultima_letra
        return palabra_desordenada
    else:
        return ""

def desordenar_frase(frase):
    """Función para desordenar una frase"""
    paraules = frase.split()
    frase_desordenada = ""
    for palabra in paraules:
        palabra_desordenada = desordenar_palabra(palabra)
        if palabra_desordenada:
            frase_desordenada += palabra_desordenada + ' '
    return frase_desordenada

def final():
    """Función final / input"""
    frase = input("Introdueix una frase: ")
    frase_desordenada = desordenar_frase(frase)
    print("Frase desordenada:", frase_desordenada)

final()