A = ['prefessor', 'prefers', 'to', 'teach', 'programming']

# Return the number of the letters of a prefix that is more frequence.

def common_max_prefix(A):
    maxim = 0
    for i in range(0, len(A)-1):
        for j in range(i+1, len(A)):
            n = common_prefix(A[i], A[j])
            if maxim < n:
                maxim = n
    return maxim

def common_prefix(A,B):
    n = 0
    for i in range(0, min(len(A), len(B))):
        if A[i] == B[i]:
            n = n + 1
        else:
            return n

print(common_max_prefix(A))