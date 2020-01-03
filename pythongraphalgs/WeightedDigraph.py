# Weighted directed graph class, inspired by the corresponding Java
# class in Algorithms, 4th ed. by Sedgewick & Wayne, available at
# https://algs4.cs.princeton.edu/home/
#
# Jesper Larsson, Malmö University, 2018

import Bag

class Edge:
    def __init__(self, fro, to, weight):
        self._fro = fro
        self._to = to
        self._weight = weight
            
    def fro(self): return self._fro

    def to(self): return self._to

    def weight(self): return self._weight

class WeightedDigraph:
    def __init__(self, V):
        E = 0
        adj = [None] * V

        def addedge(v, w, weight):
            nonlocal E
            E += 1
            adj[v] = Bag.add(Edge(v, w, weight), adj[v])

        self.V = lambda: V
        self.E = lambda: E
        self.addedge = addedge
        self.adj = lambda v: adj[v] or []
