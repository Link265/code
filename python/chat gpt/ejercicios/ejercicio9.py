# 20/5/2023
#ejercicio 9

num = int(input("ingrese un numero: "))

def signo_del_numero(x):
    if x>0:
        return f"{x} es positivo"
    if x<0:
        return f"{x} es negativo"
    
    return f"{x} es igual a 0"

print(signo_del_numero(num))