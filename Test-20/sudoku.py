from sys import stdin

def isValid(row, col, i, board):

    N = len(board)

    # check if row is valid
    for c in range(N):
        if board[row][c] == i:
            return False
        
    # check if column is valid
    for r in range(N):
        if board[r][col] == i:
            return False
        
    # check if 3x3 is valid
    start_r = (row//3) * 3
    end_r = start_r + 3

    start_c = (col//3) * 3
    end_c = start_c + 3

    for r in range(start_r, end_r):
        for c in range(start_c, end_c):
            if board[r][c] == i:
                return False    

    # all checks passed, is valid!
    return True

def solve(row, col, board):

    N = len(board)

    # check if complete row is solved
    if col == N:
        # check if its last valid row
        if row == N-1:
            # solved!
            return True
        else:
            # solve next row
            return solve(row+1, 0, board)

    else:
        # check if current cell is solved
        if board[row][col] != 0:
            # is solved so solve next column in row
            return solve(row, col+1, board)
        else:
            # is not solved, try to solve with 1 through 9
            for i in range(1, 10):
                # if is a valid placement
                if isValid(row, col, i, board):
                    board[row][col] = i
                    # if with this placement is solved
                    if solve(row, col+1, board):
                        # break recursion, solved!
                        return True
                    # current cell didn't solve it, backtrack
                    board[row][col] = 0

    # the recursive call didn't solve it
    return False

def readInput():
    lines = stdin.readlines()
    board = []
    for line in lines:
        line = list(map(int, line.strip().split()))
        board.append(line)
    return board

def printBoard(board):

    N = len(board)

    for i in range(N):
        if i % 3 == 0:
            print('-'*((2*N)+7))
        for j in range(N):
            if j == 0:
                print('| ', end='')
            if j % 3 == 0 and j != 0:
                print('| ', end='')
            print(f'{board[i][j]}', end=' ')
            if j+1 == N:
                print('|', end='')
        print()
    print('-'*((2*N)+7))

if __name__ == '__main__':
    board = readInput()
    print("Unsolved board:")
    printBoard(board)
    if (solve(0, 0, board)):
        print("Solved board:")
        printBoard(board)
    else:
        print("\nNo solution found for this board.\n")

