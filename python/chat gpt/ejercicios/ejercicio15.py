# 26/5/2023
#ejercicio 15

cadena = input("introduzca una cadena: ")

def polindromo(x):

    invertida = x[::-1]
    if  x == invertida:
        return "si es un polindromo"
    return "no es un polindromo"

print(polindromo(cadena))

