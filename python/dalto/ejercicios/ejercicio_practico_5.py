#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 20:02:01 2010

@author: Link
"""

#fibonacci

def fibonacci(x):
    fib = [1]
    if x >= 2:
        fib = [1,1]
   #se le resta 1 a x para compenzar que el array ya tiene a [1,1]
    for i in range(1,x-1):
        fib.append(fib[i-1]+fib[i])

    return(fib)

# c = int(input("cuantos numeros de la sucesion de fibonacci quieres?: "))

def fibonacci_2(a):
    if a == 0:
        return 1
    if a == 1:
        return 1
    return fibonacci_2(a - 1) + fibonacci_2(a - 2)

for i in range(10):
    print(fibonacci_2(i))


