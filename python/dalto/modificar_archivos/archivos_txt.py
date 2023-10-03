#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 22:03:04 2010

@author: Link
"""

# archivos txt

a = open("archivo1.txt",encoding="UTF-8")
#abriendo el archivo y codificandolo en utf-8

print(a)#mostrando el objeto del archivo

# print(a.read())#leyendo el archivo
# una vez que se lee el archivo, no se puede volver a leer


#leyendo linea por linea y retorna un array 
lineas = a.readlines()
# .readlines(10) puede leer 10 letras o palabras entren en el rango

print(lineas)

a.close()



