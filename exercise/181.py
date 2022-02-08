import random
A = [5,8,4,3,10,7,16]

# Given an array, return q1 and q2 that divide the array into 3 subsequence,
# 1..q1-1 q1...q2-1 q2...end
def Three_Way_Partition(A, begin, end):
    q1 = begin
    q2 = q1 + 1
    for i in range(q2, end):
        if A[i] <= A[q1]:
            x = A[i]
            A[i] = A[q2]
            A[q2] = x
            if A[q2] < A[q1]:
                x = A[q1]
                A[q1] = A[q2]
                A[q2] = x
                q1 = q1 + 1
            q2 = q2 + 1
    return q1, q2


print(Three_Way_Partition(A, 0, len(A)))
print(A)
# Do a better quick sort with the three way partition
def Quicksort_better(A, begin, end):
    if begin < end:
        q1, q2 = Three_Way_Partition(A, begin, end)
        Quicksort_better(A, begin, q1)
        Quicksort_better(A, q2, end)

Quicksort_better(A, 0, len(A))
print(A)


