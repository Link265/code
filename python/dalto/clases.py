#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 22:21:31 2010

@author: Link
"""

#crear una clase

class myclass():
    def __init__(self):
        self.x = 100
        self.y = 100


#heredando una clase

class two(myclass):
    def __init__(self):
        self.z = 100
    
print(two)
