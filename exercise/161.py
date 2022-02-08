A = [1,2,3,3,4,5,8]

# Return true if there are at least 2 elements with the distance k
# O(n log n)
def Find_Elements_At_Distance(A, k):
    for i in range(0, len(A)):
        if binary_search(A, A[i] + k):
            return True
    return False


def binary_search(A, k):
    first = 0
    last = len(A)-1
    while first <= last:
        middle = (first + last) // 2
        if k < A[middle]:
            last = middle - 1
        elif k > A[middle]:
            first = middle + 1
        else:
            return True
    return False

print(Find_Elements_At_Distance(A, 6))


# O(n)
def Find_Elements_At_Distance_i(A,k):
    j = 1
    i = 0
    while j < len(A):
        if A[j] - A[i] > k:
            i = i + 1
        elif A[j] - A[i] < k:
            j = j + 1
        else:
            return True
    return False

print(Find_Elements_At_Distance_i(A, 6))
