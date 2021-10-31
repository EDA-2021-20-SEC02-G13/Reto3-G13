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
from DISClib.ADT import orderedmap as om
from prettytable import PrettyTable, ALL
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
    print("Altura del arbol fechas:", om.height(catalog["datesIndex"]))
    print("Numero de elementos:", om.size(catalog['datesIndex']))
    print("")
    print("Altura del arbol segundos:", om.height(catalog["secondsIndex"]))
    print("Numero de elementos:", om.size(catalog['secondsIndex']))
    print("")
    print("Altura del arbol longitudes:", om.height(catalog["longitudeIndex"]))
    print("Numero de elementos:", om.size(catalog['longitudeIndex']))
    print("-"*62)
    for pos in range(1, 6):
        print(str(pos) + ":", lt.getElement(catalog["ufos"], pos))
    for pos in range(sizeUfos-4, sizeUfos+1):
        print(str(pos) + ":", lt.getElement(catalog["ufos"], pos))
    print("-"*62)


def printCityUfos(ciudad, total, ltCiudad, ciudadTotal):
    """
    Imprime los datos requeridos para el requerimiento 1
    """
    tbCity = PrettyTable(["datetime", "city", "state", "country", "shape",
                          "duration (seconds)"])
    u = 1
    for pos in range(1, 4):
        ufo = lt.getElement(ltCiudad, pos)
        tbCity.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                        ufo["country"], ufo["shape"],
                        ufo["duration (seconds)"]])
        u += 1
        if u > total:
            break
    if ciudadTotal == 4:
        ufo = lt.getElement(ltCiudad, ciudadTotal)
        tbCity.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                        ufo["country"], ufo["shape"],
                        ufo["duration (seconds)"]])
    elif ciudadTotal == 5:
        for pos in range(ciudadTotal-1, ciudadTotal+1):
            ufo = lt.getElement(ltCiudad, pos)
            tbCity.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                            ufo["country"], ufo["shape"],
                            ufo["duration (seconds)"]])
    elif ciudadTotal > 5:
        for pos in range(ciudadTotal-2, ciudadTotal+1):
            ufo = lt.getElement(ltCiudad, pos)
            tbCity.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                            ufo["country"], ufo["shape"],
                            ufo["duration (seconds)"]])
    tbCity.max_width = 40
    tbCity.hrules = ALL
    print("\n" + "-"*23 + " Req 1. Answer " + "-"*24)
    print("There are " + str(total) + " different cities with UFO sightings.")
    print("\n" + "There are " + str(ciudadTotal) + " sightings at the "
          + ciudad + " city.")
    print("The first 3 and last 3 UFO sightings in the city are:")
    print(tbCity)


def printSecondsUfos(s1, s2, total, mayor, totalMayor, ltRango, totalRango):
    """
    Imprime los datos requeridos para el requerimiento 2
    """
    tbSeconds = PrettyTable(["datetime", "city", "state", "country", "shape",
                             "duration (seconds)"])
    u = 1
    for pos in range(1, 4):
        ufo = lt.getElement(ltRango, pos)
        tbSeconds.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                           ufo["country"], ufo["shape"],
                           ufo["duration (seconds)"]])
        u += 1
        if u > total:
            break
    if totalRango == 4:
        ufo = lt.getElement(ltRango, totalRango)
        tbSeconds.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                          ufo["country"], ufo["shape"],
                          ufo["duration (seconds)"]])
    elif totalRango == 5:
        for pos in range(totalRango-1, totalRango+1):
            ufo = lt.getElement(ltRango, pos)
            tbSeconds.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                               ufo["country"], ufo["shape"],
                               ufo["duration (seconds)"]])
    elif totalRango > 5:
        for pos in range(totalRango-2, totalRango+1):
            ufo = lt.getElement(ltRango, pos)
            tbSeconds.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                               ufo["country"], ufo["shape"],
                               ufo["duration (seconds)"]])
    tbSeconds.max_width = 40
    tbSeconds.hrules = ALL
    print("\n" + "-"*23 + " Req 2. Answer " + "-"*24)
    print("There are " + str(total) + " different UFO sightings durations.")
    print("The largest duration is " + str(mayor) + " seconds, with "
          + str(totalMayor) + " UFO sightings.")
    print("\n" + "There are " + str(totalRango) + " sightings between: "
          + str(s1) + " and " + str(s2) + " duration.")
    print("The first 3 and last 3 UFO sightings in the duration time are:")
    print(tbSeconds)


