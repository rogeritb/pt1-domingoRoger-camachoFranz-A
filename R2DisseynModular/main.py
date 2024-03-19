"""
Roger Domingo Meléndez - Franz Camacho Panozo
04/03/2024
ASIXc M03 UF2 pt1 R2: Disseny Modular, R2, main.py
Descripcio
La seva funcionalitat és obtenir les dades, processar-les per a obtenir les “paraules boges” i finalment mostrar-les per pantalla
"""

from crazy_words import *
from data_source import *

def main():
    """Función principal"""
    frase = get_data_from_keyboard()
    frase_desordenada = desordenar_frase(frase)
    print("Frase desordenada:", frase_desordenada)

main()