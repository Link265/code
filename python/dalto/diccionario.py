#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 19:46:06 2023

@author: Link
"""

#diccionarios

#otra forma de crear diccionarios
dic1 = dict(hola = "a",b = "d")

print(dic1)

array = frozenset({'a','b'})
#las listas no pueden ser  keys por lo que se usa frozen set
dic2 = {array:"verde"}

print(dic2)

#el primer parametro es una lista de keys y el segundo es el valor por
# defecto
dic3 = dict.fromkeys(['a','b'],"Link")
#cuando no se pone un segundo valor, el valor por defecto es 'none'

print(dic3)