A = [1,4,2,8,3]

#Return the maximal NON adjacent sequence of the array
# Recursive Method
def max_non_adjacent_sequence(A, i):
    if i < 0:
        return 0
    else:
        return max(A[i] + max_non_adjacent_sequence(A, i-2), max_non_adjacent_sequence(A, i-1))
        # il totale non mi serve perché il risultato é gia storato nel return
        # return max(A[i] + max_non_adjacent_sequence(A, total+A[i], i-2),
        # max_non_adjacent_sequence(A, total, i-1))

print(max_non_adjacent_sequence(A, len(A)-1))








def max_non_adjacent_sequence_i(A, i):
    if i >= len(A):
        return 0
    else:
        return max(max_non_adjacent_sequence_i(A, i + 1), A[i] + max_non_adjacent_sequence_i(A, i + 2))

print(max_non_adjacent_sequence_i(A, 0))








# Dynamic Programming
def dp(A, i, mem):
    if i in mem:
        return mem[i]
    if i < 0:
        return 0
    else:
        res = max(A[i] + dp(A, i-2,mem), dp(A, i-1,mem))
    mem[i] = res
    return res

print(dp(A, len(A)-1, {}))










def max_non_adjacent_seq(A):
    p = 0
    q = 0
    r = 0
    for i in range(0, len(A)):
        r = max(A[i] + p, q)
        p = q
        q = r
    return r

print(max_non_adjacent_seq(A))