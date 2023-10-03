#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 20:17:14 2023

@author: Link
"""

#bucles

for i in range(3):
    print(i)

colors = ["verde","rosa",'rojo']

chars = ["Link","zelda",'ganon',"navi"]

#recorriendo 2 listas del mismo tamano al mismo tiempo
for color,char in zip(colors,chars):
    print(color,char)
#recorre completamente el elemento mas corto de los dos

    
# enumerate hace que color sea igual a una tupla que contenga el 
# indice y elemento del array    
for color in enumerate(colors):
    print(color)
    print(color[0],color[1])

print("////")


#segunda forma de usar enumerate
for i,color in enumerate(colors):
    print(i,color)    
#primero el indice y despues el valor    


for i in range(3):
    print(i)
else:#el else en un bucle se ejecuta al final
    # ecepto si hay un break
    print("el bucle termino")

print("////")
#diccionarios

dic = {
    "verde":"Link",
    "corona":"Zelda",
    "barba":"ganon"
    }
#interando keys
for key in dic:
    print(key)     

#interando values
for key,value in dic.items():
    print(key,value)    

# strings
string = "cadenas"
for letra in string:
    print(letra)

#bucles de una linea
     
numeros = [1,2,3,5,7,11]

numeros_por_2 = [x+1 for x in numeros]
# estructura: x for x in objeto
print(numeros_por_2)


    
    