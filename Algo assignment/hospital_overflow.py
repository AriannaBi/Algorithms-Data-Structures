def create_array(C, k):
    A = [0] * (C + 1)
    for i in range(0, C + 1):
        if i == 0:
            A[i] = C - 1
        else:
            if i > k:
                C = A[i - 1] + k
                A[i] = C - (i + 1)
            else:
                C = A[i - 1] + i
                A[i] = C - (i + 1)
    return A


def hospital_overflow(A):
    first = 0
    last = len(A) - 1
    while first <= last:
        middle = int((first + last) / 2)
        if (A[middle] < 0) and (A[middle - 1] >= 0):
            return middle + 1
        elif A[middle] == 0 and A[middle + 1] < 0:
            return middle + 2
        elif A[middle] > 0:
            first = middle + 1
        else:
            last = middle - 1


A = create_array(5, 2)
print(hospital_overflow(A))




