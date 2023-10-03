#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 20:28:10 2010

@author: Link
"""

#archivos csv 1

#importando libreria para leer csv
import csv as c


with open("archivo2.csv") as a:
    
    #leyendo archivo
    b = c.reader(a)
    
    #mostrando archivo    
    for i in b:
        print(i)





