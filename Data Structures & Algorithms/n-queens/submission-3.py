#diag1 (row + col)
#   j→  0 1 2 3
# i↓
# 0     0 1 2 3
# 1     1 2 3 4
# 2     2 3 4 5
# 3     3 4 5 6

#Bảng diag2 (row - col)
#   j→   0  1  2  3
# i↓
# 0      0 -1 -2 -3
# 1      1  0 -1 -2
# 2      2  1  0 -1
# 3      3  2  1  0


from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = [False] * n
        diag1 = [False] * (2 * n)
        diag2 = [False] * (2 * n)

        board = [["."] * n for _ in range(n)]

        def backtrack(i):
            if i == n:
                res.append(["".join(row) for row in board])
                return

            for j in range(n):
                if col[j] or diag1[i + j] or diag2[i - j + n]:
                    continue

                col[j] = True
                diag1[i + j] = True
                diag2[i - j + n] = True
                board[i][j] = "Q"

                backtrack(i + 1)

                col[j] = False
                diag1[i + j] = False
                diag2[i - j + n] = False
                board[i][j] = "."

        backtrack(0)
        return res