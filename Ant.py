class Ant:
    def __init__(self, starting_node):
        self.trail = []
        # self.visited = {}
        self.trail.append(starting_node)

    def visit_node(self, node):
        self.trail.append(node)
        # self.visited.append()

    def has_visited(self, node):
        # return self.visited[node]
        return node in self.trail

    def last_visited(self):
        return self.trail[-1]

    def trail_length(self, edges):
        first_node, last_node = self.trail[0], self.trail[len(self.trail)-1]
        length = edges[last_node][first_node]
        for i in range(0, len(self.trail)-1):
            n1, n2 = self.trail[i], self.trail[i+1]
            length += edges[n1][n2]
        return length

    def calc_trail_length(self, edges):
        self.total_trail_length = self.trail_length(edges)
