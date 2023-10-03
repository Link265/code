#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 21:41:57 2010

@author: Link
"""

#filter

def par(x):
    if x%2 == 0:
        return True

# filter crea un bucle con la funcion del 
# primer parametro utilizando los valores de la lista del
# segundo parametro
fil = list(filter(par,[0,1,2,3,4,5,6,7,8,9,10]))

print(fil)

#con lambda

fil = list(filter(lambda x:x%2 == 0,[0,1,2,3,4,5,6,7,8,9,10]))

print(fil)
