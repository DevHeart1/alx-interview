#!/usr/bin/python3
"""
Write a program that solves the N queens problem.
"""


import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)


def nQueens(n, i=0, a=[], b=[], c=[]):
    """Generates backtracking solutions for N queens problem"""
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                for solution in nQueens(n, i+1, a+[j], b+[i+j], c+[i-j]):
                    yield solution
    else:
        yield a


for solution in nQueens(n):
    answer = [[col, row] for col, row in enumerate(solution)]
    print(answer)
