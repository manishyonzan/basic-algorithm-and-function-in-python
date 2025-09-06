import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g.add_edges_from([('A', 'B'),('A','C'),('B','C'),('D',"C")])
nx.draw(g,with_labels=True)
plt.show()