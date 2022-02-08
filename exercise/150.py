A = [8,7,1,2,3,4,5]

# O(n)
def Three_Way_Partition(A, v):
    i = 0
    x = 0
    while A[i] < v:
        i = i + 1
    for j in range(i+1, len(A)):
        if A[j] < v:
            x = A[i]
            A[i] = A[j]
            A[j] = x
            i = i + 1
    p = i
    for j in range(i -1, len(A)):
        if A[j] == v:
            x = A[i]
            A[i] = A[j]
            A[j] = x
            i = i + 1
    q = i
    return A, p, q

print(Three_Way_Partition(A, 5))