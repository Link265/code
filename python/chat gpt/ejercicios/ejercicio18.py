#2023-05-27 07:27:31
# ejercicio 18

numeros = input("ingrese una lista de numeros separados por coma: ").split(",")
numeros = [int(x) for x in numeros]

numeros.sort()

def mediana(x):
    longitud = len(x)
    if longitud%2 == 0:
        return (x[(longitud // 2)-1] + x[longitud // 2])//2
    return x[longitud //2]
    

print(mediana(numeros))
