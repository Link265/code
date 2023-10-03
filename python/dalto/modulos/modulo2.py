#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 21:19:19 2010

@author: Link
"""

#modulo2

import modulo1 as m1 #importando modulo 1 y renombrandolo a m1
from modulo1 import cargar,descargar #importando solamente las funciones
# que necesitamos en lugar del modulo completo

from modulo1 import* #importando todas las funciones

m1.cargar()#namespace

descargar()
