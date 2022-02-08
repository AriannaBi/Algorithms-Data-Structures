#!/usr/bin/python3
import sys

# We represent a graph with an adjacency list
#
Adj = []                        # adjacency list, indexed by node id
V = []                          # vertex names, indexed by node id
V_idx = {}                      # name --> node id


def print_graph():
    global Adj, V, V_idx
    print('V:')
    for i in range(len(V)):     # iteration over V
        print(i, V[i])
    print('E:')
    for v in range(len(V)):     # iteration over E
        for w in Adj[v]:
            print(v, w, ' ( ', V[v], '-->', V[w], ')')


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


def bfs(s):
    # Breadth-first search starting from vertex s
    # return D: distance vector, P: previous vector
    global Adj, V
    n = len(V)
    D = [None]*n
    P = [None]*n
    # start from s
    D[s] = 0
    # we use a queue to schedule node visitations
    Q = [s]
    while len(Q) > 0:
        v = Q[0]                # main parent
        del Q[0]                # dequeue
        for w in Adj[v]:        # iterate over v's neighbors
            if D[w] == None:
                D[w] = D[v] + 1
                P[w] = v
                Q.append(w)     # enqueue
    return D, P


read_graph(sys.stdin)

print_graph()

print(V)
print(bfs(0)[0])
print(bfs(0)[1])


# D, P = bfs(0)
