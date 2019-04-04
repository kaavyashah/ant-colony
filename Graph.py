class Node:
    def __init__(self, i):
        '''
            Right now, i is any identifier for the node.
            Later, these will hold the information for each attractions.
        '''
        self.i = i

class Graph:

    def __init__(self, nodes, edges):
        '''
            nodes: a list of nodes
            edges: a 2D array where edges[i][j] = dist(i, j), the distance from node i to node j
        '''
        self.nodes = nodes
        self.edges = edges

    def get_distance(self, n1, n2):
        '''
            Returns the edge distance between two nodes.
        '''
        return self.edges[n1][n2]
