# text based implementation of Dijkstra's algorithm
import sys


# Node class
class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight):
        if (neighbor not in self.neighbors):
            self.neighbors[neighbor] = weight
        else:
            print(neighbor + ' is already a neighbor of ' + self.name + '!')

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

    def Dijkstra(self, s):

        # check that starting node exists in the graph
        if (s not in self.graph):
            print('node with name ' + s + ' does not exist in the graph!')
            return

        distances = {n: sys.maxsize for n in self.graph}
        parents = {n: None for n in self.graph}
        unvisited = self.graph.copy()

        # init distance of source node
        distances[s] = 0

        while unvisited:

            # extract node with minimum distance from s
            current_node = min(unvisited, key=lambda n: distances[n])

            # iterate through adjacent nodes of current node, see if shortest path can be improved, update neighbor
            for n, w in self.graph[current_node].neighbors.items():
                if (distances[n] > distances[current_node] + w):
                    distances[n] = distances[current_node] + w
                    parents[n] = current_node

            # relax node, remove it from further consideration
            unvisited.pop(current_node)

        for n, w in distances.items():
            print('shortest distance from ' + s + ' to ' + n + ': ' + str(w))


# build and print a sample graph
g = Graph()
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 3)
g.add_edge('C', 'B', 1)
g.add_edge('B', 'D', 2)
g.add_edge('B', 'E', 3)
g.add_edge('C', 'D', 4)
g.add_edge('C', 'E', 5)
g.add_edge('E', 'D', 1)
g.Dijkstra('A')

# shortest paths: A,A=0, A,B=3, A,C=2, A,D=5, A,E=6
