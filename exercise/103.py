A = [7,62,5,57,12,39,5,8,16,48]


# Given an array return the array ordered by the modulo of 10. in place
def Modulo_Partition(A):
    for i in range(0, len(A)):
        for j in range(i + 1, len(A)):
            if A[j] % 10 <= A[i] % 10:
                x = A[i]
                A[i] = A[j]
                A[j] = x
    return A


print(Modulo_Partition(A))




