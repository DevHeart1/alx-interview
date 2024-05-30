#!/usr/bin/python3
'''
Then N queens puzzle.
The challenge of placing N non-attacking queens
on an NxN chessboard.
'''
import sys

col = set()
posDiag = set()
negDiag = set()
res = []
board = []
temp = []
resMtx = []
count = 0


def solveNQueens(n):
    '''
    Implementation of the function that
    solves N queens puzzle.
    '''
    board = [['.'] * n for i in range(n)]

    def backtrack(r):
        '''
        Recursive puzzle solver.
        '''
        if r == n:
            copy = [''.join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = 'Q'

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = '.'
    backtrack(0)


if __name__ == "__main__":
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        print("Usage: nqueens N")
        exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)
    solveNQueens(int(sys.argv[1]))
    for row in res:
        for r in row:
            col = r.index('Q')
            temp.append([count, col])
            if(count == int(sys.argv[1]) - 1):
                count = 0
            else:
                count += 1
        resMtx.append(temp)
        temp = []
    for r in resMtx:
        print(r)
