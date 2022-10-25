def Row(x):
    return [[x,i] for i in range(9)]

def Col(x):
    return [[i,x] for i in range(9)]

def Box(x):
    I,J = 3*(x//3),3*(x%3)
    return [[i+I,j+J] for j in range(3) for i in range(3)]
#
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

########################################

N = 9

def notInRow(arr, row):
    st = set()
    for i in range(0, 9):
        if arr[row][i] in st:
            return False
        if arr[row][i] != ' ':
            st.add(arr[row][i])
    return True

def notInCol(arr, col): 
    st = set()
    for i in range(0, 9):
        if arr[i][col] in st:
            return False
        if arr[i][col] != ' ':
            st.add(arr[i][col])
    return True

def notInBox(arr, startRow, startCol):
    st = set()
    for row in range(0, 3):
        for col in range(0, 3):
            curr = arr[row + startRow][col + startCol]
            if curr in st:
                return False
            if curr != ' ':
                st.add(curr)
    return True
 
def validBoard(arr):
    for row in range(0, 9):
        for col in range(0, 9):
            if not (notInRow(arr, row) and notInCol(arr, col) and\
            notInBox(arr, row - row % 3, col - col % 3)):
                return False
    return True
            

def isSafe(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
    for x in range(9):
        if grid[x][col] == num:
            return False
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def Solve(grid, row, col, possible):
    if not validBoard(grid):
        return False
    if (row == 8 and col == 9):
        return True
    if col == N:
        row += 1
        col = 0
    if grid[row][col] != " ":
        return Solve(grid, row, col + 1, possible)

    for num in possible[row][col]:
        if isSafe(grid, row, col, num):
            grid[row][col] = num
            if Solve(grid, row, col + 1, possible):
                return True
        grid[row][col] = " "
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
