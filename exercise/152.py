A = [8,9,-50,2,3]
B = [2,3,-50,8,9]
D = [-6,2,-4,1,3,-1,5,-1]
# Dynamic programming: with i going from left to right, let x(i)
# be the value of the maximal contiguous sequence ending at position i.
# So, x(1) = A[1], x(i) = max{A[i] + x(i + 1), A[i]}

# From the C i take the maximum number.
C = []
def max_contiguous_subsequence(A, i, C):
    if i >= len(A):
        return 0
    else:
        res = max(A[i], A[i] + max_contiguous_subsequence(A, i + 1, C))
        C.append(res)
        return res

max_contiguous_subsequence(A, 0, C)
print(max(C))

C = []
max_contiguous_subsequence(B, 0, C)
print(max(C))

C = []
max_contiguous_subsequence(D, 0, C)
print(max(C))



# ------------------------------------------------------------------------
# Max sum of the array (sum of the positive numbers)
def sequence(A, i):
    if i >= len(A):
        return 0
    else:
        return max(A[i] + sequence(A, i+1), sequence(A, i + 1))

print(sequence(A, 0))



# Kadane algo
def Kadane(arr, n):
    current = A[0]
    next = A[0]
    for i in range(1, n):
        current = max(A[i], current + A[i])
        next = max(next, current)
    return next

#print(Kadane(A, len(A)))

