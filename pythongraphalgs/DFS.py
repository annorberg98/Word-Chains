# Depth-first search for finding connectedness in Digraph.
#
# Jesper Larsson, Malmö University, 2018

class DFS:
    def __init__(self, G, s):
        def dfs(G, v):
            marked[v] = True
            for w in G.adj(v):
                if (not marked[w]):
                    dfs(G, w)

        marked = [False] * G.V()
        dfs(G, s)

        self.marked = lambda v: marked[v] 
