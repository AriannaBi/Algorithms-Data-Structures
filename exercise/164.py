A = [7, 89, 11, 88, 106, 4, 28, 71, 17]


def Minimal_Simplified_Subset(A):
    X = []
    A.sort()
    B = [0]*len(A)
    for i in range(0, len(A)):
        j = 0
        k = 0
        while k < len(A):
            if A[k] - A[j] < A[i]:
                k = k + 1
            elif A[k] - A[j] > A[i]:
                j = j + 1
            else:
                B[k] = 1
                k = k + 1
    for i in range(0, len(A)):
        if B[i] == 0:
            X.append(A[i])
    return X


print(Minimal_Simplified_Subset(A))


