 #2023-06-01 09:00:56
#ejercicio 1 intermedio (listas)

import numpy as np

lista = list()
while True:
    num = input("ingrese un numero para la lista o fin para terminar: ")
    if num == "fin":
        break
    try:
        num = int(num)
        lista.append(num)
    except:
        print("eso no es un numero")

def promedio(x):
    #funcion que calcula el promedio de una lista
    pro = np.mean(x)
    return f"el promedio es {pro}"

def desviacion(x):
    #funcion que calcula la desviacion estandar de una lista
    des =  np.std(x)
    return f"la desviacion estandar es {des}"

print(f"""la suma de los valores es: {sum(lista)}
{promedio(lista)}
{desviacion(lista)}""")









