class Solution(object):
    def solveNQueens(self, n):
        res = []
        board = [['.'] * n for _ in range(n)]

        def safe(r, c):
            for i in range(r):
                if board[i][c] == 'Q':
                    return False
                if c-r+i >= 0 and board[i][c-r+i] == 'Q':
                    return False
                if c+r-i < n and board[i][c+r-i] == 'Q':
                    return False
            return True

        def backtrack(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return

            for c in range(n):
                if safe(r, c):
                    board[r][c] = 'Q'      
                    backtrack(r + 1)      
                    board[r][c] = '.'      

        backtrack(0)
        return res