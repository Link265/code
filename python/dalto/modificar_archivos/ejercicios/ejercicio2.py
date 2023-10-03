#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 23:02:34 2010

@author: Link
"""

#ejercicio 2

import pandas as pd

#cambiar el tipo de dato de una columna

a = pd.read_csv("archivo2.csv")
a2 = pd.read_csv("archivo2.csv")
print(a)

#convirtiendo los enteros a strings
#    a["edad"] = a["edad"].astype(str)

print(type(a['edad'][0]))

#remplazo

#    a["nombre"].replace("Ganon","Ganondorf",inplace=True)

print(a)
print("\n")
#eliminando filas con datos faltantes
a = a.dropna()
# para eliminar columnas vacias se utiliza a = a.dropna(axis=1)

print(a)




print("\n")

#eliminando filas con datos repetidos
a = a.drop_duplicates()

print(a)

#creando csv con el archivo modificado
a.to_csv("nuevo_csv.csv")


