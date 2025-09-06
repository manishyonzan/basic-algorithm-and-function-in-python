"""
Understanding Graphs in Python
A graph consists of nodes (vertices) and edges (relationships).

For examples, in a social network, people are nodes and friendships are edges. Or in a roadmap, cities are nodes and roads are edges.

There are a few different types of graphs:

Directed: edges have direction (one-way streets, task scheduling).

Undirected: edges go both ways (mutual friendships).

Weighted: edges have values (distances, costs).

Unweighted: edges are equal (basic subway routes).

Now that you know what graphs are, let’s look at the different ways they can be represented in Python.


Ways to represent graphs in python

adjacency matrix
An adjacency matrix is a 2D array where each cell (i, j) shows whether there is an edge from node i to node j.
In an unweighted graph, 0 means no edge, and 1 means an edge exists.
In a weighted graph, the cell holds the edge weight.

This makes it very quick to check if two nodes are directly connected (constant-time lookup), but it uses more memory for large graphs.
graph = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

Here, the matrix shows a fully connected graph of 3 nodes. For example, graph[0][1] = 1 means there is an edge from node 0 to node 1.


Adjacency List
An adjacency list represents each node along with the list of nodes it connects to.

This is usually more efficient for sparse graphs (where not every node is connected to every other node). It saves memory because only actual edges are stored instead of an entire grid.

graph = {
    'A': ['B','C'],
    'B': ['A','C'],
    'C': ['A','B']
}
Here, node A connects to B and C, and so on. Checking connections takes a little longer than with a matrix, but for large, sparse graphs, it’s the better option



"""