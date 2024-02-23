"""
Roger Domingo Meléndez
23/02/2024
ASIXc M03 UF2 pt1 R1: Disseny descendent: Dividir en funcions
Descripció: ParaulesBoges.
Implementar en Python un programa que demani una frase per teclat i la retorni per pantalla amb les lletres de cada paraula de la frase desordenada, tal com diu l’estudi de la Universitat de Cambridge.

"""
import random

def desordenar_frase(frase):
    paraules = frase.split()
    frase_desordenada = ""

    for palabra in paraules:
        lletres = list(palabra)
        primera_lletra = lletres.pop(0)
        ultima_lletra = lletres.pop()

        random.shuffle(lletres)

        palabra_desordenada = primera_lletra + ''.join(lletres) + ultima_lletra
        frase_desordenada += palabra_desordenada + ' '

    return frase_desordenada.rstrip()


frase = input("Introdueix una frase: ")
frase_desordenada = desordenar_frase(frase)
print("Frase desordenada:", frase_desordenada)