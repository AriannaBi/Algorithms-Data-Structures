A = [31,32,33,34,35, 40, 44]


# Given an array of x coordinates and a length l,
# return the most congested segment in an interval l.
# 1,2,3,4,8,9 l= 3 is 1,2,3,4 because 4-1=3

def Most_Congested_Segment(A, l):
    A.sort()
    i = 0
    j = 1
    m = 0
    x = 0
    y = 0
    k = 0
    while j < len(A):
        if A[j] - A[i] > l:
            i = i + 1
            j = j + 1
            k = 0
        elif A[j] - A[i] <= l and k <= l:
            k = k + 1
            if j - i > m:
                x = i
                y = j
                m = j - i
            j = j + 1
    return x, y, m

print(Most_Congested_Segment(A, 3))
