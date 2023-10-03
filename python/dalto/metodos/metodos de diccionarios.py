#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 23:03:50 2010

@author: Link
"""

diccionario = {
    "nombre":"Link",
    "ropa":"verde",
    "hogar":"hyrule",        
    "items":2
}

#devuelve un objeto dict_item
#dict_item es un objeto iterable
print(diccionario.keys())
#muestra las keys de un diccionario
#puede servir para iterar

print(diccionario.get("ropa"))
#no da error en caso de no encontrar el valor
#retorna el valor de la clave especifacada

diccionario.pop("hogar")
print(diccionario)
#elimina uno o mas elementos deseados por key

print(diccionario.items())
#retorna un array de tuplas 

diccionario.clear()
print(diccionario)#elimina los todos los elementos