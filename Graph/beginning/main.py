class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 not in self.adj_list.keys() or v2 not in self.adj_list.keys():
            return False
        if v2 in self.adj_list[v1] or v1 in self.adj_list[v2]:
            return False
        self.adj_list[v1].append(v2)    
        self.adj_list[v2].append(v1)
        return True    
    
    def remove_edge(self, v1, v2):
        if v1 not in self.adj_list.keys() or v2 not in self.adj_list.keys():
            return False
        if v2 not in self.adj_list[v1] or v1 not in self.adj_list[v2]:
            return False
        self.adj_list[v1].remove(v2)    
        self.adj_list[v2].remove(v1)
        return True 
    def remove_vertex(self, v):
        if v not in self.adj_list.keys():
            return False
        del self.adj_list[v]
        for item in self.adj_list:
            if v in self.adj_list[item]:
                self.adj_list[item].remove(v)
        return True
    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex} : {self.adj_list[vertex]}")
            
my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_edge("B", "A")
my_graph.remove_vertex("A")
my_graph.print_graph()