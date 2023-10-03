#2023-05-27 08:09:09
#ejercicio 20

cadena = input("ingrese una cadena de texto: ")

def solo_letras(x):
    if x.isalpha():
        return "solamente tiene letras"
    return "tiene mas que solamente letras"

print(solo_letras(cadena))