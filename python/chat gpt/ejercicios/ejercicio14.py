
# 26/5/2023
#ejercicio 14

lista = input("ingrese una lista de numeros separados por coma: ").split(",")

numeros = [int(x) for x in lista]

def organizacion(x):
    original = x.copy( )
    x.sort(reverse=True)
    for i,j in zip(original,x):
        
        if i == j:
           continue
        return "no esta ordenado"
    return "esta ordenado"
print(organizacion(numeros))
