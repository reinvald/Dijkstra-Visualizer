# text based implementation of Dijkstra's algorithm
import sys


# Node class
class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.distance = sys.maxsize
        self.parent = None

    def add_neighbor(self, neighbor, weight):
        if (neighbor not in self.neighbors):
            self.neighbors[neighbor] = weight
            print('neighbor successfully added!')

    def print_neighbors(self):
        print('printing all neighbors and their respective weights...')
        for n, w in self.neighbors.items():
            print('neighbor: ' + n + 'weight: ' + w)


# Graph class
class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, name):
        if (name not in self.graph):
            newNode = Node(name)
            self.graph[name] = newNode
        else:
            print('node ' + name + ' already exists!')

    def add_edge(self, u, v, w):
        if (u in self.graph and v in self.graph):
            self.graph[u].add_neighbor(v, w)
        else:
            print('error adding edge between ' + u + ' and ' + v +
                  '! check that both nodes exist in the graph...')

    def print_graph(self):
        print('printing graph...')
        for u, u_node in self.graph.items():
            print(u + ': ' + str(u_node.neighbors))


g = Graph()
g.add_node('hi')
g.add_node('cruck')
g.add_edge('hi', 'cruck', 7)
g.print_graph()
