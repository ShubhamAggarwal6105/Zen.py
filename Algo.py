def Row(x):
    return [[x,i] for i in range(9)]

def Col(x):
    return [[i,x] for i in range(9)]

def Box(x):
    I,J = 3*(x//3),3*(x%3)
    return [[i+I,j+J] for j in range(3) for i in range(3)]

def Check(grid,i,j, possible):
    for a,b in Row(i):
        x = possible[a][b]
        if x=='F': continue
        if grid[i][j] in x:
            x.remove(grid[i][j])
            possible[a][b]=x
        if x==[]: return False
    for a,b in Col(j):
        x = possible[a][b]
        if x=='F': continue
        if grid[i][j] in x:
            x.remove(grid[i][j])
            possible[a][b]=x
        if x==[]: return False
    for a,b in Box((j//3)+3*(i//3)):
        x = possible[a][b]
        if x=='F': continue
        if grid[i][j] in x:
            x.remove(grid[i][j])
            possible[a][b]=x
        if x==[]: return False
    return True

def main(grid, possible):
    temp_grid = [i[:] for i in grid]
    possible.clear()
    for i in range(9):
        possible.append([])
        for j in range(9):
            if grid[i][j]==' ':
                possible[i].append([1,2,3,4,5,6,7,8,9])
            else:
                possible[i].append('F')

    flag = True
    while True:
        for i in range(9):
            for j in range(9):
                if possible[i][j]=='F':
                    flag = Check(grid,i,j, possible)
                    if not flag: return False

        for a in range(9):
            for b in range(9):
                x = possible[a][b]
                if x=='F': continue
                if len(x)==1:
                    # print(a,b,x[0])
                    grid[a][b] = x[0]
                    possible[a][b] = 'F'
                    flag = Check(grid,a,b, possible)
                    if not flag: return False

        for i in range(9):
            
            d = [0]*10
            for a,b in Row(i):
                if possible[a][b] == 'F': continue
                for j in possible[a][b]:
                    d[j]+=1
            for k in range(1,10):
                if d[k]==1:
                    for a,b in Row(i):
                        if possible[a][b] == 'F': continue
                        if k in possible[a][b]:
                            # print("Row",a,b,k)
                            grid[a][b] = k
                            possible[a][b] = 'F'
                            flag = Check(grid,a,b, possible)
                            break
                    if not flag: return False

            d = [0]*10
            for a,b in Col(i):
                if possible[a][b] == 'F': continue
                for j in possible[a][b]:
                    d[j]+=1
            for k in range(1,10):
                if d[k]==1:
                    for a,b in Col(i):
                        if possible[a][b] == 'F': continue
                        if k in possible[a][b]:
                            # print("Col",a,b,k)
                            grid[a][b] = k
                            possible[a][b] = 'F'
                            flag = Check(grid,a,b, possible)
                            if not flag: return False
                            break

            d = [0]*10
            for a,b in Box(i):
                if possible[a][b] == 'F': continue
                for j in possible[a][b]:
                    d[j]+=1
            for k in range(1,10):
                if d[k]==1:
                    for a,b in Box(i):
                        if possible[a][b] == 'F': continue
                        if k in possible[a][b]:
                            # print("Box",a,b,k)
                            grid[a][b] = k
                            possible[a][b] = 'F'
                            flag = Check(grid,a,b, possible)
                            if not flag: return False
                            break

        if temp_grid == grid: return True
        temp_grid = [i[:] for i in grid]

def validBoard(arr):
    for x in range(9):
        s = set()
        for i,j in Row(x):
            if arr[i][j] in s: return False
            if arr[i][j] != ' ': s.add(arr[i][j])
        s = set()
        for i,j in Col(x):
            if arr[i][j] in s: return False
            if arr[i][j] != ' ': s.add(arr[i][j])
        s = set()
        for i,j in Box(x):
            if arr[i][j] in s: return False
            if arr[i][j] != ' ': s.add(arr[i][j])
    return True

def safe(grid, r, c, num):
    for a,b in Row(r):
        if grid[a][b]==num: return False
    for a,b in Col(c):
        if grid[a][b]==num: return False
    for a,b in Box((c//3)+3*(r//3)):
        if grid[a][b]==num: return False
    return True

def Solve(grid, r, c, possible):
    if not validBoard(grid): return False
    if (r == 8 and c == 9): return True
    if c == 9:
        r+=1
        c=0
    if grid[r][c] != " ":
        return Solve(grid, r, c+1, possible)
    for num in possible[r][c]:
        if safe(grid, r, c, num):
            grid[r][c] = num
            if Solve(grid, r, c+1, possible): return True
        grid[r][c] = " "
    return False

def foo(grid, possible):
    if not validBoard(grid):
        return False

    if not main(grid, possible):
        return False

    if not Solve(grid, 0, 0, possible):
        return False

    return grid

def _flatten(grid):
    for i in range(9):
        for j in range(9):
            grid[i][j] = int(grid[i][j])
            if grid[i][j] == 0:
                grid[i][j] = " "
    return grid

def is_empty(grid):
    for i in grid:
        for j in i:
            if j == " ":
                return True
    return False

def TextSolve(grid):
    grid = _flatten(grid)
    a = foo(grid, [])

    if a:
        print("valid solution formed:")
        print(a)

    else:
        print("no solution for this position.")

if __name__ == "__main__":
    grid = eval(input("enter board as 2D nested array: "))
    TextSolve(grid)
