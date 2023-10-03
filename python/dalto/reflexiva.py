# 12/5/2023
# 8:26 AM

#comprobar de que tipo es una relacion

a = input("ingrese la relacion con tuplas separadas por espacios: ").split(" ")

class Comprobar():
    def __init__(self,relacion):
        self.relacion = relacion

        #separando elementos de la relacion
        elem = set()
        for i in self.relacion:
            coma = i.index(",")
            elem.add(i[1:coma])
            elem.add(i[coma+1:-1])
        self.my_elements = list(elem)
    
    def reflexiva(self):
        for i in self.my_elements:
            
            if f"({i},{i})" not in self.relacion:
                return "no es una relacion reflexiva"
        self.es_reflexiva = True   
        return "es una relacion reflexiva"    
            

con = Comprobar(a)

print(con.reflexiva())


