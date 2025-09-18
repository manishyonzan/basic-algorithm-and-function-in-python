import heapq
def dijkstra(graph, start):
    heap =[(0, start)]
    shortest_path = {node: float('inf') for node in graph}
    shortest_path[start] = 0
    while heap:
        cost, node = heapq.heappop(heap)
        for neighbour,weight in graph[node]:
            new_cost = cost + weight
            if new_cost < shortest_path[neighbour]:
                shortest_path[neighbour] = new_cost
                heapq.heappush(heap, (new_cost,neighbour))
    return shortest_path

graph = {
    'A': [('B',1), ('C',4)],
    'B': [('A',1), ('C',2), ('D',5)],
    'C': [('A',4), ('B',2), ('D',1)],
    'D': [('B',5), ('C',1)]
}

print(dijkstra(graph=graph,start="A"))