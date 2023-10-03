class Graph():
    def __init__(self):
        self.nodes = []
        self.ad_list = {}
        self.visitados = []

    def add_node(self,node):
        if node not in self.nodes:
            self.nodes.append(node)
            self.ad_list[node] = []

    def add_edge(self,node1,node2):
        if node2 not in self.ad_list[node1]:
            self.ad_list[node1].append(node2)
            self.ad_list[node2].append(node1)

    def recorrer(self,nodo_inicial):

        visitas = 0
        for i in self.ad_list[nodo_inicial]:
            if i not in self.visitados:
                self.visitados.append(i)
                visitas += self.recorrer(i)
            else:
                visitas += 1

        return visitas

    def reset_rrecorrida(self):
        self.visitados = [] 

    def is_tree(self):
        if self.recorrer(self.nodes[0]) > len(self.nodes):
            return False
        if len(self.visitados) < len(self.nodes):
            return False
        
        return True
    
    def reset(self):
        self.nodes = []
        self.ad_list = {}
        self.visitados = []

def valor_absoluto(x):
    if x < 0:
        x = -x
    return x


while True:
    casos = int(input("ingrese el numero de casos: "))
    if (casos > 0) and (casos < 10):
        break
    print("el numero no puede ser mayor de 10 ni menor de 0")

vertices = []
vertices_num = []

for i in range(casos):
    while True:
        vertices_num.append(int(input('cuantos vertices va a ingresar?: ')))
        if (vertices_num[i] > 100) or (vertices_num[i] < 0):
            print("el numero debe estar entre 100 y 1")
            continue



        vertices.append(input("ingrese los vertices: ").split(" "))

        try:
            vertices[i] = [int(x) for x in vertices[i]]
        except:
            print("error ingreso un valor no convertible a entero")
            continue    

        error = False
        for j in vertices[i]:
            if (j < -100) or (j > 100):
                error = True
                break
        if error:
            print("los vertices deben estar entre -100 y 100")
            continue            


        if vertices_num[i] == len(vertices[i])/2:
            break
        print('el numero de vertices no coincide')   

graph = Graph()

for i in range(casos):

    for j in range(0,len(vertices[i]),2):
        graph.add_node((vertices[i][j],vertices[i][j+1]))

    for j in range(len(graph.nodes)-1):
        for k in range(j+1,len(graph.nodes)):

            valor = valor_absoluto(graph.nodes[k][0] - graph.nodes[j][0]) + valor_absoluto(graph.nodes[k][1] - graph.nodes[j][1])
            if valor == 1:
                graph.add_edge(graph.nodes[k],graph.nodes[j])
            print(valor)    

    if graph.is_tree():
        print("Es un arbol")
    else:
        print("no es un arbol")

    print(graph.nodes)
    print(graph.ad_list)

    graph.reset()        

                


