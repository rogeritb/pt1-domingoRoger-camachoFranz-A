"""
    FranzCamacho RogerDomingo AlfonsoOrtiz
    ASIX1c M03 UF1 A5
    27/04/2024
    Realease 3
"""
import os
import crazyWords
import datetime
import logging

logging.basicConfig(filename='boges.log', level=logging.DEBUG,filemode='w', format='%(asctime)s - Paraulesboges - %(levelname)s - %(message)s')
def comprobarFile():
        archivo = 'paraules.txt'
        if os.path.exists(archivo):
            return True
        else:
            logging.error("No existe este archivo")
def comprobardirec():
    directorioentrada = './entrada'
    directoriosalida = './sortida'
    if os.path.exists(directorioentrada):
        if os.path.exists(directoriosalida):
            return True
        else:
            logging.error("No existe este Directorio")
    else:
        logging.error("No existe este Directorio")

def getDataFromFile():
    contador=0
    archivo = 'paraules.txt'
    try:
        archivofinal = open(archivo, "r")
        for linea in archivofinal:
            contenidonormal = linea
            # Enviar palabras locas
            contenidolista=contenidonormal.split()
            palabras=crazyWords.separararchivo(contenidolista)
            frasedes=crazyWords.juntararchivo(palabras)
            if contador==0:
                archivodestino = open("paraulesboges.txt", "w")
                archivodestino.write(frasedes)
            else:
                archivodestino = open("paraulesboges.txt", "a")
                archivodestino.write("\n"+frasedes)
            contador+=1
        logging.info("paraulesboges.txt - Archivo creado y volver loco el texto")
        archivofinal.close()
        archivodestino.close()
    except Exception as e:
        logging.error(str(e))        
def getDataFromFileDirecotio():
    contador=0
    directorientrada = './entrada'
    directorisalida = './sortida'
    try:
        llistaItems = os.listdir(directorientrada)
        print("Fitxers i directoris trobats a '%s': " % directorientrada)
        for item in llistaItems:
            rutaFitxer= os.path.join(directorientrada, item)
            if os.path.isfile(directorientrada + "/" + item):
                archivo=item.split(".")
                if archivo[1]=="txt":
                    print(f"ARCHIVO .txt\t {rutaFitxer}")
                    archivoinicial = open(rutaFitxer, "r")
                    archivoloco=archivo[0].replace(" ", "")
                    for linea in archivoinicial:
                        #contenidonormal = archivoinicial.readline()
                        contenidonormal = linea
                        # Enviar palabras locas
                        contenidolista=contenidonormal.split()
                        palabras=crazyWords.separararchivo(contenidolista)
                        frasedes=crazyWords.juntararchivo(palabras)
                        if contador==0:
                            archivodestino = open(directorisalida+"/"+archivoloco+"boges.txt", "w")
                            archivodestino.write(frasedes)
                        else:
                            archivodestino = open(directorisalida+"/"+archivoloco+"boges.txt", "a")
                            archivodestino.write("\n"+frasedes)
                        contador+=1
                    logging.info(f"{archivoloco}boges.txt - Archivo creado y volver loco el texto")
                    archivoinicial.close()
                    archivodestino.close()
                else:
                    print(f"OTROS ARCHIVOS\t {rutaFitxer}")
                    logging.info(f"{archivo[0]}.{archivo[1]} - No es un archivo .txt")
            else:
                print(f"DIRECTORI\t {rutaFitxer}")
                logging.info(f"{rutaFitxer}- És un directorio")
    except Exception as e:
                logging.error(str(e))

    