# 20/5/2023
#ejercicio 2


def multiplicar(x,y):
    return f"la multiplicacion de los 2 numeros es {x*y}"

def sumar(x,y):
    return f"la suma de los 2 numeros es {x+y}"

def restar(x,y):
    return f"la resta de los 2 numero es {x-y}"

def division(x,y):
    if y == 0:
        return "la division es invalida"

    return f"la division es {x/y}" 

num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese otro numero: "))

#muestra el resultado de la suma,reta,multiplicacion y division
print("\n",multiplicar(num1,num2),"\n",sumar(num1,num2),"\n",restar(num1,num2),"\n",division(num1,num2))
