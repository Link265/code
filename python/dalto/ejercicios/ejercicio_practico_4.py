#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 19:39:00 2010

@author: Link
"""

#ejercicio practico 3

def calcular_primos(x):

    for i in range(2,x//2 +1):
        if x%i == 0:return False  #si el resto de la division de x/i da 0 entonces no sera primo
    return True #si se termino el bucle sin cumplir la condicion entonces es primo

def mostrar_primos(x):
    print(list(filter(calcular_primos,range(1,x))))

primos_cantidad = int(input("hasta que numero quieres buscar primos?"))

mostrar_primos(primos_cantidad)
