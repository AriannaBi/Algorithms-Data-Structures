A = [[3,0],[3,5], [6,8], [6,2],[8,0],[8,5]]


# Find if there is a square
# O(n^4)
def Find_Square(A):
    for x1 in range(0, len(A)):
        for x2 in range(x1 + 1, len(A)):
            if A[x1][0] == A[x2][0]:
                for x11 in range(0, len(A)):
                    for x22 in range(x11 + 1, len(A)):
                        if A[x11][0] == A[x22][0] and A[x11][0] != A[x1][0]:
                            if abs(A[x1][1]-A[x11][1]) == abs(A[x2][1]-A[x22][1]) \
                                    and abs(A[x11][0] - A[x1][0]) == abs(A[x1][1]-A[x2][1]):
                                return True
    return False


print("There are square n^4?: ", Find_Square(A))

def Binary_Search_2D(A, x, y):
    A.sort()
    first = 0
    last = len(A) - 1
    while first <= last:
        middle = (first + last) // 2
        if A[middle][0] < x:
            first = middle + 1
        elif A[middle][0] > x:
            last = middle - 1
        elif first == last and A[first][0] == x and A[first][1] == y:
            return True
        elif first == last:
            return False
        elif A[middle][1] < y:
            first = middle + 1
        elif A[middle][1] > y:
            last = middle - 1
        else:
            return True
    return False


#print(Binary_Search_2D(A, 3,3))


# O(n^2 log n)
def Find_Square_i(A):
    A.sort()
    for i in range(0, len(A)):
        for j in range(i + 1, len(A)):
            dx = A[j][0] - A[i][0]
            dy = A[j][1] - A[i][1]
            if Binary_Search_2D(A, A[i][0] + dy, A[i][1] - dx) and Binary_Search_2D(A, A[j][0] + dy, A[j][1] - dx):
                return True
    return False


print(Find_Square_i(A))