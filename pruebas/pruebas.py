import random

def desordenar_caracteres(caracteres):

    if len(caracteres) <= 2:
        return caracteres
    caracteres_intermedios = list(caracteres[1:-1])
    random.shuffle(caracteres_intermedios)
    return caracteres[0] + ''.join(caracteres_intermedios) + caracteres[-1]

def desordenar_palabra(palabra):

    if len(palabra) <= 3 or palabra.isdigit():
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

def mantener_numeros_en_su_posicion(cadena):

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
            resultado += caracteres[indice_car]
            indice_car += 1
    return resultado