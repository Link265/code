#2023-06-07 09:51:19

lista1 = input("ingrese una lista con elementos esparados por comas: ").split(",")
lista2 = input("ingrese otra lista con elementos esparados por comas: ").split(",")

def elementos_repetidos(li1,li2):
    li3 = list()
    for i,x in enumerate(li1):
        for j,y in enumerate(li2):
            if x == y:
                li3.append(x)

    if len(li3) > 0:
        return li3            
    return "no tienen elementos repetidos"

print(elementos_repetidos(lista1,lista2))

