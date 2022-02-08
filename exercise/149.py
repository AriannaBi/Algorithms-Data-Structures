A = [1,5,4,3,3,3,4,5,6,7]


def algo149(A):
    a = 0
    for i in range(0, len(A)-1):
        for j in range(i+1, len(A)):
            x = 0
            for k in range(i, j+1):
                if A[k]%2 == 0:
                    x = x + 1
                else:
                    x = x - 1
            if x == 0 and j - i > a:
                a = j - i
    return a


print(algo149(A))

# Instead of check the x out of the loop, i check the x while the loop is running
# in this way i can do O(n^2) instead of O(n^3)
def betteralgo149(A):
    j = 0
    x = 0
    a = 0
    for i in range(0, len(A)):
        x = 0
        for j in range(i, len(A)):
            if A[j]%2 == 0:
                x = x + 1
            else:
                x = x - 1
            if x == 0 and j - i > a:
                a = j - i
    return a


print(betteralgo149(A))