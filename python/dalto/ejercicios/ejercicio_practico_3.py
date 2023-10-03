#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 22:25:44 2010

@author: Link
"""

estudiantes_num = int(input("cuantos estudiantes son?: "))

estudiantes = [{"nombre":input(f"nombre del estudiante numero {x} : "),"edad":input(f"cual se la edad del estudiante numero {x} : ")} for x in range(1,estudiantes_num+1)]

# edades = [int(x["edad"]) for x in estudiantes]

# maestro = max(edades)

# def a():
#     for i,element in enumerate(estudiantes):
#         print(i,element,maestro)
#         if str(maestro) == element["edad"]:
#             return i

# maestro = a()
        
# print(f"""el maestro sera {estudiantes[maestro]["nombre"]}""") 

estudiantes.sort(key=lambda x:x["edad"])
     
print(f"""el maestro sera {estudiantes[-1]["nombre"]}""")

print(f"""el asistente sera {estudiantes[0]["nombre"]}""")


