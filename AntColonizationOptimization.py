import random

class AntColonyOptimization:

    def __init__(self, graph):
        self.alpha = 1.0
        self.beta = 1.5
        self.Q = 500
        self.evap_coeff = 0.5
        self.ant_factor = 0.8
        self.random_factor = 0.01
        self.max_iterations = 1000
        self.num_ants = ant_factor*num_nodes

        self.graph = graph
        self.trails = [[]]
        self.ants = []
        self.num_nodes = len(self.graph.nodes)
        self.starting_node = 0

        self.probabilities = []

        for ant in self.num_ants:
            ants.append(Ant(self.num_nodes, self.starting_node))

        self.trail_levels = [[0 for i in range(self.num_nodes)] for i in range(self.num_nodes)]

    def get_trail_level(self, n1, n2):
        """
            Given two nodes, return the trail level of the edge between
            them.
        """
        return self.trail_levels[n1][n2]

    def set_trail_level(self, n1, n2, new_level):
        """
            Given two nodes, set the trail level of the edge between
            them to new_level.
        """
        self.trail_levels[n1][n2] = new_level

    def gen_next_node(self, probabilities, total):
        """
            Given the probabilities for all possible edges and the sum
            of all probabilities, generate the next node to be traversed.
        """
        rand_num = random.uniform(0, 1) * denom
        for i in range(len(probabilities)):
            p = probabilities[i]
            if rand_num - p <= 0:
                return i

    def select_edge(self, ant):
        '''
            Given ant at specific node, calculates probabilities for
            each edge and randomly selects the next edge to traverse.
        '''
        curr_node = ant.last_visited().i
        numerators = []

        for n in range(self.num_nodes): #all nodes are neighbors for our purpose
            curr_numer = 0
            if n != curr_node: #guaranteed to not stay at same node
                attractiveness = 1 / self.graph.get_distance(curr_node, n)
                trail_level = self.get_trail_level(curr_node, n)
                curr_numer = attractiveness * trail_level
            numerators.append(curr_numer)

        total_probl = sum(numerators)
        probls = [n / total_probl for n in numerators]
        next_node = self.gen_next_node(probls, total_probl)
        ant.visit_node(next_node)

    def pheromone_update(self):
        ''' At the end of each iteration, update trails for all paths the ants took.'''
        return None

    def run_aco(self):
        '''
            Runs entire ACO algorithm.
        '''
        return None

    def best_tour(self):
        '''
            After ACO is run, finds the most optimal tour out of all the ants.
        '''
        return None
