"""
Roger Domingo Meléndez - Franz Camacho Panozo
04/03/2024
ASIXc M03 UF2 pt1 R2: Disseny Modular, R2, main.py
Descripcio
La seva funcionalitat és obtenir les dades, processar-les per a obtenir les “paraules boges” i finalment mostrar-les per pantalla
"""

import ParaulesBoges

def main():
    """Funció principal"""
    frase = input("Introdueix una frase: ")
    frase_desordenada = ParaulesBoges.desordenar_frase(frase)
    print("Frase desordenada:", frase_desordenada)

if __name__ == "__main__":
    main()
