#2023-05-26 09:07:48
#ejercicio 16

numeros = input("ingrerse un factorial para calcularlo: ")
numeros = int(numeros)



def factorial(x):
    fact =1
    for i in range(1,x+1):
        fact *= i
    return fact
print(factorial(numeros))