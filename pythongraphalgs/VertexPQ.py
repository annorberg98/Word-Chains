# Priority queue, whose elements are ints, and whose priorities can be
# adjusted without taking them out of the queue. Modeled after
# Sedgewick & Wayne's heap class, specifically IndexMinPQ.java,
# available at https://algs4.cs.princeton.edu/
#
# Jesper Larsson, Malmö University 2018

class VertexPQ:
    def __init__(self, max_n):
        n = 0
        pq = [-1] * (max_n+1)             # vertices in heap order
        qp = [-1] * max_n                 # positions of vertices in pq
        dist_to = [float('inf')] * max_n  # keys of vertices, lower dist means higher prio

        def exch(i, j):
            v = pq[i]
            w = pq[j]
            pq[i] = w
            pq[j] = v
            qp[w] = i
            qp[v] = j
            
        def swim(k):
            while k > 1 and dist_to[pq[k//2]] > dist_to[pq[k]]:
                exch(k, k//2)
                k //= 2

        def sink(k):
            nonlocal n
            while 2*k <= n:
                j = 2*k
                if j < n and dist_to[pq[j]] > dist_to[pq[j+1]]:
                    j += 1
                if dist_to[pq[k]] <= dist_to[pq[j]]:
                    break
                exch(k, j)
                k = j

        def set_dist(v, d):
            if qp[v] < 0:                 # vertex not in queue, add it
                nonlocal n
                n += 1
                pq[n] = v
                qp[v] = n
                dist_to[v] = d
                swim(n)
            else:                         # already in queue, modify
                grows = d > dist_to[v]
                dist_to[v] = d
                if grows:
                    sink(qp[v])
                else:
                    swim(qp[v])

        def del_min():
            nonlocal n
            min = pq[1]
            exch(1, n)
            n -= 1
            sink(1)
            qp[min] = -1
            return min
            
        self.set_dist = set_dist
        self.get_dist = lambda v: dist_to[v]
        self.del_min = del_min
        self.empty = lambda: n == 0
