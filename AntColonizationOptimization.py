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
            self.ants.append(Ant(self.num_nodes, self.starting_node))

        self.trail_levels = [[0 for i in range(self.num_nodes)] for i in range(self.num_nodes)]

    def get_trail_level(self, n1, n2):
        """
            Given two nodes, return the trail level of the edge between
            them.
        """
        return self.trail_levels[n1][n2]

    def incre_trail_level(self, n1, n2):
        """
            Given two nodes, incremenr the trail level of the edge between
            them.
        """
        self.trail_levels[n1][n2] += 1

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


        #don't we need to account for visited nodes?

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
        self.incre_trail_level(curr_node, next_node)
        ant.visit_node(next_node)


    def pheromone_update(self):
        ''' At the end of each iteration, update trails for all paths the ants took.'''
        for trail in len(self.trails):
            curr_prob = self.probabilities[i]
            level = self.trail_level[i]
            total_pheremone = 0
            for ant in self.ants:
                if ant.has_visited(trail):
                    kth_val = self.Q / ant.trail_length(self.graph.edges)
                    total_pheremone += kth_val
            self.trail_level[i] = (1 - curr_prob)*self.trail_level[i] +  total_pheremone
        return None

    def run_aco(self):
        '''
            Runs entire ACO algorithm.

            ISSUE: Not taking into account the weight of final point back to starting point to complete tour
        '''
        for i in range(10): #arbitrary stopping point
            for ant in self.ants:
                while not len(ant.visited) == num_nodes: #while the tour is not complete/the ant has not visited all nodes
                    select_edge(ant) #move the current ant further along

            pheromone_update() #perform the pheromone_update

            #reset the ants for the new iteration
            self.ants = []

            for ant in self.num_ants:
                ants.append(Ant(self.num_nodes, self.starting_node))


    def best_tour(self):
        '''
            After ACO is run, finds the most optimal tour out of all the ants.
        '''
        best_path = []

        copy_trail_levels = [x[:] for x in self.trail_levels] #prevent mutation of original trail_levels list

        current_node = self.starting_node

        while len(best_path) < self.num_nodes: #while the tour is not complete
            best_path.append(current_node) #update the best path

            next_node = max(copy_trail_levels[current_node]) #find the next trail with the highest level

            #prevents repeat nodes in best path
            #COMMENT: probably not necessary if ACO is implemented correctly
            if next_node in best_path:
                copy_trail_levels[current_node][next_node] = 0
                continue

            current_node = next_node

        return best_path
