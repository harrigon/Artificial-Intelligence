from search import *
from math import *

class LocationGraph(ExplicitGraph):
    def __init__(self, nodes, locations, edges, starting_list, goal_nodes, estimates=None):
        """Initialises an explicit graph.
        Keyword arguments:
        nodes -- a set of nodes
        edge_list -- a sequence of tuples in the form (tail, head) or 
                     (tail, head, cost)
        starting_list -- the list of starting nodes (states)
        goal_node -- the set of goal nodes (states)
        """


        
        self.locations = locations
        self.nodes = nodes 
        
        
        self.edges = set(edges)
        new_edges = set()
        for i in edges:
            reversed_edge = (i[1], i[0])
            new_edges.add(reversed_edge)
        self.edges = self.edges.union(new_edges)
       
        self.starting_list = starting_list
        self.goal_nodes = goal_nodes
        self.estimates = estimates
        
        self.edge_list = list(self.edges)
        self.edge_list.sort(key=lambda x: x[1])

        

            
    def euclidean_dist(self, nodeA, nodeB):
        return sqrt((nodeA[0] - nodeB[0])**2 + (nodeA[1] - nodeB[1])**2)
        
    def outgoing_arcs(self, node):
        """Returns a sequence of Arc objects corresponding to all the
        edges in which the given node is the tail node. The label is
        automatically generated."""

        for edge in self.edge_list:
            if len(edge) == 2:  # if no cost is specified
                tail, head = edge
                cost = self.euclidean_dist(self.locations[tail], self.locations[head])      
            else:
                tail, head, cost = edge
            if tail == node:
                yield Arc(tail, head, str(tail) + '->' + str(head), cost)
        
    
    

class OrderedExplicitGraph(ExplicitGraph):
    
    def __init__(self, nodes, edges, starting_list, goal_nodes, estimates=None):
        """Initialises an explicit graph.
        Keyword arguments:
        nodes -- a set of nodes
        edge_list -- a sequence of tuples in the form (tail, head) or 
                     (tail, head, cost)
        starting_list -- the list of starting nodes (states)
        goal_node -- the set of goal nodes (states)
        """

        # A few assertions to detect possible errors in
        # instantiation. These assertions are not essential to the
        # class functionality.
        assert all(tail in nodes and head in nodes for tail, head, *_ in edges)\
           , "edges must link two existing nodes!"
        assert all(node in nodes for node in starting_list),\
            "The starting_states must be in nodes."
        assert all(node in nodes for node in goal_nodes),\
            "The goal states must be in nodes."

        self.nodes = nodes      
        self.edges = edges
        self.starting_list = starting_list
        self.goal_nodes = goal_nodes
        self.estimates = estimates
        
        self.edge_list = list(self.edges)
        self.edge_list.sort(key=lambda x: x[1])
        self.edge_list.reverse()

        
        
class FunkyNumericGraph(Graph):
    """A graph where nodes are numbers. A node (number) n leads to n-1 and
    n+2. Nodes that are divisible by 10 are goal nodes."""
    
    def __init__(self, starting_number):
        self.starting_number = starting_number

    def outgoing_arcs(self, tail_node):
        yield Arc(tail_node, tail_node-1, label="1down", cost=1)
        yield Arc(tail_node,tail_node+2, label="2up", cost=1)
        
    def starting_nodes(self):
        yield self.starting_number

    def is_goal(self, node):
        return (node%10 == 0)     

class LCFSFrontier(Frontier):
    
    """Implements a frontier container appropriate for LCFS
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty list."""
        self.container = []


    def add(self, path):
        """Adds a new path to the frontier. A path is a sequence (tuple) of
        Arc objects. You should override this method.

        """        
  
        
        self.container.append(path)


    def __iter__(self):
        """Returns a generator. The generator selects and removes a path from
        the frontier and returns it. A path is a sequence (tuple) of
        Arc objects. Override this method according to the desired
        search strategy.

        """        

        while self.container:
            yield self.container.pop()
        
    
class BFSFrontier(Frontier):
    
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty list."""
        self.container = []


    def add(self, path):
        """Adds a new path to the frontier. A path is a sequence (tuple) of
        Arc objects. You should override this method.

        """        
        #print("Path being added", path)
        
        self.container.append(path)


    def __iter__(self):
        """Returns a generator. The generator selects and removes a path from
        the frontier and returns it. A path is a sequence (tuple) of
        Arc objects. Override this method according to the desired
        search strategy.

        """        

        while self.container:
            yield self.container.pop(0)
    
        

class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty list."""
        self.container = []


    def add(self, path):
        """Adds a new path to the frontier. A path is a sequence (tuple) of
        Arc objects. You should override this method.

        """        
        
        self.container.append(path)


    def __iter__(self):
        """Returns a generator. The generator selects and removes a path from
        the frontier and returns it. A path is a sequence (tuple) of
        Arc objects. Override this method according to the desired
        search strategy.

        """        

        while self.container:
            yield self.container.pop()

def main():
    
    graph = LocationGraph(nodes=set('ABC'),
                      locations={'A': (0, 0),
                                 'B': (3, 0),
                                 'C': (3, 4)},
                      edges={('A', 'B'), ('B','C'),
                             ('B', 'A'), ('C', 'A')},
                      starting_list=['A'],
                      goal_nodes={'C'})

    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)
    
    graph = LocationGraph(nodes=set('ABC'),
                          locations={'A': (0, 0),
                                     'B': (3, 0),
                                     'C': (3, 4)},
                          edges={('A', 'B'), ('B','C'),
                                 ('B', 'A')},
                          starting_list=['A'],
                          goal_nodes={'C'})
    
    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)
    
    pythagorean_graph = LocationGraph(
        nodes=set("abc"),
        locations={'a': (5, 6),
                   'b': (10,6),
                   'c': (10,18)},
        edges=[tuple(s) for s in {'ab', 'ac', 'bc'}],
        starting_list=['a'],
        goal_nodes={'c'})
    
    solution = next(generic_search(pythagorean_graph, LCFSFrontier()))
    print_actions(solution)    

if __name__ == "__main__":
    main()
