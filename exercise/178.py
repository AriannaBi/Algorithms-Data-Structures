P = [[1, 1], [3, 4], [5, 3], [7, 6]]

# Return the area of a minimal axis-aligned square that
# covers all points in P.
def Minimal_Covering_Square(P):
    if len(P) <= 3:
        return 0
    right = P[0][1]
    left = P[0][0]
    top = P[0][1]
    bottom = P[0][1]
    for i in range(1, len(P)):
        if P[i][0] > right:
            right = P[i][0]
        elif P[i][0] < left:
            left = P[i][0]
        if P[i][1] > top:
            top = P[i][1]
        elif P[i][1] < bottom:
            bottom = P[i][1]
    print(right, left, top, bottom)
    if right - left > top - bottom:
        return (right - left) * (right - left)
    else:
        return (top - bottom) * (top - bottom)

print(Minimal_Covering_Square(P))