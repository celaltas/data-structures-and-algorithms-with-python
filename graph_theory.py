
# Adjacency Matrix representation in Python

class Graph:
    def __init__(self, size):
        self.adjacency_matrix = []
        for i in range(size):
            self.adjacency_matrix.append([0]*size)
        self.size = size

    def add_edge(self, v1, v2):
        if v1 != v2:
            self.adjacency_matrix[v1][v2] = 1
            self.adjacency_matrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if self.adjacency_matrix[v1][v2] != 0:
            self.adjacency_matrix[v1][v2] = 0
            self.adjacency_matrix[v2][v1] = 0

    def __len__(self):
        return self.size

    def show_graph(self):
        for row in self.adjacency_matrix:
            for val in row:
                print(val, end="")
            print("\n")


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)

g.show_graph()
graph = Graph(6)
print(graph.adjacency_matrix)


# Adjascency List representation in Python


class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(1, 2)

graph.print_agraph()
