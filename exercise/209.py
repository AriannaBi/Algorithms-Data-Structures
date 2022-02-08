A = ['professor', 'prefers', 'to', 'teach', 'programming']

# Return the number of the letters of a prefix that is contained
# in at least k words.

A.sort()
print(A)

kn = 1
def common_max_prefix(A, k):
    global kn
    maxim = 0
    n = 0
    for i in range(0, len(A)-1):
        n = common_prefix(A[i], A[i+1])[0]
        n1 = common_prefix(A[i], A[i+1])[1]
        A[i+1] = n1
        if n == 0:
            kn = 1
        else:
            kn = kn + 1
        if maxim < n and kn >= k:
            maxim = n
    return maxim


def common_prefix(A,B):
    n = 0
    s = ' '
    for i in range(0, min(len(A), len(B))):
        if A[i] == B[i]:
            n = n + 1
            s = s + A[i]
        else:
            if s != ' ':
                s = s[1:]
                return n, s
    return n, B



print(common_max_prefix(A, 3))