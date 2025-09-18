# DFS works differently from BFS. Instead of moving level by level, it follows one path as far as it can go before backtracking. Think of it as diving deep down a trail, then returning to explore the others.
# We can implement DFS in two ways:
# Recursive DFS, which uses the function call stack
# Iterative DFS, which uses an explicit stack


# DFS is especially useful for:
# Cycle detection
# Maze solving and puzzles
# Topological sorting


def dfs_recursive(graph,node,visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node,end=" -> ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs_recursive(graph, neighbour, visited)
        
        
        
graph = {
    'A': ['B','C'],
    'B': ['A','D','E'],
    'C': ['A','F'],
    'D': ['B'],
    'E': ['B','F'],
    'F': ['C','E']
}
# Explanation: DFS visits B after A, goes deeper into D, then backtracks to explore E and F, and finally visits C.
dfs_recursive(graph=graph,node="A")
print()

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if not node in visited:
            print(node, end=" -> ")
            visited.add(node)
            stack.extend(reversed(graph[node]))
            
dfs_iterative(graph=graph, start="A")
