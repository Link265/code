#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 22:30:34 2010

@author: Link
"""

# ejercicio 1

nombres = ['Pedro','mario','Luigi','peach']
apellidos = ["Alvarado","Bros","Bros",'Champinon']


with open("archivo.txt","w") as a:
    
    for n,ap in zip(nombres,apellidos):
        a.write(f"{n} {ap} \n")
    

with open("archivo.txt") as a:
    
    print(a.read())




