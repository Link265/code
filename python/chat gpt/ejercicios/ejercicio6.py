# 20/5/2023
#ejercicio 6

    
#comprueba si un numero es divisible con otro
def divisible(x,y):
    
    if y == 0:
        return "no se puede dividir entre 0"

    if x%y == 0:
        return f"{x} es divisible entre {y}"
    
    return f"{x} es no divisible entre {y}"
 
try:
    num1= int(input("ingrese un numero: "))
    num2= int(input("ingrese otro numero: "))
    print(divisible(num1,num2))
except:
    print("ingresa un numero pendejo")
