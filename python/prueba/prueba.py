print("hola mundo en python otra vez")

with open("C:\\Users\\Fabian tovar\\Desktop\\file.txt","a") as a:
    #a.write(" hola otra vez")
    a.close

print("me encanta identar") 

def funcion(a,x):
    print(f"{a} y {x}")

funcion(2,3)    

variable = "no importa el maldito tipo de las variables jajajajajajjaja"

letra = 3
numero = 'a'

funcionlambda = lambda x: x*2

print(f"{funcionlambda(3)}")

cadena = "perro gato loro lobo".split(' ')
print(cadena)

array_de_todos_los_numeros_del_1_al_100 = [x for x in range(1,101)]

print(array_de_todos_los_numeros_del_1_al_100)

puros_pares_del_1_al_100 = filter(lambda x:not x%2,array_de_todos_los_numeros_del_1_al_100)

print(list(puros_pares_del_1_al_100))

