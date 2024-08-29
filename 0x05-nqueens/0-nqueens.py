#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    """ Check if a queen can be placed on board at row, col """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(board, col, results):
    """ Solve N Queens using backtracking """
    if col == len(board):
        result = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    result.append([i, j])
        results.append(result)
        return True
    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1, results) or res
            board[i][col] = 0
    return res

def nqueens(N):
    """ Initialize board and start solving """
    board = [[0 for _ in range(N)] for _ in range(N)]
    results = []
    solve_nqueens(board, 0, results)
    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solutions = nqueens(N)
    for solution in solutions:
        print(solution)

