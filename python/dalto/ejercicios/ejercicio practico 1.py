#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 20:25:40 2010

@author: Link
"""

#ejercicio practico 1

horas= {
    "este curso":1.5,
    "curso corto":2.5,
    "curso promedio":4,
    "curso largo":7
}

for i in horas:
    if i == "este curso" :
       continue
   
    relacion = int(100 - (horas["este curso"] / horas[i]) * 100) 
    print(f"este curso es un {relacion}% mas rapido que el {i}")

crudo_dalto = 3.5
crudo_promedio = 5

porcentaje_crudo = int(100 - ( horas["este curso"] / crudo_dalto) *100)

print(f"el crudo de dalto es el {porcentaje_crudo}% del material final")

porcentaje_crudo = 100 - ( horas["curso promedio"] / crudo_promedio) *100

print(f"el crudo promedio es el {porcentaje_crudo}% del material final")

este_vs_promedio = int((horas["curso promedio"] / horas["este curso"])*10)

print(f"ver 10 horas de este curso equivale a ver {este_vs_promedio} horas de otros cursos")

promedio_vs_este = horas["este curso"]/ horas["curso promedio"] * 10

print(f"ver 10 horas de otros cursos equivale a ver {promedio_vs_este} horas de este")
