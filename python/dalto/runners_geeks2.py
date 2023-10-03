class Graph():
    def __init__(self):
        self.nodes = []
        self.ad_list = {}

    def add_node(self,node):
        self.nodes.append(node)

        self.ad_list[node] = []

    def edge(self,node1,node2):
        self.ad_list[node1].append(node2)
        self.ad_list[node2].append(node1)

    def arbol(self):

        

        pass


graph = Graph()

while True:
    cases = int(input())

    if cases > 10:
        print('no puedes ingresar mas de 10 casos, intenta otra vez')
        continue
    break

vertices_num = []
vertices = []

for i in range(cases):
    while True:    
        vertices_num.append(int(input()))

        if vertices_num > 100:
            print('no puedes ingresar mas de 100 vertices, intente otra vez')
            continue

        vertices.append(input())

        if len(vertices.split(' ')) == vertices_num*2:
            break

        print('el numero de vertices no coincide, intente otra vez')

for i in range(cases):
    #agregando nodos al grafo
    for j in range(0,vertices_num[i],2):
        graph.add_node((int(vertices[i].split(' ')[j]),int(vertices[i].split(' ')[j+1])))

    #agregando conexiones entre nodos
    for j in range(len(graph.nodes)-1):
        for k in range(j+1,len(graph.nodes)):

            distance_x = graph.nodes[j][0] - graph.nodes[k][0]
            if distance_x < 0:
                distance_x = -distance_x

            distance_y = graph.nodes[j][1] - graph.nodes[k][1]
            if distance_y < 0:
                distance_y = -distance_y
            

            distance = distance_x + distance_y

            if (distance == 1) or (distance == -1):
                graph.edge(graph.nodes[j],graph.node[k])

    #comprobando si es un arbol


