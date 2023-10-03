#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 21:24:21 2010

@author: Link
"""

#paquetes 

#un paquete se para importar multiples modulos de una carpeta

#para que python lo reconosca como modulo
#la carpeta debe tener un archivo __init__.py 
#el archivo puede estar vacio
import paquete.paquete1 as p
import paquete.paquete2 as p2

p.saludar('Link')
p2.despedir('Link')







