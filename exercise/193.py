A = [1,2,3,4,3,5]

def contain_k_elements(A, k):
    tot = 1
    for i in range(0, len(A)):
        for j in range(i+1, len(A)):
            if A[i] == A[j]:
                tot = tot + 1
        if tot >= k:
            return True
    return False
print(contain_k_elements(A, 2))


B = [3,3,4,5,5,8,8]

def Group_Of_Equals(B, k):
    B.sort()
    i = 0
    j = 1
    while j < len(B):
        if B[i] == B[j]:
            if (j - i) + 1 >= k:
                return True
            j = j + 1
        else:
            i = j
            j = j + 1
    return False

print(Group_Of_Equals(B, 2))
