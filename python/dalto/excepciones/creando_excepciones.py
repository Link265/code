#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 19:46:24 2010

@author: Link
"""

#creando otra clase de excepcion

class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"se ha detectado el siguiente error : {err}")


#la palabra raise lanza una excepcion seleccionada alante de 
# la palabra
    
raise MiExcepcion("excepcion ha ocurrido")
    
