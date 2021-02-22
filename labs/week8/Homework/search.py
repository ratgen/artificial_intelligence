class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)   # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH)


'''
Search the tree for the goal state and return path from initial state to goal state
'''
def TREE_SEARCH():
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while fringe is not None:
        node = REMOVE_FIRST(fringe)
        if node.STATE == GOAL_STATE:
            return node.path()
        children = EXPAND(node)
        fringe = INSERT_ALL(children, fringe)
        print("fringe: {}".format(fringe))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''
def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(node)  # create node for each in state list
        s.STATE = child  # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        successors = INSERT(s, successors)
    return successors


'''
Insert node in to the queue (fringe).
'''
def INSERT(node, queue):
   queue.insert(0, node)
   return queue
    


'''
    Insert list of nodes into the fringe
'''
def INSERT_ALL(list, queue):
    for item in list:
        queue.insert(0, item)
    return queue


'''
Removes and returns the first element from fringe
'''
def REMOVE_FIRST(queue):
    return queue.pop(0)

'''
Successor function, mapping the nodes to its successors
'''
def successor_fn(state):  # Lookup list of successor states
    children = STATE_SPACE[state]  # successor_fn( 'C' ) returns ['F', 'G']

    children.remove(state) #the state itself should not be included

    illegal_states = [('W', 'W', 'E', 'E'), ('W','E','E','W')]
    for remove_state in illegal_states:
        if remove_state in children[:]: 
            print('remove state')
            children.remove(remove_state)

    if state[0] == 'E':
        for item in children[:]:
            if item[0] != 'W':
                children.remove(item)

    for index in range(1,4):
        if state[index] == 'E':
            for item in children[:]:
                if item[index] != 'E':
                    children.remove(item) 
    
    return children



INITIAL_STATE = ('W', 'W', 'W', 'W') #We represent the a state with a tuple: (location, A status, B status)
GOAL_STATE = ('E', 'E', 'E', 'E') 
PERMUTATIONS = [('E', 'W', 'W', 'W'), ('W', 'E', 'W', 'E'), ('E', 'W', 'E', 'W'), ('E', 'E', 'E', 'E'), ('E', 'E', 'E', 'W'), ('E', 'E', 'W', 'E'), ('W', 'E', 'W', 'W'), ('W', 'E', 'E', 'E'), ('E', 'W', 'W', 'E'), ('E', 'W', 'E', 'E'), ('W', 'W', 'E', 'E'), ('W', 'W', 'W', 'E'), ('W', 'E', 'E', 'W'), ('E', 'E', 'W', 'W'), ('W', 'W', 'E', 'W'), ('W', 'W', 'W', 'W')]

STATE_SPACE = {}
for item in PERMUTATIONS:
    STATE_SPACE[item] = PERMUTATIONS

'''
Run tree search and display the nodes in the path to goal node
'''
def run():
    path = TREE_SEARCH()
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()