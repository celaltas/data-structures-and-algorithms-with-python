
# Adjacency Matrix representation in Python

import re
from unicodedata import name


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


# DFS algorithm in Python


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for item in graph[start]-visited:
        dfs(graph, item, visited)
    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

print(dfs(graph, '0'))


"""

Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

"""


def search(graph, start, end):
    if start == end:
        return True
    visited = set()
    visited.add(start)
    for item in graph[start]-visited:
        if item == end:
            return True
        return False


print(search(graph, "0", "3"))


"""

Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error.
4.7
EXAMPLE
Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c


"""


class Project:

    def __init__(self, name):
        self.name = name
        self.dependencies = 0
        self.children = []

    def get_name(self):
        return self.name

    def increment_dependencies(self):
        self.dependencies = +1

    def decrement_dependencies(self):
        self.dependencies = -1

    def get_children(self):
        return self.children

    def get_number_dependencies(self):
        return self.dependencies

    def add_neighbor(self, project):
        if project not in self.children:
            self.children.append(project)
            self.increment_dependencies()


class Graph:

    def __init__(self):
        self.nodes = []
        self.hash_map = {}

    def get_or_create(self, project_name):
        if project_name not in self.hash_map.keys():
            node = Project(project_name)
            self.nodes.append(node)
            self.hash_map(name=node)
        return self.hash_map.get(project_name)

    def add_edge(self, start_name, end_name):
        start = self.get_or_create(start_name)
        end = self.get_or_create(end_name)
        start.add_neighbor(end)

    def get_nodes(self):
        return self.nodes

    def get_nodes(self):
        return self.nodes


def find_build_order(projects, dependencies):
    graph = build_graph(projects, dependencies)
    return order_projects(graph.get_nodes())


def build_graph(projects, dependencies):
    graph = Graph()
    for project in projects:
        graph.get_or_create(project)

    for dependency in dependencies:
        first = dependency[0]
        second = dependency[1]
        graph.add_edge(first, second)

    return graph

def add_non_dependent(order, projects, offset):
    for project in projects:
        if project.get_number_dependencies() == 0:
            order[offset] = project
            offset +=1
    return offset

def order_projects(projects):
    order = []
    end_of_list = add_non_dependent(order,projects,0)
    to_be_processed = 0
    while to_be_processed<len(order):
        current_project = order[to_be_processed]
        if current_project is None:
            return None
        children = current_project.get_children
        for child in children:
            child.decrement_dependencies()
        end_of_list = add_non_dependent(order,children,end_of_list)
        to_be_processed +=1
    return order