def printTimessUfos(f1, f2, total, menor, ltRango, totalRango):
    """
    Imprime los datos requeridos para el requerimiento 3
    """
    Ultimos_5 = lt.newList('ARRAY_LIST')
    tbDates = PrettyTable(["datetime", "city", "state", "country", "shape",
                           "duration (seconds)"])
    u = 1
    for pos in range(1, 4):
        ufo = lt.getElement(ltRango, pos)
        tbDates.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                         ufo["country"], ufo["shape"],
                         ufo["duration (seconds)"]])
        u += 1
        if u > total:
            break
    if totalRango == 4:
        ufo = lt.getElement(ltRango, totalRango)
        tbDates.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                         ufo["country"], ufo["shape"],
                         ufo["duration (seconds)"]])
    elif totalRango == 5:
        for pos in range(totalRango-1, totalRango+1):
            ufo = lt.getElement(ltRango, pos)
            tbDates.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                             ufo["country"], ufo["shape"],
                             ufo["duration (seconds)"]])
    elif totalRango > 5:
        for pos in range(totalRango-2, totalRango+1):
            ufo = lt.getElement(ltRango, pos)
            tbDates.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                             ufo["country"], ufo["shape"],
                             ufo["duration (seconds)"]])
    tbDates.max_width = 40
    tbDates.hrules = ALL
    print("\n" + "-"*23 + " Req 3. Answer " + "-"*24)
    print("There are " + str(total) + " different UFO sightings dates "
          + "[hh:mm:ss].")
    print("The 5 latest time for ufo are: ")
    Tiempos = om.keySet(catalog['timeIndex'])
    ctn = 0
    for j in reversed(range(1, (lt.size(Tiempos)+1))):
        c = lt.getElement(Tiempos, j-1)
        d = lt.getElement(Tiempos, j)
        if c != d and ctn < 5:
            last = lt.getElement(Tiempos, j)
            lt.addLast(Ultimos_5, last)
            ctn += 1
    for no in range(1, (lt.size(Ultimos_5)+1)): 
        xd = om.get(catalog['timeIndex'],lt.getElement(Ultimos_5,no))
        wuatafok = xd['value']
        print(lt.getElement(Ultimos_5,no),lt.size(wuatafok['ltTiempo']))
        
    print("\n" + "There are " + str(totalRango) + " sightings between: "
        + str(f1) + " and " + str(f2))
    print("The first 3 and last 3 UFO sightings in this time are:")
    print(tbDates)


def printDatesUfos(f1, f2, total, menor, ltRango, totalRango):
    """
    Imprime los datos requeridos para el requerimiento 4
    """
    tbDates = PrettyTable(["datetime", "city", "state", "country", "shape",
                           "duration (seconds)"])
    u = 1
    for pos in range(1, 4):
        ufo = lt.getElement(ltRango, pos)
        tbDates.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                         ufo["country"], ufo["shape"],
                         ufo["duration (seconds)"]])
        u += 1
        if u > total:
            break
    if totalRango == 4:
        ufo = lt.getElement(ltRango, totalRango)
        tbDates.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                         ufo["country"], ufo["shape"],
                         ufo["duration (seconds)"]])
    elif totalRango == 5:
        for pos in range(totalRango-1, totalRango+1):
            ufo = lt.getElement(ltRango, pos)
            tbDates.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                             ufo["country"], ufo["shape"],
                             ufo["duration (seconds)"]])
    elif totalRango > 5:
        for pos in range(totalRango-2, totalRango+1):
            ufo = lt.getElement(ltRango, pos)
            tbDates.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                             ufo["country"], ufo["shape"],
                             ufo["duration (seconds)"]])
    tbDates.max_width = 40
    tbDates.hrules = ALL
    print("\n" + "-"*23 + " Req 4. Answer " + "-"*24)
    print("There are " + str(total) + " different UFO sightings dates "
          + "[YYYY-MM-DD].")
    print("The oldest date is " + str(menor))
    print("\n" + "There are " + str(totalRango) + " sightings between: "
          + str(f1) + " and " + str(f2))
    print("The first 3 and last 3 UFO sightings in this time are:")
    print(tbDates)


