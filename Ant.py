class Ant:
    def __init__(self, starting_node):
        self.trail = []
        self.visited = []
        self.visited.append(starting_node)

    def visit_node(self, node):
        self.trail.append(node)
        self.visited[node] = True

    def has_visited(self, node):
        return self.visited[node]

    def last_visited(self):
        return self.visited[-1]

    def trail_length(self, edges):
        first_node, last_node = self.trail[0], self.trail[len(self.trail)-1]
        length = edges[last_node][first_node]
        for i in range(0, len(self.trail)-1):
            n1, n2 = self.trail[i], self.trail[i+1]
            length += edges[n1][n2]
        return length
