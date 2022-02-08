# Algo-x return the starting and ending point of the minimal subsequence that have
# the same number inside greater at least k.

A = [1, 2, 1, 3, 4, 5, 1, 1]

def prova(A, k):
    l = float("-inf")
    r = float("+inf")
    for i in range(0, len(A)):
        c = 1
        j = i + 1
        while c < k and j < len(A):
            if A[i] == A[j]:
                c = c + 1
            j = j + 1
        if c == k and r - l > i - j:
            l = i
            r = j
            # These are the possibility, but we take the minimal sequence
            print(i, j-1)
    return l, r-1

print(prova(A, 2))