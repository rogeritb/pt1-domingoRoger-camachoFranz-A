"""
Roger Domingo Meléndez - Franz Camacho Panozo
04/03/2024
ASIXc M03 UF2 pt1 R2: Disseny Modular, R2, crazy_words.py
Descripcio
És “qui sap”, és a dir, té implementada la lògica necessària per a convertir un text de paraules “normals”, en un text de “paraules boges”
"""

import random
from data_source import *

def mostrar_menu():
    print("Selecciona una opción:")
    print("1. Obtener datos desde el teclado")
    print("2. Obtener datos desde el servidor")
    print("3. Obtener datos desde ChatGPT")
    print("4. Obtener datos desde un archivo")
    print("5. Salir")

def ejecutar_opcion(opcion):
    if opcion == 1:
        datos = get_data_from_keyboard()
        # Aquí puedes hacer lo que necesites con los datos obtenidos
    elif opcion == 2:
        URL = "https://api.api-ninjas.com/v1/dadjokes"
        get_data_from_server(URL)
    elif opcion == 3:
        pregunta = input("Introduce tu pregunta: ")
        get_data_from_chatGTP(pregunta)
    elif opcion == 4:
        file_name = input("Introduce el nombre del archivo: ")
        get_data_from_file(file_name)
    elif opcion == 5:
        print("Saliendo...")
        return False
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")

    return True

def main():
    menu = ''
    while menu <1 and menu >4:
        menu = input('Ingrese un opcion: ')
        if menu == '1':
            print()
        elif menu == '2':
            print()
        elif menu == '3':
            print()
        elif menu == '4':
            print()
def mantener_numeros_en_su_posicion(palabra):
    tiene_numeros = any(c.isdigit() for c in palabra)
    tiene_no_numeros = any(not c.isdigit() for c in palabra)

    if tiene_numeros and tiene_no_numeros:
        return palabra

    return ''.join(c for c in palabra)

def desordenar_caracteres(caracteres):
    if len(caracteres) <= 2:
        return caracteres
    caracteres_intermedios = list(caracteres[1:-1])
    random.shuffle(caracteres_intermedios)
    return caracteres[0] + ''.join(caracteres_intermedios) + caracteres[-1]

def desordenar_palabra(palabra):
    if len(palabra) <= 3 or (all(c.isdigit() or c == '.' or c == ',' or c == '$' or c == '€' for c in palabra)):
        return palabra

    primera_caracter = palabra[0]
    ultima_caracter = palabra[-1]

    caracteres_intermedios_desordenados = desordenar_caracteres(palabra[1:-1])

    palabra_desordenada = primera_caracter + caracteres_intermedios_desordenados + ultima_caracter
    return palabra_desordenada

def desordenar_palabra_correo(palabra):
    if "@" in palabra:
        partes_correo = palabra.split('@')
        usuario_desordenado = desordenar_palabra(partes_correo[0])
        dominio_desordenado = '.'.join([desordenar_palabra(part) for part in partes_correo[1].split('.')])
        palabra_desordenada = f"{usuario_desordenado}@{dominio_desordenado}"
        return palabra_desordenada
    else:
        return desordenar_palabra(palabra)

def desordenar_frase(frase):
    palabras = frase.split()
    frase_desordenada = ""
    for palabra in palabras:
        palabra_desordenada = desordenar_palabra_correo(palabra)
        frase_desordenada += palabra_desordenada + ' '
    return frase_desordenada.strip()
