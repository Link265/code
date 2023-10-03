#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 19:50:59 2010

@author: Link
"""

def p(a):
    print(a)

#crear listas de manera alternariva
lista = list([1,2,False,True])

p(len(lista))#longitud

lista.append("hola")#agrega un elemento a la lista
p(lista)

lista.insert(-1,"adios")#agrega un elmento a la lista en el indice
# especificado
# este caso "adios" se coloca en la penultima posicion en vez
# de la ultima
p(lista)

lista.extend(["Zelda","Link","Zelda","Ganon"])#agrega elementos a la lista
#con otra lista 
p(lista)

lista.pop(-1)#elimina elementos de una lista con el indice
p(lista)

lista.remove("Zelda")#elimina elementos de la lista con el valor
p(lista)

lista_de_numeros = [3,7,2,5,8,3]

lista_de_numeros.sort()#organiza lista de numeros
#lista.sort(reverse=True) organiza la cadena al revez
p(lista_de_numeros)

lista.reverse()
#invierte los elementos de una lista
p(lista)

lista.clear()#borra los elementos de la lista
p(lista)

p({3,3,5})

