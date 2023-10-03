# tuplas
a = (True,"hola",43,False,"ls")
# las tuplas no se pueden modificar
# se pueden crear tuplas de diferentes maneras
tupla2 = "dato1","dato2"
# tambien de un solo dato
tupla3 = "dato3",

# listas
b = [True,"hola",43,False,"ls"]
# se parecen a los array pero no son lo mismo
# se puenden accerder a los valores mediante slicing
print(b[1:3])
# muestra desde el indice 1 hasta el 2 se decir 3 - 1

# set
c = {True,"Link","zelda",True}
# aunque repitas valores, solo se mostranran una sola vez
# los datos estan desorganizados
# no se puede utilizar indices " c[3] " por ejemplo
set1 = frozenset({'dato1','dato2',('dato3','dato4')})
#frozenset crea un conjunto inmutable lo que nos permite
# anadirlo a otro conjunto
set2 = {'verde',True,set1}


# diccionario
d = {
    'python':3,
    'java':4
}

print(set1)
