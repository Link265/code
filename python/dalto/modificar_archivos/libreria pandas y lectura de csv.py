#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 21:03:40 2010

@author: Link
"""

#libreria pandas y lectura de csv

import pandas as pd

#obteniendo el data frame
a = pd.read_csv("archivo2.csv")
a2 = pd.read_csv("archivo2.csv")

#leyendo data frame
#    print(a)

#mostrando datos de la columna nombre
#     print(a["nombre"])

#cambiando el nombre de las columnas
# y el encabezado anterior pasa a ser un elemento
#    a = pd.read_csv("archivo2.csv",names=["name","clothes","age"])

print("\n")

#ordenando valores del por age
print(a.sort_values("edad"))
print("\n")

#ordenandolos al revez
print(a.sort_values("edad",ascending=False))
print("\n")

#concatenando data frames
print(pd.concat([a,a2]))
print("\n")

#accediendo al archivo desde el encabezado
print(a.head(2))#muestra 2 filas segun el parametro

print("\n")

#accediendo al archivo desde abajo
print(a.tail(2))#muestra 2 filas
print("\n")

#mostando el numero de filas y de columnas
print(a.shape)

#filas
print(a.shape[0])

#columnas
print(a.shape[1])
print("\n")

#mostrando informacion estadistica del data frame
print(a.describe())
print("\n")

#accediendo a un elemento especifico

#con loc
print(a.loc[1,"edad"])
# en la fila se coloca un entero y en la columna un string

#con iloc
print(a.iloc[0,2])
# se accede por medio de los indices sin necesidad de colocar el 
# nombre de la columna
print("\n")

#mostrando tadas las filas de la colomna 1
print(a.iloc[:,1])

#mostrando filas con edades mayores a 30
print(a.loc[a["edad"]<30,:])
#no se puede hacer con iloc