def printGeoUfos(total, geoUfos):
    """
    Imprime los datos requeridos para el requerimiento 5
    """
    tbGeo = PrettyTable(["datetime", "city", "state", "country", "shape",
                         "duration (seconds)", "latitude", "longitude"])
    u = 1
    for pos in range(1, 6):
        ufo = lt.getElement(geoUfos, pos)
        tbGeo.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                       ufo["country"], ufo["shape"],
                       ufo["duration (seconds)"], ufo["latitude"],
                       ufo["longitude"]])
        u += 1
        if u > total:
            break
    if total == 6:
        ufo = lt.getElement(geoUfos, total)
        tbGeo.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                       ufo["country"], ufo["shape"],
                       ufo["duration (seconds)"], ufo["latitude"],
                       ufo["longitude"]])
    elif total == 7:
        for pos in range(total-1, total+1):
            tbGeo.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                           ufo["country"], ufo["shape"],
                           ufo["duration (seconds)"], ufo["latitude"],
                           ufo["longitude"]])
    elif total == 8:
        for pos in range(total-2, total+1):
            tbGeo.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                           ufo["country"], ufo["shape"],
                           ufo["duration (seconds)"], ufo["latitude"],
                           ufo["longitude"]])
    elif total == 9:
        for pos in range(total-3, total+1):
            tbGeo.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                           ufo["country"], ufo["shape"],
                           ufo["duration (seconds)"], ufo["latitude"],
                           ufo["longitude"]])
    elif total == 10:
        for pos in range(total-4, total+1):
            tbGeo.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                           ufo["country"], ufo["shape"],
                           ufo["duration (seconds)"], ufo["latitude"],
                           ufo["longitude"]])
    elif total > 10:
        for pos in range(total-5, total+1):
            tbGeo.add_row([ufo["datetime"], ufo["city"], ufo["state"],
                           ufo["country"], ufo["shape"],
                           ufo["duration (seconds)"], ufo["latitude"],
                           ufo["longitude"]])
    tbGeo.max_width = 40
    tbGeo.hrules = ALL
    print("\n" + "-"*23 + " Req 5. Answer " + "-"*24)
    print("There are " + str(total) + " different UFO sightings in the current"
          + " area.")
    print("The first 5 and last 5 UFO sightings in this time are:")
    print(tbGeo)


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
        print("-"*62)
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
        print("\n" + "-"*23 + " Req 1. Inputs " + "-"*24)
        ciudad = str(input("Indique la ciudad que desea de buscar: "))
        start_time = time.process_time()
        #
        tplCiudad = controller.getCityInfo(catalog, ciudad)
        #
        stop_time = time.process_time()
        elapsed_time_mseg = round((stop_time - start_time)*1000, 2)
        print("Tiempo:", elapsed_time_mseg, "mseg")
        printCityUfos(ciudad, tplCiudad[0], tplCiudad[1], tplCiudad[2])

    elif int(inputs[0]) == 2:
        print("\n" + "-"*23 + " Req 2. Inputs " + "-"*24)
        sec1 = float(input("Indique la duracion inicial con la que desea"
                           " iniciar el rango: "))
        sec2 = float(input("Indique la duracion final con la que desea"
                           " finalizar el rango: "))
        start_time = time.process_time()
        #
        tplRangeSecond = controller.getSecondInfo(catalog, sec1, sec2)
        total = tplRangeSecond[0]
        mayor = tplRangeSecond[1]
        totalMayor = tplRangeSecond[2]
        ltRangoSecond = tplRangeSecond[3]
        totalRangoSecond = tplRangeSecond[4]
        #
        stop_time = time.process_time()
        elapsed_time_mseg = round((stop_time - start_time)*1000, 2)
        print("Tiempo:", elapsed_time_mseg, "mseg")
        printSecondsUfos(sec1, sec2, total, mayor, totalMayor, ltRangoSecond,
                         totalRangoSecond)

    elif int(inputs[0]) == 3:
        print("\n" + "-"*23 + " Req 4. Inputs " + "-"*24)
        tiempo1 = input("Indique la hora inicial con la que desea"
                       " iniciar el rango: ")
        tiempo2 = input("Indique la hora final con la que desea"
                       " finalizar el rango: ")
        start_time = time.process_time()
        #
        tplRangeTime = controller.getTimeInfo(catalog, tiempo1, tiempo2)
        menor = tplRangeTime[0]
        total = tplRangeTime[1]
        ltRangoFecha = tplRangeTime[2]
        totalRangoFecha = tplRangeTime[3]
        #
        stop_time = time.process_time()
        elapsed_time_mseg = round((stop_time - start_time)*1000, 2)
        print("Tiempo:", elapsed_time_mseg, "mseg")
        printTimessUfos(tiempo1, tiempo2, total, menor, ltRangoFecha,
                       totalRangoFecha)
        

    elif int(inputs[0]) == 4:
        print("\n" + "-"*23 + " Req 4. Inputs " + "-"*24)
        fecha1 = input("Indique la fecha inicial con la que desea"
                       " iniciar el rango: ")
        fecha2 = input("Indique la fecha final con la que desea"
                       " finalizar el rango: ")
        start_time = time.process_time()
        #
        tplRangeDate = controller.getDateInfo(catalog, fecha1, fecha2)
        menor = tplRangeDate[0]
        total = tplRangeDate[1]
        ltRangoFecha = tplRangeDate[2]
        totalRangoFecha = tplRangeDate[3]
        #
        stop_time = time.process_time()
        elapsed_time_mseg = round((stop_time - start_time)*1000, 2)
        print("Tiempo:", elapsed_time_mseg, "mseg")
        printDatesUfos(fecha1, fecha2, total, menor, ltRangoFecha,
                       totalRangoFecha)

    elif int(inputs[0]) == 5:
        print("\n" + "-"*23 + " Req 5. Inputs " + "-"*24)
        log1 = round(float(input("Indique la longitud inicial con la que desea"
                                 " iniciar el rango: ")), 2)
        log2 = round(float(input("Indique la longitud final con la que desea"
                                 " finalizar el rango: ")), 2)
        lat1 = round(float(input("Indique la latitud inicial con la que desea"
                                 " iniciar el rango: ")), 2)
        lat2 = round(float(input("Indique la latitud final con la que desea"
                                 " finalizar el rango: ")), 2)
        log2 = -103.00
        log1 = -109.05
        lat1 = 31.33
        lat2 = 37.00
        start_time = time.process_time()
        #
        tplGeo = controller.getGeographicInfo(catalog, log1, log2, lat1, lat2)
        total = tplGeo[0]
        geoUfos = tplGeo[1]
        #
        stop_time = time.process_time()
        elapsed_time_mseg = round((stop_time - start_time)*1000, 2)
        print("Tiempo:", elapsed_time_mseg, "mseg")
        printGeoUfos(total, geoUfos)

    elif int(inputs[0]) == 6:
        pass

    else:
        sys.exit(0)
sys.exit(0)
