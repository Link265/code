#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 21:15:18 2010

@author: Link
"""

#usando factoriales para calcular euler

#el valor inicial del factorial
factorial = 1

#el valor inicial de la suma
suma = 1

#define el valor maximo del factorial
maximo = 20

for i in range(1,maximo):
    
    #el valor del factorial va a ir aumentando con respecto a i
    # es decir sera 1! despues 2!,3! hasta llegar (maximo - 1)!    
    factorial = i*factorial
    
    #realiza la suma para calcular el numero de euler
    suma = suma + 1/factorial
    #NOTA: e = 1/1! + 1/2! + 1/3! + ... + 1/n!


#mostrando el valor final de la suma la cual tiene como resultado e
print(suma)


