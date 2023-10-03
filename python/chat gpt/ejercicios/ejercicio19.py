#2023-05-27 07:57:07
# ejercicio 19 


lista1 = input("ingrese una lista de numeros separados por coma: ").split(",")

lista2 = input("ingrese otra  lista de numeros separados por coma: ").split(",")

def iguales(x,y):
    for i,j in zip(x,y):
        if i != j:
            return "no son iguales"
    return "son iguales"    

print(iguales(lista1,lista2))
