#!/usr/bin/python3
import sys

# We represent a graph with an adjacency list
#
Adj = []                        # adjacency list, indexed by node id
V = []                          # vertex names, indexed by node id
V_idx = {}                      # name --> node id


# u is the parent, v is the adjacent/children
def read_graph(f):
    global Adj, V, V_idx
    # line format:
    # u [v1 v2 v3 ...]
    # meaning: u-->v1; u-->v2; u-->v3; ...
    for line in f:
        u = None
        for v_name in line.strip().split():
            if v_name in V_idx:
                v = V_idx[v_name]
            else:
                v = len(V)
                V_idx[v_name] = v
                V.append(v_name)
                Adj.append([])
            if u == None:
                u = v
            else:
                Adj[u].append(v)


def find_cycle():
    # Depth-first search
    # return P: previous vector,
    #        D: discovery times,
    #        F: finish times
    n = len(V)
    P = [None]*n
    D = [None]*n
    F = [None]*n
    t = 0                       # time ticker
    # we use a stack to schedule node visitations
    S = []
    for i in range(n):          # for every vertex
        if D[i] == None:        # not yet discovered
            S.append(i)         # we start a DFS
            P[i] = None
            while len(S) > 0:
                v = S[-1]
                if D[v] == None:
                    # we just discovered v
                    D[v] = t
                    t += 1
                    for w in Adj[v]:
                        if D[w] == None:
                            P[w] = v
                            S.append(w)
                        elif F[w] == None:
                            #cycle!
                            c = [v]
                            while P[v] != w:
                                c.append(v)
                                print(v)
                            c.append(w)
                            c.reverse()
                            return c
                else:
                    if F[v] == None:
                        F[v] = t
                        t += 1
                    del S[-1]
    return None


read_graph(sys.stdin)
print(find_cycle())
