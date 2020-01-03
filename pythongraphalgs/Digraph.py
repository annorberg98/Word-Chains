# Directed graph class, inspired by the corresponding Java class in
# Algorithms, 4th ed. by Sedgewick & Wayne, available at
# https://algs4.cs.princeton.edu/home/
#
# Jesper Larsson, Malmö University, 2018

import Bag

class Digraph:
    def __init__(self, V):
        E = 0
        adj = [None] * V

        def addedge(v, w):
            nonlocal E
            E += 1
            adj[v] = Bag.add(w, adj[v])              # add w to adj[v]

        self.V = lambda: V
        self.E = lambda: E
        self.addedge = addedge
        self.adj = lambda v: adj[v] or []
