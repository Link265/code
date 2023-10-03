# 20/5/2023
#ejercicio 9

def mayor_de_edad(x):
    if x >= 18:
        return "eres mayor de edad"
    return "eres menor de edad" 

edad = int(input("ingresa tu edad: "))

print(mayor_de_edad(edad))
