A = [ 1, 5, 19, 17, 12, 8, 5, 3, 2]

# A sequence of numbers is called unimodal if it is first
# strictly increasing and then strictly decreasing.
# Find the maximum of a unimodal sequence
def Unimodal_Find_Maximum(A):
    first = 0
    end = len(A)-1
    while first <= end:
        middle = (first + end) // 2
        if A[middle - 1] > A[middle]:
            end = middle - 1
        elif A[middle] < A[middle + 1]:
            first = middle + 1
        else:
            return A[middle]
    return "Not a unimodal sequence"

print(Unimodal_Find_Maximum(A))