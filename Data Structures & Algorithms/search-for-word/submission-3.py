class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Rows = len(board)
        Cols = len(board[0])
        visited = [[False for _ in range(Cols)] for _ in range(Rows)]
        def dfs(r,c,i):
            if i == len(word):
                return True
            if(r<0 or c<0 or r>=Rows or c>=Cols
                   or board[r][c] != word[i] or visited[r][c]):
                return False
            visited[r][c] = True
            res = dfs(r-1,c,i+1) or dfs(r+1,c,i+1) or dfs(r,c-1,i+1) or dfs(r,c+1,i+1)
            visited[r][c] = False
            return res
        for i in range(Rows):
            for j in range(Cols):
                if dfs(i,j,0):
                    return True
        return False