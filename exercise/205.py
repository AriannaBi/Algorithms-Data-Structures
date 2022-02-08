#!/usr/bin/python3
import sys

# We represent a graph with an adjacency list

Adj = []                        # adjacency list, indexed by node id
V = []                          # vertex names, indexed by node id
V_idx = {}                      # name --> node id


def graph_degree():
    global Adj, V, V_idx
    x = 0
    for i in range(0, len(Adj)):
        if x < len(Adj[i]):
            x = len(Adj[i])
    return x


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


read_graph(sys.stdin)
print(V)
print(graph_degree())