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


import config as cf
import datetime
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
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
    catalog = {"ufos": None}

    catalog["ufos"] = lt.newList("ARRAY_LIST")

    catalog["datesIndex"] = om.newMap(omaptype="RBT",
                                      comparefunction=compareDates)

    return catalog


# Funciones para agregar informacion al catalogo

def addUfo(catalog, ufo):
    """
    Adiciona un avistamiento de un ovni a la lista de avistamientos,
    esta guarda en cada posicion la informacion de cada uno
    """
    lt.addLast(catalog["ufos"], ufo)
    updateDateIndex(catalog["datesIndex"], ufo)


def updateDateIndex(datesIndex, ufo):
    """
    Revisa si existe o no la fecha en el mapa. En base a esto, crea una
    nueva estructura para modelarla, o la adiciona a la lista de fechas
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


# Funciones para creacion de datos

def newDate():
    """
    Crea una nueva estructura para modelar los avistamientos de una fecha
    """
    datentry = {"ltFecha": None}
    datentry["ltFecha"] = lt.newList("ARRAY_LIST", compareDates)
    return datentry


# Funciones de consulta

def ufosSize(catalog):
    """
    Retorna el numero de avistamientos cargados
    """
    return lt.size(catalog["ufos"])


# Funciones de comparacion

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

# Funciones de ordenamiento
