#!/usr/bin/python3
import sys

# Each vertex has to be connected with a vertex that has not the same color.
# the colors are green and red


# We represent a graph with an adjacency list
#
Adj = []                        # adjacency list, indexed by node id
V = []                          # vertex names, indexed by node id
V_idx = {}                      # name --> node id
# P = [None] * len(V)

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

def is_bipartite(s):
    global Adj, V, V_idx
    # the stack
    Q = [s]
    # every element deleted form the stack
    Q1 = []
    # set all the vertices as green
    for i in range(0, len(V)):
         V[i] = V[i], "green"
    while len(Q) > 0:
        v = Q[0]
        # we are in the children
        for w in Adj[v]:
            if w not in Q1:
                Q.append(w)
                # if the parent is green, do the children red
                if V[v][1] == "green":
                    V[w] = V[w][0], "red"
            if V[v][1] == V[w][1]:
                return False
        # dequeue from Q and add to Q1
        Q1.append(Q[0])
        del Q[0]
    # it means that there are some vertex not connected to the graph
    if len(V) != len(Q):
        return False
    return True


read_graph(sys.stdin)
print_graph()
print(is_bipartite(0))
print("v", V)
print("vidx",V_idx)
print("Adj",Adj)


