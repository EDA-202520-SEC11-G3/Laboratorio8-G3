"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
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
 * Contribuciones
 *
 * Dario Correal
 """

import os
import csv
import datetime
from DataStructures.Tree import red_black_tree as rbt
from DataStructures.List import single_linked_list as al
from DataStructures.Map import map_linear_probing as lp

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

def new_logic():
    analyzer = {
        "crimes": None,
        "dateIndex": None,
        "areaIndex": None
    }
    analyzer["crimes"] = al.new_list()
    analyzer["dateIndex"] = rbt.new_map()
    analyzer["areaIndex"] = rbt.new_map()  # Árbol por áreas reportadas
    return analyzer

def load_data(analyzer, crimesfile):
    crimesfile = data_dir + crimesfile
    input_file = csv.DictReader(open(crimesfile, encoding="utf-8"), delimiter=",")
    for crime in input_file:
        add_crime(analyzer, crime)
    return analyzer

def add_crime(analyzer, crime):
    al.add_last(analyzer['crimes'], crime)
    update_date_index(analyzer['dateIndex'], crime)
    update_area_index(analyzer['areaIndex'], crime)
    return analyzer

def update_area_index(map, crime):
    area = crime.get("REPORTED_AREA", None)
    if area in ["", " ", None]:
        area = 9999
    entry = rbt.get(map, area)
    if entry is None:
        entry = al.new_list()
        rbt.put(map, area, entry)
    al.add_last(entry, crime)
    return map

def update_date_index(map, crime):
    occurreddate = crime['OCCURRED_ON_DATE']
    crimedate = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
    entry = rbt.get(map, crimedate.date())
    if entry is None:
        datentry = new_data_entry(crime)
        rbt.put(map, crimedate.date(), datentry)
    else:
        datentry = entry
    add_date_index(datentry, crime)
    return map

def add_date_index(datentry, crime):
    lst = datentry["lstcrimes"]
    al.add_last(lst, crime)
    offenseIndex = datentry["offenseIndex"]
    offentry = lp.get(offenseIndex, crime["OFFENSE_CODE_GROUP"])
    if offentry is None:
        entry = new_offense_entry(crime["OFFENSE_CODE_GROUP"], crime)
        al.add_last(entry["lstoffenses"], crime)
        lp.put(offenseIndex, crime["OFFENSE_CODE_GROUP"], entry)
    else:
        entry = offentry
        al.add_last(entry["lstoffenses"], crime)
    return datentry

def new_data_entry(crime):
    entry = {'offenseIndex': None, 'lstcrimes': None}
    entry['offenseIndex'] = lp.new_map(num_elements=30, load_factor=0.5)
    entry['lstcrimes'] = al.new_list()
    return entry

def new_offense_entry(offensegrp, crime):
    ofentry = {'offense': None, 'lstoffenses': None}
    ofentry['offense'] = offensegrp
    ofentry['lstoffenses'] = al.new_list()
    return ofentry

def crimes_size(analyzer):
    return al.size(analyzer['crimes'])

def index_height(analyzer):
    return rbt.height(analyzer["dateIndex"])

def index_size(analyzer):
    return rbt.size(analyzer["dateIndex"])

def min_key(analyzer):
    return rbt.get_min(analyzer["dateIndex"])

def max_key(analyzer):
    return rbt.get_max(analyzer["dateIndex"])

def index_height_areas(analyzer):
    return rbt.height(analyzer["areaIndex"])

def index_size_areas(analyzer):
    return rbt.size(analyzer["areaIndex"])

def min_key_areas(analyzer):
    return rbt.get_min(analyzer["areaIndex"])

def max_key_areas(analyzer):
    return rbt.get_max(analyzer["areaIndex"])

def get_crimes_by_range_area(analyzer, initialArea, finalArea):
    areas = rbt.keys(analyzer["areaIndex"], initialArea, finalArea)
    totalcrimes = 0
    for area in areas:
        lst = rbt.get(analyzer["areaIndex"], area)
        totalcrimes += al.size(lst)
    return totalcrimes

def get_crimes_by_range(analyzer, initialDate, finalDate):
    initialDate = datetime.datetime.strptime(initialDate, '%Y-%m-%d')
    finalDate = datetime.datetime.strptime(finalDate, '%Y-%m-%d')
    lst = rbt.values(analyzer["dateIndex"], initialDate.date(), finalDate.date())
    totalcrimes = 0
    for lstdate in lst:
        totalcrimes += al.size(lstdate["lstcrimes"])
    return totalcrimes

def get_crimes_by_range_code(analyzer, initialDate, offensecode):
    initialDate = datetime.datetime.strptime(initialDate, '%Y-%m-%d')
    crimedate = rbt.get(analyzer["dateIndex"], initialDate.date())
    if crimedate is not None:
        offensemap = crimedate["offenseIndex"]
        numoffenses = lp.get(offensemap, offensecode)
        if numoffenses is not None:
            return al.size(numoffenses["lstoffenses"])
    return 0