A = [1,2,3,4,5,6,7]

# Given an array, return the array partitioned by first prime elements and then composites elements. in place

# O(sqrt(m))
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True


#print(is_prime(1))

# O(n*srqt(m))
def Partition_Primes_Composites(A):
    j = 1
    i = 0
    while j <= len(A)-1:
        if not is_prime(A[i]) and is_prime(A[j]):
            x = A[i]
            A[i] = A[j]
            A[j] = x
            i = i + 1
            j = j + 1
        elif not is_prime(A[j]):
            j = j + 1
    return A

print(Partition_Primes_Composites(A))




