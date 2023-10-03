#2023-06-05 08:38:57

lista = input("ingrese una lista de numeros separados por coma: ").split(",")

lista = [int(x) for x in lista]

lista2 = list(filter(lambda x: not x%2,lista))

print(lista2)


