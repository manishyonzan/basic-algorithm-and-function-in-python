# The basic idea behind BFS is to explore a graph one layer at a time. It looks at all the neighbors of a starting node before moving on to the next level. A queue is used to keep track of what comes next.
# BFS is particularly useful for:
# Finding the shortest path in unweighted graphs
# Detecting connected components
# Crawling web pages

from collections import deque

graph = {
    'A': ['B','C'],
    'B': ['A','D','E'],
    'C': ['A','F'],
    'D': ['B'],
    'E': ['B','F'],
    'F': ['C','E']
}

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        print("node:", node)
        for neighbour in graph[node]:
            if not neighbour in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                
bfs(graph=graph,start="A")