# Demonstration of how to use Digraph and DFS.
#
# Jesper Larsson, Malmö University 2018

from Digraph import Digraph
from DFS import DFS

# Digraph example from lecture
G = Digraph(13)
G.addedge(0, 1)
G.addedge(0, 5)
G.addedge(2, 0)
G.addedge(2, 3)
G.addedge(3, 2)
G.addedge(3, 5)
G.addedge(4, 3)
G.addedge(4, 2)
G.addedge(5, 4)
G.addedge(6, 0)
G.addedge(6, 9)
G.addedge(6, 4)
G.addedge(7, 6)
G.addedge(7, 8)
G.addedge(8, 7)
G.addedge(8, 9)
G.addedge(9, 10)
G.addedge(9, 11)
G.addedge(10, 12)
G.addedge(11, 4)
G.addedge(11, 12)
G.addedge(12, 9)

# Perform depth-first search from s
s = 9
search = DFS(G, s)

# Print the nodes that were reached
for v in range(0, G.V()):
    if search.marked(v):
        print(v)
