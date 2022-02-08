A = ['A', 'C', 'G', 'T']

B = ['B', 'B', 'D', 'A', 'C', 'G']


# Verify with the k length as input
def Verification151(s1, s2, k):
    C = [None]*k
    D = [None]*k
    if len(s1) < k or len(s2) < k:
        return False
    for i in range(0, len(s1) - k + 1):
        C = s1[i:i + k]
        for j in range(0, len(s2) - k + 1):
            D = s2[j:j + k]
            if C == D:
                return True
    return False


print(Verification151(A, B, 2))










A = ['A', 'C', 'G', 'T']

B = ['B', 'B', 'D', 'A', 'G', 'T']

C = ['G', 'T']

# Verify with the subsequence as input
def Verification(s1, s2, s3):
    c = 0
    if len(s1) < len(s3) or len(s2) < len(s3):
        return False
    for i in range(0, len(s1) - len(s3) + 1):
        if s1[i:i+len(s3)] == s3:
            c = 1
    for i in range(0, len(s2) - len(s3) + 1):
        if s2[i:i+len(s3)] == s3:
            c = 2
    if c == 2:
        return True
    return False


print(Verification(A, B, C))