"""
    Joel Guerrero, Matvei Karikh, Matteo Vilchez
    ASIX1c M03 UF1 A5
    25/04/2023
    Pt3
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