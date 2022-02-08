A = [1,2,2,1,0]
B = [2,2,3,1]

# Find the longest common subsequence (not contiguous)
def longest_subsequence(A, B,  i, j, M):
    if j >= len(B) or i >= len(A):
        return 0
    if (i, j) in M:
        return M[(i, j)]
    elif A[i] == B[j]:
        res = 1 + longest_subsequence(A, B, i+1, j+1, M)
    else:
        res = max(longest_subsequence(A, B, i+1, j+1, M),
                   longest_subsequence(A, B, i+1, j, M),
                   longest_subsequence(A, B, i, j+1, M))
    M[(i, j)] = res
    return res

print(longest_subsequence(A, B, 0, 0, {}))




A = [2,3,0,7,3,9,3,1]
B = [2,3,3,3,3,1]


# Common maximal subsequence CONTIGUOUS!
def maximal_common_subsequence(A, B):
    m = 0
    for i in range(0, len(A)):
        for j in range(0, len(B)):
            l = 0
            while i + l < len(A) and j + l < len(B) and A[i+l] == B[j+l]:
                l = l + 1
            if l > m:
                m = l
    return m


print(maximal_common_subsequence(A, B))