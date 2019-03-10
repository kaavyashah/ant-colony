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

    def select_edge(self, ant):
        '''
            Given ant at specific node, calculates probabilities for
            each edge and randomly selects the next edge to traverse.
        '''
        return None

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
