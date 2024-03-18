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
            resultado += caracteres[indice_car]
            indice_car += 1
    return resultado

# Ejemplo de uso
entrada = input("Introduce una cadena con números y caracteres: ")
salida = mantener_numeros_en_su_posicion(entrada)
print("Salida:", salida)
