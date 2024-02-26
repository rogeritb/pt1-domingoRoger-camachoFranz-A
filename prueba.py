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
        if "@" in palabra:  # Si es una dirección de correo electrónico
            partes_correo = palabra.split("@")
            usuario = partes_correo[0]
            dominio = partes_correo[1]
            usuario_desordenado = desordenar_palabra(usuario)
            dominio_desordenado = desordenar_palabra(dominio)
            palabra_desordenada = usuario_desordenado + "@" + dominio_desordenado
        else:
            palabra_desordenada = desordenar_palabra(palabra)
        frase_desordenada += palabra_desordenada + ' '
    return frase_desordenada.strip()

def main():
    """Función principal"""
    frase = input("Introduce una frase: ")
    frase_desordenada = desordenar_frase(frase)
    print("Frase desordenada:", frase_desordenada)

# Llamada a la función main al final del script
main()

