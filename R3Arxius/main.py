"""
    FranzCamacho RogerDomingo AlfonsoOrtiz
    ASIX1c M03 UF1 A5
    27/04/2024
    Realease 3
"""
import dataSource
import datetime
import os
def opcionfile():
    if dataSource.comprobarFile() is True:
        dataSource.getDataFromFile()
    opciondirec()
def opciondirec():    
    if dataSource.comprobardirec() is True:
        dataSource.getDataFromFileDirecotio()

opcion=opcionfile()