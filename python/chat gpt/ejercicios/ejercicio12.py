# 21/5/2023
#ejercicio 11

cadena = input("ingrese una lista de numeros separados por coma")
cadena = cadena.split(',')

numeros = [int(x) for x in cadena]

def sumar(numbers):
    resultado = 0
    for x in numbers:
        resultado += x 
    return resultado

print(sumar(numeros))

#terminado 24/5/2023