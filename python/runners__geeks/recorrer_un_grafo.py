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


gra = Graph()

gra.add_node(1)
gra.add_node(2)
gra.add_node(3)
gra.add_node(4)
gra.add_node(5)
gra.add_node(6)
gra.add_node(7)

gra.add_edge(1,2)
gra.add_edge(1,3)
gra.add_edge(2,4)
gra.add_edge(2,5)
gra.add_edge(3,6)
gra.add_edge(3,7)

print(gra.is_tree())

for i in gra.nodes:
    print(f'{i} relaciones:{gra.ad_list[i]}')




