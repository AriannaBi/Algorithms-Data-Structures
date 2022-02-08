A = [1,2,3,2,5,3,2,3,3]


# Return the number that is present with the maximal frequency.
def max_repeated_number(A):
    A.sort()
    x = 0
    y = 0
    k = 0
    i = 0
    j = 1
    while j < len(A) and i < len(A):
        if A[i] != A[j]:
            i = j
            j = j + 1
            k = 0
        else:
            k = k + 1
            j = j + 1
        if x < k:
            x = k
            y = A[i]
    return y


print(max_repeated_number(A))