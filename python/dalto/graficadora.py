import matplotlib.pyplot as pm
import numpy as np

# x = np.linspace(0,2*np.pi,100)
# y = np.sin(x)
 
# a = np.linspace(-5,5,50)
# b = np.cos(a)
 
# pm.plot(a,b)
# pm.xlabel("x")
# pm.ylabel("y")
# pm.title("grafico")
# pm.show


def graficar(x,y):
    pm.plot(x,y)
    pm.show

def valores_de_y():
    x = np.linspace(-5,5,50)
    y = input("ingrese una formula: ")
    
    y = eval(y)
    
    graficar(x,y)



valores_de_y()    
    