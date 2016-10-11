from search import *
import itertools, heapq

class MapGraph(Graph):
    """Represents a routing problem. The problem is given by a
    rectangular map in the form of a string. The map contains a
    starting state a goal state and typicaly a few obstacles. The
    objective is to find the shortest path from the starting point to
    the goal point."""

    def __init__(self, map_str):
        # cleaning up the map_str
        self.map =  map_str.splitlines()
        self.starting_list = []

        # initialising the starting and goal states
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] in "S":
                    self.starting_list.append((i,j))
                if self.map[i][j] in "G":
                    self.goal_node = (i,j)

    def starting_nodes(self):
        return self.starting_list

    def is_goal(self, node):
        return self.goal_node == node

    def outgoing_arcs(self, node):
        row, col = node
        directions_to_consider = [('N' , -1, 0),
                                  ('NE', -1, 1),
                                  ('E' ,  0, 1),
                                  ('SE',  1, 1),
                                  ('S' ,  1, 0),
                                  ('SW',  1, -1),
                                  ('W' ,  0, -1),
                                  ('NW', -1, -1)]
        return [Arc((row, col), (row + dr, col + dc), label, 1) for label, dr, dc in 
                directions_to_consider if self.map[row+dr][col+dc] in 'SG ']


    def estimated_cost_to_goal(self, node):
        """Reutrn the estimated cost to a goal state from the given
        state."""
        goal_row, goal_col = self.goal_node
        row, col = node
        delta_r, delta_c = abs(goal_row-row), abs(goal_col-col)
        return max(delta_r, delta_c)
        # return delta_r + delta_c #Manhattan
        # return math.sqrt(delta_r**2 + delta_c**2) #Euclidean
        

class PriorityFrontier(Frontier):
    """Implements a priority queue for lowest-cost-first search."""
    def __init__(self, heuristic=None, pruning=False, greedy=False):
        self.container = []
        self.count = itertools.count()
        self.heuristic = (heuristic.__getitem__ if type(heuristic) is dict
                          else heuristic)
        self.pruning = pruning
        self.visited = set()
        self.greedy = greedy
        assert not greedy or heuristic


    def add(self, path):
        cost = sum(arc.cost for arc in path) if not self.greedy else 0
        if self.heuristic:
            cost += self.heuristic(path[-1].head)
        if path[-1].head not in self.visited: #always satisfied without pruning
            heapq.heappush(self.container, (cost, next(self.count), path))


    
    def __iter__(self):
        while self.container:
            cost, _, path = heapq.heappop(self.container)
            if self.pruning:
                if path[-1].head in self.visited:
                    continue
                else:
                    self.visited.add(path[-1].head)
            yield path

class AStarFrontier(PriorityFrontier):
    def __init__(self, graph):
        super().__init__(heuristic=graph.estimated_cost_to_goal, pruning=True)


class LCFSFrontier(PriorityFrontier):
    def __init__(self):
        super().__init__(pruning=True)

        
def print_map(map_graph, frontier=[], solution=None):
    stars = {arc.head for arc in solution[1:-1]} if solution else set()
    for i in range(len(map_graph.map)):
        for j in range(len(map_graph.map[i])):
            if (i, j) in stars:
                print('*', end='')
            elif (i, j) in frontier.visited and map_graph.map[i][j] not in 'SG':
                print('.', end='')
            else:
                print(map_graph.map[i][j], end='')
        print()
