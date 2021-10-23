﻿"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Inicialización del catálogo de libros

def initCatalog():
    """
    Inicializa el catalogo de UFO Sightings
    """
    catalog = model.newCatalog()
    return catalog


# Funciones para la carga de datos

def loadData(catalog, ufoFile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    file = cf.data_dir + ufoFile
    input_file = csv.DictReader(open(file, encoding="utf-8"), delimiter=",")
    for ufo in input_file:
        model.addUfo(catalog, ufo)

# Funciones de ordenamiento


# Funciones de consulta sobre el catálogo

def ufosSize(catalog):
    """
    Retorna el numero de avistamientos cargados
    """
    return model.ufosSize(catalog)
