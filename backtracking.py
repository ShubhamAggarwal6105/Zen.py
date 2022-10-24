def is_valid(g, r, c, n):
    for i in range(9):
        if g[r] == n: return 0

    for j in range(9):
        if g[c] == n: return 0
    
    # same number in 3x3 matrix or not
    sr = r - r % 3
    sc = c - c % 3

    for x in range(3):
        for y in range(3):
            if g[x + sr][y + sc] == n:
                return 0
    return 1

def Solve(g, r, c):
    if (r, c) == (8, 9):
        return 1 # to avoid further backtracking

    if c == 9:
        r, c = r + 1, 0

    if g[r][c] > 0:
        return Solve(g, r, c + 1)

    for _ in range(1, 10):
        if is_valid(g, r, c, _):
            g[r][c] = _
            if Solve(g, r, c + 1):
                return 1
        g[r][c] = 0
    return 0

