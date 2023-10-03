a = {
    "python":"programacion",
    "java":"clases"
}
# print(type(a));

#print(dir(a))#muestra los metodos aplicables 
#de una variable

s = "hOLa como estas"

print(s.upper())#convierte a mayusculas

print(s.lower())#convierte a minusculas

print(s.capitalize())#primera letra mayusculas

print(s.find("a"))#retorna la posicion del carater
# deseado y si no esta retorna -1

# s.index() funciona igual pero da error si no 
# encuentra el caracter

print(s.isnumeric())#determina si es un caracter 
# numerico

#print(s.isalfa())# alfanumerico

print(s.count("h"))#retorna el numero de veces 
# que encuentre el parametro

print(len(s))#logitud

print(s.startswith("h"))

print(s.endswith("a"))

print(s.replace("estas","te encuentras"))
#replaza un pedazo por otro pedazo

print(s.split(" "))#separa la cadena en una lista

