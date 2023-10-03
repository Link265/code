#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 21:21:39 2010

@author: Link
"""

#manejar excepciones

def sumar():
    while True:
        a = input("ingresa un numero: ")
        b = input("ingresa otro numero: ")
         
        #try prueba si existe un excepcion en el codigo
        #si no la encuentra se ejecuta normalmente
        #si la encuentra salta a except
        try:
            res = int(a) + int(b)    
            
        #se ejecuta solamente SI encuentra una excepcion    
        except Exception as e:
            print(f"""no seas pendejo pon un numero!""")
            print(f"error:{e}")
            print(f"error de tipo:{type(e)}")
            
        #else se ejecuta solamente si NO encuentra 
        #una excepcion
        else:
            break
        
        #el finally siempre se va a ejecutar independientemente
        #de si encontro una excepcion o no
        finally:
            print("esto se ejecuta siempre")
        
    return res

print(sumar())
