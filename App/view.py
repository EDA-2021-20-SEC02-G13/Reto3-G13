"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import time
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

default_limit = 1000
sys.setrecursionlimit(default_limit*10)


# Funciones para la impresión de resultados

def printCargaArchivos(catalog, sizeUfos):
    """
    Imprime los datos requeridos para la carga de archivos
    """
    print("-"*62)
    print("Avistamientos cargados: " + str(sizeUfos))
    print("-"*62)
    for pos in range(1, 6):
        print(str(pos) + ":", lt.getElement(catalog["ufos"], pos))
    for pos in range(sizeUfos-4, sizeUfos+1):
        print(str(pos) + ":", lt.getElement(catalog["ufos"], pos))
    print("-"*62)


# Menu de opciones

def printMenu():
    print("\n" + "-"*20 + " Bienvenido al Reto 3 " + "-"*20)
    print("0 - Crear catalogo y cargar su información")
    print("1 - Req 1. Contar los avistamientos en una ciudad")
    print("2 - Req 2. Contar los avistamientos por duracion")
    print("3 - Req 3. Contar avistamientos por Hora/Minutos del dia")
    print("4 - Req 4. Contar los avistamientos en un rango de fechas")
    print("5 - Req 5. Contar los avistamientos de una zona geografica")
    print("6 - Bono. Visualizar los avistamientos de una zona geografica")
    print("7 - Salir de la aplicación")
    print("-"*62)


# Menu principal

catalog = None
ufoFile = "UFOS/UFOS-utf8-small.csv"

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input("Seleccione una opción para continuar: ")

    if int(inputs[0]) == 0:
        print("-"*61)
        print("Cargando información de los archivos ....")
        start_time = time.process_time()
        #
        catalog = controller.initCatalog()
        controller.loadData(catalog, ufoFile)
        sizeUfos = controller.ufosSize(catalog)
        #
        stop_time = time.process_time()
        elapsed_time_mseg = round((stop_time - start_time)*1000, 2)
        print("Tiempo:", elapsed_time_mseg, "mseg")
        printCargaArchivos(catalog, sizeUfos)

    elif int(inputs[0]) == 1:
        pass

    elif int(inputs[0]) == 2:
        pass

    elif int(inputs[0]) == 3:
        pass

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
        pass

    elif int(inputs[0]) == 6:
        pass

    else:
        sys.exit(0)
sys.exit(0)
