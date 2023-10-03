# 21/5/2023
#ejercicio 11

cadena = input("ingrese una lista de numeros separados por comas: ")

#separando lo numeros de cadena en una lista usando split()
cadena = cadena.split(",")

#creando una nueva cadena pero cambiando el tipo de dato a entero
numeros = [int(x) for x in cadena]

#funcion que retorna el numero mayor de una cadena comparando los elementos
def numero_mayor(x):
    mayor = x[0]
    for num in x:    
        if mayor < num:
            mayor = num
    return mayor

#funcion que retorna el numero mayor ordenando al lista de menor a mayor
# y despues retornando el ultimo elemento 
def ordenacion(x):
    x.sort()
    return x[-1]

print(f"el numero mas grande es {ordenacion(numeros)}")