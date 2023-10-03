from sympy import *
#indefinidas
x = symbols('x')
f = "1/(x+x**2024)"
res = integrate(f)
print(res)

#definida
f = x**2+1
res = integrate(f,(x,0,1))
print(res)