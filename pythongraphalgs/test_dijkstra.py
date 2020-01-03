# Demonstration of how to use WeightedDigraph and Dijkstra.
#
# Jesper Larsson, Malmö University 2018

from WeightedDigraph import WeightedDigraph
from Dijkstra import Dijkstra

# Weighted digraph example from lecture
G = WeightedDigraph(8)
G.addedge(4, 5, 0.35)
G.addedge(5, 4, 0.35)
G.addedge(4, 7, 0.37)
G.addedge(5, 7, 0.28)
G.addedge(7, 5, 0.28)
G.addedge(5, 1, 0.32)
G.addedge(0, 4, 0.38)
G.addedge(0, 2, 0.26)
G.addedge(7, 3, 0.39)
G.addedge(1, 3, 0.29)
G.addedge(2, 7, 0.34)
G.addedge(6, 2, 0.40)
G.addedge(3, 6, 0.52)
G.addedge(6, 0, 0.58)
G.addedge(6, 4, 0.93)

# Calculate shortest paths from s
s = 0
search = Dijkstra(G, s)

# Print the nodes that were reached, with distance and path
for v in range(0, G.V()):
    if search.has_path_to(v):
        print(v, search.dist_to(v), search.path_to(v))
