class Node:
    def __init__(self, value):
        self.key = value
        self.right = None
        self.left = None


# O(log n)
def bst_insert(t, k):
    if t is None:
        return Node(k)
    if k > t.key:
        t.right = bst_insert(t.right, k)
    else:
        t.left = bst_insert(t.left, k)
    return t


A = [10,5,13,4,7,11,15,6,8,12,14,17,17]
t = None
for a in A:
    if t == None:
        t = Node(a)
    else:
        bst_insert(t, a)


def BST_Height_i(t):
    if t is None:
        return 0
    return 1 + max(BST_Height_i(t.right), BST_Height_i(t.left))


print(BST_Height_i(t))
