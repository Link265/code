#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 20:43:05 2010

@author: Link
"""

#parametro args (*)

#convierte listas/tuplas/sets en parametros separados
print(*[4,2,56,2,2])

# en el caso de los diccionarios, se retorna las keys separadas
print(*{"2":4,"3":2})

#convierte argumentos separados en tuplas
def ejemplo(*numeros):
    print(numeros)
ejemplo(3,4,5,6,6)
