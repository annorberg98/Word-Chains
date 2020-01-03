# Dijkstras algorithm for finding shortest paths in
# WeightedDigraph. Modeled after Sedgewick & Wayne's DijkstraSP,
# available at https://algs4.cs.princeton.edu/
#
# Jesper Larsson, Malmö University, 2018

from VertexPQ import VertexPQ

class Dijkstra:
    def __init__(self, G, s):
        edge_to = [-1] * G.V()

        q = VertexPQ(G.V())
        q.set_dist(s, 0)
        while not q.empty():
            v = q.del_min()
            for e in G.adj(v):
                w = e.to()
                if q.get_dist(w) > q.get_dist(v) + e.weight():
                    q.set_dist(w, q.get_dist(v) + e.weight())
                    edge_to[w] = v
                    
        def path(v):
            if q.get_dist(v) < 0:
                return None
            p = [v]
            while v != s:
                v = edge_to[v]
                p.append(v)
            p.reverse()
            return p
                        
        self.has_path_to = lambda v: q.get_dist(v) < float('inf')
        self.dist_to = lambda v: q.get_dist(v)
        self.path_to = path
