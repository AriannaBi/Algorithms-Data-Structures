#!/usr/bin/python3


# We represent a graph with an adjacency list
Adj = []                        # adjacency list, indexed by node id
V = []                          # vertex names, indexed by node id
V_idx = {}                      # name --> node id

def print_graph():
    global Adj, V, V_idx
    read_graph("B A C")
    print('V:')
    for i in range(len(V)):     # iteration over V
        print(i,V[i])
    print('E:')
    for v in range(len(V)):     # iteration over E
        for w in Adj[v]:
            print(v,w,' ( ',V[v],'-->',V[w],')')


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


import sys
read_graph(sys.stdin)


