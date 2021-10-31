"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from time import time
import config as cf
import datetime
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as ms
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos
listas, una para los videos, otra para las categorias de los mismos.
"""


# Construccion de modelos

def newCatalog():
    """
    Inicializa el catalogo de UFO Sightings. Se crea una lista vacia para
    guardar todos los avistamientos e indices para los requerimientos
    """
    catalog = {"ufos": None,
               "citiesIndex": None,
               "secondsIndex": None,
               "datesIndex": None,
               "longitudeIndex": None}

    catalog["ufos"] = lt.newList("ARRAY_LIST")

    catalog["citiesIndex"] = mp.newMap(19900,
                                       maptype="PROBING",
                                       loadfactor=0.5,
                                       comparefunction=compareCities)

    catalog["secondsIndex"] = om.newMap(omaptype="RBT",
                                        comparefunction=compareSeconds)

    catalog["datesIndex"] = om.newMap(omaptype="RBT",
                                      comparefunction=compareDates)
    
    catalog["timeIndex"] = om.newMap(omaptype="RBT",
                                      comparefunction=compareDates)

    catalog["longitudeIndex"] = om.newMap(omaptype="RBT",
                                          comparefunction=compareLongitude)

    return catalog


# Funciones para agregar informacion al catalogo

def addUfo(catalog, ufo):
    """
    Adiciona un avistamiento de un ovni a la lista de avistamientos,
    esta guarda en cada posicion la informacion de cada uno
    """
    lt.addLast(catalog["ufos"], ufo)
    updateCityIndex(catalog["citiesIndex"], ufo)
    updateSecondIndex(catalog["secondsIndex"], ufo)
    updateDateIndex(catalog["datesIndex"], ufo)
    updateTimeIndex(catalog['timeIndex'], ufo)
    updateLongitudeIndex(catalog["longitudeIndex"], ufo)


def updateCityIndex(citiesIndex, ufo):
    """
    Revisa si existe o no la ciudad en el mapa. En base a esto, crea una
    nueva estructura para modelarla, o la adiciona a la lista de avistamientos
    """
    ciudad = ufo["city"]
    entry = mp.get(citiesIndex, ciudad)
    if entry is None:
        cityEntry = newCity()
        mp.put(citiesIndex, ciudad, cityEntry)
    else:
        cityEntry = me.getValue(entry)
    lt.addLast(cityEntry["ltFecha"], ufo)


def updateSecondIndex(secondsIndex, ufo):
    """
    Revisa si existe o no la duracion en el mapa. En base a esto, crea una
    nueva estructura para modelarla, o la adiciona a la lista de avistamientos
    """
    seconds = float(ufo["duration (seconds)"])
    entry = om.get(secondsIndex, seconds)
    if entry is None:
        secondEntry = newSecond()
        om.put(secondsIndex, seconds, secondEntry)
    else:
        secondEntry = me.getValue(entry)
    lt.addLast(secondEntry["ltSegundos"], ufo)


def updateTimeIndex(timeIndex,ufo):
    """
    Revisa si existe o no la hora en el mapa. En base a esto, crea una
    nueva estructura para modelarla, o la adiciona a la lista de avistamientos
    """
    time = ufo["datetime"]
    ufoTime = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    entry = om.get(timeIndex, ufoTime.time())
    if entry is None:
        datentry = newTime()
        om.put(timeIndex, ufoTime.time(), datentry)
    else:
        datentry = me.getValue(entry)
    lt.addLast(datentry["ltTiempo"], ufo)


def updateDateIndex(datesIndex, ufo):
    """
    Revisa si existe o no la fecha en el mapa. En base a esto, crea una
    nueva estructura para modelarla, o la adiciona a la lista de avistamientos
    """
    date = ufo["datetime"]
    ufoDate = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    entry = om.get(datesIndex, ufoDate.date())
    if entry is None:
        datentry = newDate()
        om.put(datesIndex, ufoDate.date(), datentry)
    else:
        datentry = me.getValue(entry)
    lt.addLast(datentry["ltFecha"], ufo)


def updateLongitudeIndex(longitudeIndex, ufo):
    """
    Revisa si existe o no la longitud en el mapa. En base a esto, crea una
    nueva estructura para modelarla, o la adiciona a la lista de avistamientos
    """
    longitude = round(float(ufo["longitude"]), 2)
    entry = om.get(longitudeIndex, longitude)
    if entry is None:
        latitudentry = newLatitude()
        om.put(longitudeIndex, longitude, latitudentry)
    else:
        latitudentry = me.getValue(entry)
    updateLatitudeIndex(latitudentry["latitudeIndex"], ufo)


def updateLatitudeIndex(latitudeIndex, ufo):
    """
    Revisa si existe o no la latitud en el mapa. En base a esto, crea una
    nueva estructura para modelarla, o la adiciona a la lista de avistamientos
    """
    latitude = round(float(ufo["latitude"]), 2)
    entry = om.get(latitudeIndex, latitude)
    if entry is None:
        latentry = newLatitudelist()
        om.put(latitudeIndex, latitude, latentry)
    else:
        latentry = me.getValue(entry)
    lt.addLast(latentry["ltLatitude"], ufo)


# Funciones para creacion de datos

def newCity():
    """
    Crea una nueva estructura para modelar los avistamientos de una ciudad
    """
    cityentry = {"ltFecha": None}
    cityentry["ltFecha"] = lt.newList("ARRAY_LIST")
    return cityentry


def newSecond():
    """
    Crea una nueva estructura para modelar los avistamientos de una duracion
    en segundos
    """
    secondEntry = {"ltSegundos": None}
    secondEntry["ltSegundos"] = lt.newList("ARRAY_LIST")
    return secondEntry

def newTime():
    """
    Crea una nueva estructura para modelar los avistamientos de una hora
    """
    datentry = {"ltTiempo": None}
    datentry["ltTiempo"] = lt.newList("ARRAY_LIST", compareDates)
    return datentry

def newDate():
    """
    Crea una nueva estructura para modelar los avistamientos de una fecha
    """
    datentry = {"ltFecha": None}
    datentry["ltFecha"] = lt.newList("ARRAY_LIST")
    return datentry


def newLatitude():
    """
    Crea una nueva estructura para modelar los avistamientos de una latitud
    """
    latitudentry = {"latitudeIndex": None}
    latitudentry["latitudeIndex"] = om.newMap(omaptype="RBT",
                                              comparefunction=compareLatitude)
    return latitudentry


def newLatitudelist():
    """
    Crea una nueva estructura para modelar los avistamientos de una latitud
    """
    latentry = {"ltLatitude": None}
    latentry["ltLatitude"] = lt.newList("ARRAY_LIST")
    return latentry


# Funciones de consulta

def ufosSize(catalog):
    """
    Retorna el numero de avistamientos cargados
    """
    return lt.size(catalog["ufos"])


def getCityInfo(catalog, ciudad):
    """
    Obtiene el total de ciudades que han reportado avistamientos de ovnis,
    los avistamientos de una ciudad en especifico y su total
    """
    total = lt.size(mp.keySet(catalog["citiesIndex"]))
    entry = mp.get(catalog["citiesIndex"], ciudad)
    dictFecha = me.getValue(entry)
    ltCiudad = dictFecha["ltFecha"]
    ciudadTotal = lt.size(ltCiudad)
    ltCiudad2 = sortDateUfos(ltCiudad, ciudadTotal)
    return total, ltCiudad2, ciudadTotal


def getSecondInfo(catalog, sec1, sec2):
    """
    Obtiene el total de duraciones, la duracion en segundos mas larga, su
    total, los avistamientos en el rango, y la cantidad de dichos avistamientos
    """
    mapSeconds = catalog["secondsIndex"]
    total = lt.size(om.keySet(mapSeconds))
    mayor = om.maxKey(mapSeconds)
    parejaMayor = om.get(mapSeconds, mayor)
    dictMayor = me.getValue(parejaMayor)
    totalMayor = lt.size(dictMayor["ltSegundos"])
    ltRango1 = om.values(mapSeconds, sec1, sec2)
    ltRango2 = lt.newList("ARRAY_LIST")
    for lista in lt.iterator(ltRango1):
        for ufo in lt.iterator(lista["ltSegundos"]):
            lt.addLast(ltRango2, ufo)
    ltRango3 = sortSecondUfos(ltRango2, lt.size(ltRango2))
    return total, mayor, totalMayor, ltRango3, lt.size(ltRango2)


def getTimeInfo(catalog, tiempo1, tiempo2):
    """
    Obtiene la hora mas antigua del mapa, la cantidad de horas, los valores
    dentro del rango dado y su total
    """
    t1 = datetime.datetime.strptime(tiempo1, "%H:%M").time()
    t2 = datetime.datetime.strptime(tiempo2, "%H:%M").time()
    mapFechas = catalog["timeIndex"]
    total = lt.size(om.keySet(mapFechas))
    menor = om.maxKey(mapFechas)

    ltRango1 = om.values(mapFechas, t1, t2)
    ltRango2 = lt.newList("ARRAY_LIST")
    for lista in lt.iterator(ltRango1):
        for ufo in lt.iterator(lista["ltTiempo"]):
            lt.addLast(ltRango2, ufo)
    ltRango3 = sortDateUfos(ltRango2, lt.size(ltRango2))
    return menor, total, ltRango3, lt.size(ltRango2)


def getDateInfo(catalog, fecha1, fecha2):
    """
    Obtiene la fecha mas antigua del mapa, la cantidad de fechas, los valores
    dentro del rango dado y su total
    """
    f1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d").date()
    f2 = datetime.datetime.strptime(fecha2, "%Y-%m-%d").date()
    mapFechas = catalog["datesIndex"]
    total = lt.size(om.keySet(mapFechas))
    menor = om.minKey(mapFechas)
    parejaMenor = om.get(mapFechas, menor)
    dictMenor = me.getValue(parejaMenor)
    totalMenor = lt.size(dictMenor["ltFecha"])
    ltRango1 = om.values(mapFechas, f1, f2)
    ltRango2 = lt.newList("ARRAY_LIST")
    for lista in lt.iterator(ltRango1):
        for ufo in lt.iterator(lista["ltFecha"]):
            lt.addLast(ltRango2, ufo)
    ltRango3 = sortDateUfos(ltRango2, lt.size(ltRango2))
    return menor, totalMenor, total, ltRango3, lt.size(ltRango2)


def getGeographicInfo(catalog, log1, log2, lat1, lat2):
    """
    Obtiene el numero de avistamientos de una zona geografica, definida por la
    longitud y latitud de los parametros
    """
    mapLongitudes = catalog["longitudeIndex"]
    ltLongitudes = om.values(mapLongitudes, log1, log2)
    ltTotal = lt.newList("ARRAY_LIST")
    for mapLatitudes in lt.iterator(ltLongitudes):
        ltLatitudes = om.values(mapLatitudes["latitudeIndex"], lat1, lat2)
        for latitude in lt.iterator(ltLatitudes):
            for ufo in lt.iterator(latitude["ltLatitude"]):
                lt.addLast(ltTotal, ufo)
    return lt.size(ltTotal), ltTotal


# Funciones de comparacion

def compareCities(keyname, fecha):
    """
    Compara dos ciudades. La primera es una cadena de caracteres y el segundo
    un entry de un map
    """
    dateEntry = me.getKey(fecha)
    if (keyname == dateEntry):
        return 0
    elif (keyname > dateEntry):
        return 1
    else:
        return -1


def cmpUfoByDate(ufo1, ufo2):
    """
    Devuelve verdadero (True) si el "Date" de ufo1 es menor que el de ufo2
    Args:
        ufo1: informacion del primer avistamiento que
              incluye su valor "datetime"
        ufo2: informacion del segundo avistamiento que
              incluye su valor "datetime"
    """
    date1 = datetime.datetime.strptime(ufo1["datetime"], "%Y-%m-%d %H:%M:%S")
    date2 = datetime.datetime.strptime(ufo2["datetime"], "%Y-%m-%d %H:%M:%S")
    return date1 < date2


def cmpUfoBySecond(ufo1, ufo2):
    """
    Devuelve verdadero (True) si el "duration (seconds)" de ufo1 es menor que
    el de ufo2, si son iguales, compara las ciudades y los paises
    Args:
        ufo1: informacion del primer avistamiento que
              incluye su valor "duration (seconds)"
        ufo2: informacion del segundo avistamiento que
              incluye su valor "duration (seconds)"
    """
    ans1 = float(ufo1["duration (seconds)"])
    ans2 = float(ufo2["duration (seconds)"])
    if ans1 == ans2:
        ans1 = ufo1["city"]
        ans2 = ufo2["city"]
        if ans1 == ans2:
            ans1 = ufo1["country"]
            ans2 = ufo2["country"]
    return ans1 < ans2


def compareSeconds(sec1, sec2):
    """
    Compara dos tiempos de duracion en segundos de avistamientos
    """
    if (sec1 == sec2):
        return 0
    elif (sec1 > sec2):
        return 1
    else:
        return -1


def compareDates(date1, date2):
    """
    Compara dos fechas de dos avistamientos de ovnis
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1


def compareLongitude(log1, log2):
    """
    Compara dos coordenadas de longitud de dos avistamientos de ovnis
    """
    if (log1 == log2):
        return 0
    elif (log1 > log2):
        return 1
    else:
        return -1


def compareLatitude(lat1, lat2):
    """
    Compara dos coordenadas de latitud de dos avistamientos de ovnis
    """
    if (lat1 == lat2):
        return 0
    elif (lat1 > lat2):
        return 1
    else:
        return -1


# Funciones de ordenamiento

def sortDateUfos(ufos, sizeUfos):
    """
    Ordena los avistamientos por su fecha
    """
    sub_list = lt.subList(ufos, 1, sizeUfos)
    sub_list = sub_list.copy()
    sorted_list = ms.sort(sub_list, cmpUfoByDate)
    return sorted_list


def sortSecondUfos(ufos, sizeUfos):
    """
    Ordena los avistamientos por su duracion en segundos
    """
    sub_list = lt.subList(ufos, 1, sizeUfos)
    sub_list = sub_list.copy()
    sorted_list = ms.sort(sub_list, cmpUfoBySecond)
    return sorted_list
