
# Arianna Bianchi
class Node:
    def __init__(self, value1, value2):
        self.key1 = value1
        self.key2 = value2
        self.left = None
        self.right = None


#  Two arrays of 2 dimensions.
A = []
B = []

# Copy the array A inside the array B with Θ(n).
for i in range(0, len(A)):
    B.append(A[i])


# The insertion of an element inside a BST has complexity O(n) in the worst case,
# # while in the best case is Θ(log n).
def bst_insert(t, k1, k2):
    if t is None:
        return Node(k1, k2)
    if k2 > t.key2:
        t.right = bst_insert(t.right, k1, k2)
    else:
        t.left = bst_insert(t.left, k1, k2)
    return t


# This function takes all the elements b in the array A and insert them inside the BST, one element for one loop.
# The for loop has complexity Θ(n) for every element n in the array A, and the
# Insertion algorithm as above, has complexity O(n).
# In the end we will have O(n * n)=O(n^2) so the complexity for create_bst is O(n^2).
def create_bst(B):
    for i in range(1, len(A)):
        bst_insert(t, B[i][0], B[i][1])


# I sort the array B which is the copy of A, in this way I have the array sorted increasingly in terms
# of a element, and in terms of b i create the BST.
B.sort()
t = Node(None, None)
if len(A) > 0:
    t = Node(B[0][0], B[0][1])
    create_bst(B)


# The output function takes the len of the array A and the array A.
# With a for loop Θ(n) I loop all the elements in the array A.
# For example, at the first loop, I call the bst_search_left O(log n) that takes this element and return the left child
# of the element in the BST. Then I call the bst_search_right that return the right child of the element in the BST.
# Then with a for loop Θ(n) I find the index, of the element in the array A, of the left and right child, and I store
# this inside the local variable "out".
# The complexity of the function output is O([n * log n] * n) which is O(n^2log n)
def output(n, A):
    if t == None:
        return Node()
    for i in range(0, n):  # values of array A
        out = ""
        l = bst_search_left(t, A[i][0], A[i][1])[0]
        l2 = bst_search_left(t, A[i][0], A[i][1])[1]
        r = bst_search_right(t, A[i][0], A[i][1])[0]
        r2 = bst_search_right(t, A[i][0], A[i][1])[1]
        if l != -1 and l2 != -1:
            for j in range(0, n):
                if l == A[j][0] and l2 == A[j][1]:
                    out = out + "  " + str(j + 1)
                    break
        else:
            out = out + " " + "-1"
        if r != -1 and r2 != -1:
            for j in range(0, n):
                if r == A[j][0] and r2 == A[j][1]:
                    out = out + "  " + str(j + 1)
                    break
        else:
            out = out + " " + "-1"
        print(out)


# Return the left child of the element composed by (k1,k2).
# Complexity O(log n)
def bst_search_left(t, k1, k2):
    if t == None:
        return -1, -1
    if t.key2 > k2:
        return bst_search_left(t.left, k1, k2)
    if t.key2 < k2:
        return bst_search_left(t.right, k1, k2)
    else:
        if t.key1 == k1:
            if t.left == None:
                return -1, -1
            return t.left.key1, t.left.key2
        return bst_search_left(t.left, k1, k2)


# Return the right child of the element composed by (k1,k2).
# Complexity O(log n)
def bst_search_right(t, k1, k2):
    if t == None:
        return -1, -1
    if t.key2 > k2:
        return bst_search_right(t.left, k1, k2)
    if t.key2 < k2:
        return bst_search_right(t.right, k1, k2)
    else:
        if t.key1 == k1:
            if t.right == None:
                return -1, -1
            return t.right.key1, t.right.key2
        return bst_search_right(t.left, k1, k2)


output(len(A), A)