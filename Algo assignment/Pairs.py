
A = [3, 2, 5, 2, 1]
leng = len(A)
B = [0] * leng
left = 0
right = leng - 1


def I(A, left, right):
    n_of_pairs = 0
    if left < right:
        mid = int((left + right) / 2)
        n_of_pairs = I(A, left, mid)
        n_of_pairs = n_of_pairs + I(A, mid + 1, right)
        n_of_pairs = n_of_pairs + merge(A, left, mid, right)
    return n_of_pairs


def merge(A, left, mid, right):
    i = left
    j = mid + 1
    k = left
    n_of_pairs = 0
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            B[k] = A[i]
            k = k + 1
            i = i + 1
        else:
            B[k] = A[j]
            n_of_pairs = n_of_pairs + (mid - i + 1)
            k = k + 1
            j = j + 1
    while i <= mid:
        B[k] = A[i]
        k = k + 1
        i = i + 1
    while j <= right:
        B[k] = A[j]
        k = k + 1
        j = j + 1
    for x in range(left, right + 1):
        A[x] = B[x]
    return n_of_pairs


print(I(A, left, right))




