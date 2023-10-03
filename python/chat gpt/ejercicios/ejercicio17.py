# 2023-05-27 07:03:29
# ejercicio 17

cadena = input("ingrese una lista de numeros separados por coma: ")

#dividiendo la cadena en diferentes elementos de un array
numeros = cadena.split(",")
# y convirtiendola en enteros

numeros =  [int(x) for x in numeros]

def rep(x):
    for i in x:
        if x.count(i) > 1:
            return "hay numeros repetidos"
    return "no hay numeros repetidos"

print(rep(numeros))
