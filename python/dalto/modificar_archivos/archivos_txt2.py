#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 22:50:12 2010

@author: Link
"""

#archivos txt 2 
def fun():
    with open("archivo1.txt",encoding="UTF-8") as a:
        print(a.read())
        #se cierra automaticamente el archivo

# sobreescribiendo el archivo
# colocando el parametro "w"
with open("archivo1.txt","w",encoding="UTF-8") as a:
    a.write("lo que sea")
   
fun()

with open("archivo1.txt","w",encoding="UTF-8") as a:
    #escribe lineas
    # se coloca \n al final de cada linea
    a.writelines(["lo que sea\n","papas\n","peras"])
    
fun()    

#con el paramtro a estamos anadiendo sin borrar lo anterior    
with open("archivo1.txt","a",encoding="UTF-8") as a:
    
    #anadimos 5 lineas
    a.writelines([f"\n -linea {i}" for i in range (5)])
    
fun()    
    

    
    
    