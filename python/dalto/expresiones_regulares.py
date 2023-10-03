#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 19:51:39 2010

@author: Link
"""

#expresiones regulares

import re

texto = """hola,1. buenos dias como estas amigo mio que has hecho 32
segunda lInea de la 222 ababab oracion 7
ultima linea de esta cadena 433."""

#busca la primera palabra que coincida en la cadena
resul = re.search("linea",texto)

print(resul)
print("\n")

#busca todas las palabras que coincidan en la cadena
resul = re.findall("linea",texto,flags = re.IGNORECASE)
#con el parametro flags establecido como ignorecase 
#se ignora si la palabra esta escrita con minusculas o mayusculas
print(resul)
print("\n")

#buscando digitos numericos del 0 al 9 con \d
res = re.findall(r"\d",texto)
print(res)
print("\n")
#buscando todo en la cadena excepto digitos numericos con \D
res = re.findall(r"\D",texto)

print(res)
print("\n")

#buscando caracteres alfa numericos ("a-z" "A-Z" '0-9' "_" )
# con \w
res = re.findall(r"\w",texto)

print(res)
print("\n")

#buscando todo menos caracteres alfa numericos con \W
res = re.findall(r"\W",texto)

print(res)
print("\n")

#buscando los espacios en blanco con \s
res = re.findall(r"\s",texto)

print(res)
print("\n")

#buscando todo menos los espacios en blanco con \S
res = re.findall(r"\S",texto)

print(res)
print("\n")

#buscando los saltos de linea con \n
res = re.findall(r"\n",texto)

print(res)
print("\n")

#buscando todo menos los saltos de linea con .
res = re.findall(r".",texto)

print(res)
print("\n")

#buscando puntos .
#se debe cancelar el caracter especial con \
res = re.findall(r"\.",texto)

print(res)
print("\n")

#mostrando un string que busque un numero al que le sigue
# un punto y espacio
res = re.findall(r"\d\.\s",texto)

print(res)
print("\n")

#buscando el comienzo de una linea con "^"
#y comprobando si "hola" se encuentra la principio de una linea
res =re.findall(r"^hola",texto,flags=re.M)
#con el paramtro M logramos que busque en todas las lineas
# y no solo en la primera

print(res)
print("\n")

#buscando el final de una linea con "$"
#y comprobando si " 3" se encuentra la final de una linea
res =re.findall(r" 7$",texto,flags=re.M)
#es necesario colocar $ al final
#con el paramtro M logramos que busque en todas las lineas
# y no solo en la primera

print(res)
print("\n")

#busca el caracter indicado pero que sea que se repita 
#cierta cantidad de veces seguidas
res = re.findall(r"\d{2}",texto)
# buscando 2 valores numericos juntos en la cadena

print(res)
print("\n")

#busca el caracter indicado pero que sea que se repita 
#cierta cantidad de veces seguidas
#indicando el numero maximo y el minimo
res = re.findall(r"\d{1,4}",texto)
# buscando entre 1 y 4 valores numericos juntos en la cadena
print(res)
print("\n")

# buscando dos caracteres juntos
# y que se repitan entre 2 y 4 veces
res = re.findall(r"(ab){2,4}",texto)
print(res)
print("\n")

# buscando dos caracteres juntos
# y que se repitan entre 2 y 4 veces
# puede ser que los caracteres se encuentren por separado y
# devuelva "aa" o "bb"
res = re.findall(r"[ab]{2,4}",texto)
print(res)
print("\n")

# buscando una cosa o la otra
res = re.findall(r"a|b",texto)
print(res)
print("\n")

#remplazar valores de la cadena

# nueva_cadena = re.sub(parte que se va a remplazar,remplazo,cadena)

#con * comprobamos si un valor se repite mas de una vez en
# la cadena

# res = re.findall("a*") # comprueba si a se repite mas de una vez


