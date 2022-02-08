A = [1,2,3,4,5,6,7,8,9,10]
# Maximal distance in the array


def Maximal_Distance(A):
    max = A[0]
    min = A[0]
    for i in range(0, len(A)):
        if A[i] > max:
            max = A[i]
        if A[i] < min:
            min = A[i]
    return max - min


print(Maximal_Distance(A))