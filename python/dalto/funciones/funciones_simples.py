#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 20:08:12 2010

@author: Link
"""

#funciones simples

#parametro args
#el asterisco comple la funcion de convertir elementos los del parametro
# en una 
# tupla
def p(*num):
    print(num)
    print(*num)#transforma listas en valores separados y viceversa
# si se nesecita usar mas parametros el que lleve asterisco debe ir al
#final

p(1,2,3,4)

#forzar parametros

def fo(color,numero):
    print(f"color:{color},numero:{numero}")
#permite asignarlos correctamente a pesar que esten desorganizados
fo(numero = 90,color = "rojo")       
# al forzar alguno de los parametros, entonces se deben forzar todos
# lo demas   

#parametros por defecto
def defecto(num="no se paso ningun numero"):
    print(num)
    
defecto()





