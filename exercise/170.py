A = [5, 6, 10, 14, 18, 21, 49]
S = [5, 18, 49]

# Return if there are k elements prime among them. (5-6) (5-14) (5-18)
# Instead of (5-6) (6-14) (14-5)
def Verify_pairwise_prime(A, k, S):
    # if S not included in A:
    # return False
    if len(S) < k or len(S) > k:
        return False
    for i in range(0, len(S)):
        for j in range(i+1, len(S)):
            if CGD(S[i], S[j]) > 1:
                return False
    return True


# EUCLID'S ALGO
# if two pairs are prime the result is 1, otherwise is > 1
def CGD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a %b
        else:
            b = b % a
    return max(a, b)


#print(CGD(5,49))


print(Verify_pairwise_prime(A, 4, S))