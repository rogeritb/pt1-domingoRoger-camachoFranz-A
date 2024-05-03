"""
    FranzCamacho, RogerDomingo, AlfonsoOrtiz
    ASIX1c M03 UF1
    29/04/2024
    Pt3
"""
import random
def separararchivo(contenido):
    letras=('a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z')
    numeros=('1','2','3','4','5','6','7','8','9','0','(',')')
    palabras=[]
    for palabrades in contenido:
        if palabrades[0] in numeros:
            separado=palabrades
        elif len(palabrades)>3:
            if palabrades[0] not in letras:
                sep=list(palabrades[2:-1])
                random.shuffle(sep)
                separado=palabrades[0]+palabrades[1]+''.join(sep)+palabrades[-1]
            elif palabrades[-1] not in letras:
                sep=list(palabrades[1:-2])
                random.shuffle(sep)
                separado=palabrades[0]+''.join(sep)+palabrades[-2]+palabrades[-1]
            else:
                sep=list(palabrades[1:-1])
                random.shuffle(sep)
                separado=palabrades[0]+''.join(sep)+palabrades[-1]
        else:
            separado=palabrades
        palabras.append(separado)
    return palabras
def juntararchivo(palabras):
    frasedes=' '.join(palabras)
    return frasedes