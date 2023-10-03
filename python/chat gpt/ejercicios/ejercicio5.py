# 20/5/2023
#ejercicio 5

#funcion que comprueba si el numro es par o impar
def par(x):
    if x%2 == 0:
        return "el numero es par"
    return "el numero es impar"

try:
    num = int(input("ingrese un numero: "))
    print(par(num))
except:
    print("ingresa un numero no seas pendejo")

     
