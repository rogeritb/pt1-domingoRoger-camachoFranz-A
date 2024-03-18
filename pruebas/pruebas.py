import random

def desordenar_caracteres(caracteres):
    """Función para desordenar una lista de caracteres"""
    caracteres_desordenados = list(caracteres)
    random.shuffle(caracteres_desordenados)
    return ''.join(caracteres_desordenados)

def desordenar_palabra(palabra):
    """Función para desordenar una palabra respetando la primera y última letra"""
    if len(palabra) <= 3 or palabra.isdigit():
        return palabra

    primera_caracter = palabra[0]
    ultima_caracter = palabra[-1]
    caracteres_intermedios = palabra[1:-1]
    caracteres_intermedios_desordenados = desordenar_caracteres(caracteres_intermedios)

    palabra_desordenada = primera_caracter + caracteres_intermedios_desordenados + ultima_caracter
    return palabra_desordenada

def desordenar_palabra_correo(palabra):
    """Función para desordenar una palabra de un correo electrónico"""
    if "@" in palabra:
        partes_correo = palabra.split('@')
        usuario_desordenado = desordenar_palabra(partes_correo[0])
        dominio_desordenado = '.'.join([desordenar_palabra(part) for part in partes_correo[1].split('.')])
        palabra_desordenada = f"{usuario_desordenado}@{dominio_desordenado}"
        return palabra_desordenada
    else:
        return desordenar_palabra(palabra)

def desordenar_frase(frase):
    """Función para desordenar una frase"""
    palabras = frase.split()
    frase_desordenada = ""
    for palabra in palabras:
        palabra_desordenada = desordenar_palabra_correo(palabra)
        frase_desordenada += palabra_desordenada + ' '
    return frase_desordenada.strip()


def mantener_numeros_en_su_posicion(cadena):
    """Función para mantener los números en su posición sin desordenarlos"""
    numeros = ''.join([c for c in cadena if c.isdigit()])
    caracteres = ''.join([c for c in cadena if not c.isdigit()])

    resultado = ""
    indice_num = 0
    indice_car = 0

    for char in cadena:
        if char.isdigit():
            resultado += numeros[indice_num]
            indice_num += 1
        else:
            resultado += char

    return resultado


