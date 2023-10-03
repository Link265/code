#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 20:32:07 2023

@author: Link
"""

#teoria de conjuntos

set1 = {'a','b','c','d','e','f'}
set2 = {'a','b','c','d','e','f'}

result = set2.issubset(set1)
# .issubset() comprueba si el conjunto es un subconjunto del parametro

result2 = set2 <= set1
# hace lo mismo que que el metodo anterior

print(result,result2)

result = set1.issuperset(set2)
# .issubset() comprueba si el conjunto es un superconjunto del parametro

result2 = set1 >= set2
# hace lo mismo que que el metodo anterior

print(result,result2)

result = set1.isdisjoint(set2)
#retorna false si al menos uno de los elementos es igual

print(result)


if set1 == set2: #& set2 >= set1:
    print('los 2 conjuntos son iguales')    
