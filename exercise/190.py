A = [[1,0],[2,0],[3,0],[4,0],[5,0]]

# Given an array of A.x as distance and A.y as altitude,
# return the maximum distance in at most h altitude.
def Longest_Stretch(A, h):
    m = 0
    i = 0
    while i < len(A):
        a = A[i][1]
        b = A[i][1]
        j = i + 1
        while j < len(A):
            if A[j][1] > b:
                b = A[j][1]
            elif A[j][1] < a:
                a = A[j][1]
            if b - a <= h:
                if A[j][0] - A[i][0] > m:
                    m = A[j][0] - A[i][0]
            j = j + 1
        i = i + 1
    return m

print(Longest_Stretch(A, 3))