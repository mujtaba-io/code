
# create Node for graph for DFS

class Node:
    def __init__(self, state, parent, action, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

# make graph based on Node
        
graph = {
    'A': Node('A', None, ['B', 'E', 'C'], 0),
    'B': Node('B', None, ['D', 'E', 'A'], 0),
    'C': Node('C', None, ['A', 'F', 'G'], 0),
    'D': Node('D', None, ['B', 'E'], 0),
    'E': Node('E', None, ['A', 'B', 'D'], 0),
    'F': Node('F', None, ['C'], 0),
    'G': Node('G', None, ['C'], 0),
}

# DFS algorithm

def dfs(graph, start, goal):
    stack = []
    stack.append(start)
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node == goal:
                return visited
            for neighbor in graph[node].action:
                stack.append(neighbor)
    return visited

# test

print(dfs(graph, 'D', 'C'))
