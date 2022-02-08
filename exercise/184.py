A = [5,5,5,5,5]

def even_then_odd(A):
    i = 0
    j = 1
    while j < len(A)-1 and i < len(A)-1:
        if A[i] % 2 == 0:
            i = i + 1
        if A[j] % 2 != 0:
            j = j + 1
        if A[i] % 2 != 0 and A[j] % 2 == 0:
            x = A[i]
            A[i] = A[j]
            A[j] = x
            i = i + 1
            j = j + 1
    return A

print(even_then_odd(A))