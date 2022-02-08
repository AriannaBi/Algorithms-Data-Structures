A = [1,2,5,4,3,6,7,8,9]

# Return the maximal number of increasing subsequence in the array
def max_incresing_subsequence(A):
    i = 0
    j = 1
    x = 0
    for j in range(0, len(A)):
        if A[j] > A[j - 1]:
            if j-i > x:
                x = j - i
        else:
            i = j

    return x+1

print(max_incresing_subsequence(A))