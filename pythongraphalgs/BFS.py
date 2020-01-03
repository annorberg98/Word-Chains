# Breadth-first search for finding shortest paths in Digraph.
#
# Jesper Larsson, Malmö University, 2018

import collections

class BFS:
    def __init__(self, G, s):
        edge_to = [-1] * G.V()
        dist_to = [-1] * G.V()

        q = collections.deque()
        q.append(s)
        dist_to[s] = 0
        while q:                      # while q not empty
            v = q.popleft()
            for w in G.adj(v):
                if dist_to[w] < 0:     # if w not visited
                    q.append(w)
                    edge_to[w] = v
                    dist_to[w] = dist_to[v] + 1

        def path(v):
            if dist_to[v] < 0:
                return None
            p = [v]
            while v != s:
                v = edge_to[v]
                p.append(v)
            p.reverse()
            return p
                        
        self.has_path_to = lambda v: dist_to[v] >= 0
        self.dist_to = lambda v: dist_to[v]
        self.path_to = path

